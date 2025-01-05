# we are going to write a program that will extract a list of new list questions in stackoverflow
# we refer to this kind of program as a web crawler or a web spider.

# the first step is install the beautifulsoup4, this is a very popular package for extracting from API, from html and xml files.
# the second step is to download the webpage that countins the newest questions, so let's import the request module.

import requests
from bs4 import BeautifulSoup

respons = requests.get("https://stackoverflow.com/questions")
respons_text = respons.text
soup = BeautifulSoup(respons_text, "html.parser")
list_questions = soup.select(".s-post-summary") # we type . to specify a class
for question in list_questions:
    print(question.select_one(".s-link").getText())
    print(question.select_one(".s-post-summary--stats-item-number").get_text())