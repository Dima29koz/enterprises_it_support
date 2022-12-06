from server import config
from server.app import create_app, db
from server.app.pr11.models import NewsDBItem, get_news_by_link
from server.app.utils.news_parser.parser import get_news

app = create_app(config.DevelopmentConfig)


def add_news(url: str):
    for item in get_news(url):
        if not get_news_by_link(item.link):
            db.session.add(NewsDBItem(
                item.title,
                item.link,
                item.pub_date,
                item.sub_rubrics,
                item.tags,
                item.description,
                item.guid,
                item.img_url
            ))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        add_news('https://1prime.ru/export/rss2/index.xml')
        db.session.commit()
