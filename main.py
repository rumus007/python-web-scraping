import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Nepal")
soup = bs4.BeautifulSoup(result.text, "lxml")
res = soup.select('.vector-toc-text')
texts = []

for items in res:
    texts.append(items.text)

print(texts)