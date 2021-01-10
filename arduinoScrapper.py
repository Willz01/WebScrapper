from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://create.arduino.cc/projecthub?difficulty=intermediate&sort=trending").text
soup = BeautifulSoup(html_text, "lxml")


class Project:
    def __init__(self, title, owner, views, comments, respects):
        self.title = title
        self.owner = owner
        self.views = views
        self.comments = comments
        self.respects = respects

    def toString(self):
        print(
            f'''Project Title: {self.title} \nProject owner: {self.owner} \nViews: {self.views} \nComments: {self.comments} \nRespects: {self.respects} ''')


# print(soup)
file = open("ArduinoInfo.txt", "w")
cards = soup.find_all("div",
                      class_="thumb-inner")
for title in cards:
    projectTitle = title.h4.text
    projectOwner = title.find("span", class_="user-name").text
    # index 0: views, index 1: comments and index 2: respect
    stats = title.find_all("span", class_="stat-figure")
    file.write(projectTitle + "\n")
    project = Project(projectTitle, projectOwner, stats[0].text, stats[1].text, stats[2].text)
    project.toString()
    # print(
    #     f'''Project Title: {projectTitle} \nProject owner: {projectOwner} \nViews: {stats[0].text} \nComments: {stats[1].text} \nRespects: {stats[2].text} ''')
