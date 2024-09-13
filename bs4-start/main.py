from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
span_tag_title = soup.find_all("span", class_="titleline")
span_tag_score = soup.find_all("span", class_="score")
article_text = []
article_link = []

for tag in span_tag_title:
    anchor_tag = tag.find("a")
    article_text.append(anchor_tag.getText())
    article_link.append(anchor_tag.get("href"))

article_upvotes = [int(subtag.getText().split()[0]) for subtag in span_tag_score]

print(article_text)
print(article_link)
print(article_upvotes)

max_upvotes_index = article_upvotes.index(max(article_upvotes))
max_article_text = article_text[max_upvotes_index]
max_article_link = article_link[max_upvotes_index]
print(max_article_text, max_article_link, max(article_upvotes))











# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     tag.get("href")
#
# # heading = soup.find(name="h1", id="name")
#
# h3_heading = soup.find_all("h3", class_="heading")
# print(h3_heading)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# heading = soup.select(".heading")
# print(heading)

