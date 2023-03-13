import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
site_html = response.text
soup = BeautifulSoup(site_html, "html.parser")
movie_titles = soup.find_all(name="h3", class_="title")

movie_list_of_titles = [movie.getText() for movie in movie_titles]
movie_list_of_titles.reverse()
print(movie_list_of_titles)
with open("FileName.txt", "w") as file:
    for title in movie_list_of_titles:
        file.write(title+"\n")    
    