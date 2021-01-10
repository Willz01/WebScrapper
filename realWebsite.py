from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://schema.hkr.se/setup/jsp/Schema.jsp?startDatum=today&intervallTyp=m&intervallAntal=6"
                         "&sprak=EN&sokMedAND=true&forklaringar=true&resurser=p.TBSE1+2019+36+100+NML+en").text

soup = BeautifulSoup(html_text, "lxml")
lines = soup.find_all("tr", class_="data-white")
for line in lines:
    time = line.find("nobr").text
    course_title = line.find("a").text
    day = line.find("td", class_="commonCell data").text
    print(course_title)
    print(time)
    print(day)
