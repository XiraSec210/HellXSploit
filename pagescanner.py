import requests
from bs4 import BeautifulSoup

url = input("Target: ")
req = requests.get(url)
html = req.text

soup = BeautifulSoup(html, 'lxml')
pages = set()

for link in soup.find_all('a'):
    pages.add(link.get('href'))

for link in pages:
    if link.startswith("/"):
        req = requests.get(url + link)
        if req.status_code == 200:
            pages.add(link)

for page in pages:
    print()
    print(url + "/" + page)