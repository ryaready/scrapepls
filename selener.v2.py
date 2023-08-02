from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(r'/Users/aishwaryaiyer/Desktop/chrome-mac-x64/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


def scrape_stackoverflow_results(url):

        try:

                driver.get(url)

                question_summary_element = driver.find_element(By.CLASS_NAME, "search-result")
                question_summary = summary.question_summary_element.text.strip()

                print("Question Summary:", summary)

                title_element = summary_element.find_element(By.CLASS_NAME, "s-post-summary--content-title")
                question_title = title_element.text.strip()
                question_url = title_element.get_attribute("href")

                print("Question Title:", question_title)
                print("Question URL:", question_url)


                try:

                        accepted_answer_element = result.find_element(By.CLASS_NAME, ".answer.js-answer.accepted-answer.js-accepted-answer .s-prose.js-post-body")
                        accepted_answer = accepted_answer_element.text.strip()

                        print("Accepted Answer:", accepted_answer)


                except:

                        print("No accepted answer found for this question.")

                print("--------------------------------------------------")


                next_page_element = driver.find_element(By.CLASS_NAME, "s-pagination--item__next")

                if next_page_element.is_enabled():

                        next_page_element.click()
                        scrape_stackoverflow_results(driver.current_url)

        finally:

                driver.quit()


if __name__ == "__main__":

        base_url = "https://stackoverflow.com/search?page={}&tab=Relevance&pagesize=50&q=readiness%20probe%20hasaccepted%3ayes&searchOn=3"
        scrape_stackoverflow_results(base_url.format(1))
