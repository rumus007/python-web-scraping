import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Nepal")
soup = bs4.BeautifulSoup(result.text, "lxml")
res = soup.select('.vector-toc-text')
texts = []

for items in res:
    texts.append(items.text)

# print(texts)

img = soup.find(title="Flag of Nepal").contents
imgsrc = img[0]['src']

imglink = requests.get("https:" + imgsrc)
f = open('flag_of_nepal.png', 'wb')
f.write(imglink.content)
f.close()


