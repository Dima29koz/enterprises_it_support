import requests
from bs4 import BeautifulSoup

from server.app.utils.news_parser.news_item import NewsItem


def load_content_url(url: str):
    r = requests.get(url, stream=True)
    bs_content = BeautifulSoup(r.text, features="xml")
    return bs_content


def get_news_items(bs_content: BeautifulSoup):
    items = bs_content.findAll('item')
    for item in items:
        yield NewsItem(
            title=item.title.text,
            link=item.link.text,
            pub_date=item.pubDate.text,
            sub_rubrics=', '.join([subj.text for subj in item.find_all('subject')]),
            tags=item.tags.text if item.tags else '',
            description=item.description.text,
            guid=item.guid.text,
            img_url=item.enclosure['url'] if item.enclosure else '',
        )


def get_news(url: str):
    return get_news_items(load_content_url(url))


if __name__ == '__main__':
    print(next(get_news('https://1prime.ru/export/rss2/index.xml')))
