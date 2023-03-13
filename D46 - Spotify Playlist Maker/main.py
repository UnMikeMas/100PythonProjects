from bs4 import BeautifulSoup
import requests

user_date = input("What date you want to create a playlist with? Type your date in the YYYY-MM-DD format: ")
# First part (Billboard)
URL = f"https://www.billboard.com/charts/hot-100/{user_date}"
response = requests.get(URL)
billboard_html = response.text
soup = BeautifulSoup(billboard_html, "html.parser")
song_titles = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
list_of_titles = [title.getText().strip() for title in song_titles]

# Second Part (Spotify)