from bs4 import BeautifulSoup
import requests
import csv
import time

# base url
url = "https://stackoverflow.com/search?"
page_Limit = 1000
url2 = "&tab=Relevance&pagesize=50&q=readiness%20probe%20hasaccepted%3ayes&searchOn=3"

def build_url(base_url = url , ur_pt2 = url2, page = 1):
    return f"{base_url}page={page}{ur_pt2}"

def scrape_page(page=1):
    url = build_url(page=page)
    print(url)
    response = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(response.text,"html.parser")
    print("souped the search page NOT question")
    question_summary = soup.find_all("div", class_="s-post-summary--content")
    print(question_summary, "printed")

    for summary in question_summary:
        question = summary.find(class_="s-post-summary--content-title").text
        print(question)
        a = summary.find(class_="s-post-summary--content-title", href = True)
        print(a["href"])
        question_url = a["href"]
        question_page = request.get(question_url)
        time.sleep(2)
        question_soup = BeautifulSoup(question_page.text,"html.parser")
        accepted_answer = question_soup.find(class_= "answer js-answer accepted-answer js-accepted-answer").find(class_= "s-prose js-post-body").text
        print("found the acceptred answers youre gonna type pr somehyting arent u")
        with open("stack_data.tsv", "a")as f:
            f.write(f"{question}\t{accepted_answer}\n")
        break

def scrape():
    for i in range(2,page_Limit+1):
        print(f"about to querty ah um search page{i}")
        scrape_page (i)
        break

if __name__ == "__main__":
    scrape()

