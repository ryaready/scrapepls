from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    # Provide the path to the ChromeDriver executable without spaces and escape characters
    chrome_driver_path = '/Users/aishwaryaiyer/Desktop/chrome-mac-x64/chromedriver'
    chrome_options.binary_location = '/Users/aishwaryaiyer/Desktop/chrome-mac-x64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome'  # Path to the Chrome application
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    return driver


def scrape_stackoverflow_results(url):
    driver = setup_chrome_driver()
    driver.get(url)

        # Get all search result elements
        search_results = driver.find_elements_by_class_name("search-result")

        for result in search_results:
            # Extract the question summary
            summary_element = result.find_element_by_class_name("s-post-summary--content")
            summary = summary_element.text.strip()

            # Extract the question title and URL
            title_element = summary_element.find_element_by_class_name("s-post-summary--content-title")
            question_title = title_element.text.strip()
            question_url = title_element.get_attribute("href")

            print("Question Summary:", summary)
            print("Question Title:", question_title)
            print("Question URL:", question_url)

            # Check if an accepted answer is present
            try:
                accepted_answer_element = result.find_element_by_css_selector(".answer.js-answer.accepted-answer.js-accepted-answer .s-prose.js-post-body")
                accepted_answer = accepted_answer_element.text.strip()
                print("Accepted Answer:", accepted_answer)
            except:
                print("No accepted answer found for this question.")

            print("--------------------------------------------------")

        # Go to the next page if available
        next_page_element = driver.find_element_by_class_name("s-pagination--item__next")
        if next_page_element.is_enabled():
            next_page_element.click()
            scrape_stackoverflow_results(driver.current_url)

    finally:
        driver.quit()

if __name__ == "__main__":
  base_url = "https://stackoverflow.com/search?page={}&tab=Relevance&pagesize=50&q=readiness%20probe%20hasaccepted%3ayes&searchOn=3"
  scrape_stackoverflow_results(base_url.format(1))
