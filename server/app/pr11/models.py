from datetime import datetime

from sqlalchemy import func

from server.app import db


class NewsDBItem(db.Model):
    def __init__(self, title: str, link: str, pub_date: str,
                 sub_rubrics: str, tags: str, description: str,
                 guid: str, img_url: str):
        self.title = title
        self.link = link
        self.pub_date = convert_date(pub_date)
        self.sub_rubrics = sub_rubrics
        self.tags = tags
        self.description = description
        self.guid = guid
        self.img_url = img_url

    __tablename__ = 'news'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(256))
    link = db.Column(db.String(256))
    pub_date = db.Column(db.DateTime())
    sub_rubrics = db.Column(db.String(256))
    tags = db.Column(db.String(256))
    description = db.Column(db.Text(256))
    guid = db.Column(db.String(256))
    img_url = db.Column(db.String(256))

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            link=self.link,
            pub_date=self.pub_date.isoformat(),
            sub_rubrics=self.sub_rubrics,
            tags=self.tags,
            description=self.description,
            guid=self.guid,
            img_url=self.img_url,
        )

    def __repr__(self):
        return str(self.id)


def get_news_by_link(link: str) -> NewsDBItem | None:
    return NewsDBItem.query.filter_by(link=link).first()


def get_news_min_date() -> datetime | None:
    min_date_item = db.session.query(func.min(NewsDBItem.pub_date)).first()
    if min_date_item:
        return min_date_item[0]


def get_news_max_date() -> datetime | None:
    max_date_item = db.session.query(func.max(NewsDBItem.pub_date)).first()
    if max_date_item:
        return max_date_item[0]


def get_news_date_range(start_date, end_date):
    return NewsDBItem.query.filter(NewsDBItem.pub_date.between(start_date, end_date)).all()


def convert_date(date: str):
    date_format = '%a, %d %b %Y %X %z'
    return datetime.strptime(date, date_format)
