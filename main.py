from bs4 import BeautifulSoup

with open("index.html", "r") as file:
    content = file.read()

soup = BeautifulSoup(content, "lxml")
# print(soup.prettify())
# finds the first h5 tag and returns
tag = soup.find("h5")
print(tag.get_text())

course_html_tags = soup.find_all("h5")
for course in course_html_tags:
    print(course.text)

print("****cards********")
# finds all div tags and filters out all with class card
course_cards = soup.find_all("div", class_="card")
for card in course_cards:
    course_name = card.h5.text
    course_price = card.a.text.split()[-1]
    print(f"Course: {course_name} , Price: {course_price}")
print("****Cards descriptions*******")
course_description = soup.find_all("p")
for description in course_description:
    descrip = description.text
    print(descrip)
