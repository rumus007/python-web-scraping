import requests
import bs4

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# res = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# products = soup.select('.product_pod')
# print(products[0].select('h3')[0].select('a')[0]['title'])

two_star = []
for i in range(1, 51):
    scrape_url = base_url.format(i)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if len(book.select(".star-rating.Two")) != 0:
            book_title = book.select('h3')[0].select('a')[0]['title']
            two_star.append(book_title)


print(two_star)