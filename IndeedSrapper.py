import time

from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.indeed.com/q-python-jobs.html").text

soup = BeautifulSoup(html_text, "lxml")


# print(soup)
def find_jobs():
    cards = soup.find_all("div", class_="jobsearch-SerpJobCard unifiedRow row result")
    for card in cards:
        date_published = card.find("div", class_="result-link-bar").span.text
        days_count = date_published.split(" ")
        print(days_count)
        job_title = card.find("h2")
        company_name = card.find("span", class_="company").text.strip()
        company_location = card.find("span", class_="location accessible-contrast-color-location").text.strip()
        salary = card.find("div", class_="salarySnippet holisticSalary")

        print(f"Job title: {job_title.a.text.strip()}")
        print(f"Company:   {company_name}")
        print(f"Location:  {company_location}")
        if salary is None:
            print("No salary detail")
        else:
            print(f"Salary: {salary.text.strip()}")
        print(f"Published data: {date_published}")

        print("")


if __name__ == "__main__":
    while True:
        find_jobs()
        time_to_sleep = 20
        print(f"Sleeping for {time_to_sleep} seconds...")
        print(time.time())
        time.sleep(time_to_sleep)
