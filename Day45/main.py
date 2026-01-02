from bs4 import BeautifulSoup
import requests

#----------------------------------------------------------------------------
# PART 3
#----------------------------------------------------------------------------
EMPIRE_ENDPOINT = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=EMPIRE_ENDPOINT)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")

title_tags = soup.find_all(name="h3", class_="title")

movie_titles = [tag.getText() for tag in title_tags]

movie_titels_in_order = movie_titles[::-1]

with open(file="Top100Movies.txt", mode="w", encoding="utf-8") as f:
    for movie_title in movie_titels_in_order:
        f.write(f"{movie_title}\n")


















#----------------------------------------------------------------------------
# PART 2
#----------------------------------------------------------------------------
# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text

# soup = BeautifulSoup(yc_web_page, "html.parser")
# articles = soup.find_all(name="span", class_="titleline")
# article_texts = []
# article_links = []
# for article in articles:
#     article_tag = article.find(name="a")
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_links.append(link)

# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# # print(article_texts)
# # print(article_links)
# # print(article_upvotes)

# largest_upvote_count = max(article_upvotes)
# largest_upvote_index = article_upvotes.index(largest_upvote_count)

# print(article_texts[largest_upvote_index])
# print(article_links[largest_upvote_index])
# print(article_upvotes[largest_upvote_index])





#----------------------------------------------------------------------------
# PART 1
#----------------------------------------------------------------------------

# with open(file="website.html", mode='r') as f:
#     contents = f.read()

# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)