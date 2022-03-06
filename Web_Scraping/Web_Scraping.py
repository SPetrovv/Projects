from bs4 import BeautifulSoup
import requests
import os

entities = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

url = 'https://www.bbc.com/news/world'
main_url = 'https://www.bbc.com'

response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

div = soup.find('div', {"id": "index-page"})
for anchor in div.find_all('a', href=True):
    hyperlink = f"{main_url}{anchor['href']}"
    if hyperlink not in entities:
        entities.append(hyperlink)

new_folder = "News"
if not os.path.exists(new_folder):
    os.makedirs(new_folder)
os.chdir(new_folder)
f = open('links.txt', 'w')
for i in entities:
    f.write(f'{i}\n')
