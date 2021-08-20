import requests


def start_crawl(url):
    crawl = True
    page = 0

    while crawl:
        page += 40
        response = requests.get(url.format(page))

        print( bool(response.url == url.format(page)))

        print(response)


if __name__ == '__main__':
    target = 'https://www.digikala.com/samsung-brand/mobile-phone/?pageno={}&sortby=4'
    start_crawl(target)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
