from requests import get
from bs4 import BeautifulSoup as bs

url = 'https://www.instagram.com/cristiano/'

reponse = requests.get(url)
soup = bs(reponse.text)

print(soup)
