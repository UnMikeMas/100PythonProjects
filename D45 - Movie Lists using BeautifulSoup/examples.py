from bs4 import BeautifulSoup
import requests

# with open('website.html', encoding="utf-8") as file:
#     contents=file.read()
# soup = BeautifulSoup(contents, "html.parser")
# ## Example ##
# print(soup.title.string)

# ##Printing the whole code##
# # print(soup.prettify())

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
# #     print(tag.getText())
# #     print(tag.get("href"))
    
# # heading = soup.find(name="h1", id="name")
# # section_heading = soup.find(name="h1", class_="heading")
# company_url = soup.select_one(selector="p a")

## Scrapping a live website##
all_scores = []
all_titles = []
all_links = []
response = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(response.text, "html.parser")
news = soup.find_all(class_="titleline")
for heading in news:
    all_links.append(heading.find(name="a").get("href"))
    all_titles.append(heading.find(name="a").getText())
scores = soup.find_all(class_="score")
for score in scores:
    all_scores.append(int(score.getText().split(" ")[0]))
    
# print(all_scores)
# print(all_titles)
# print(all_links)

max_votes_index = all_scores.index(max(all_scores))
print(all_links[max_votes_index])
print(all_scores[max_votes_index])
print(all_titles[max_votes_index])