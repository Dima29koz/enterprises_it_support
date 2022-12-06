from dataclasses import dataclass


@dataclass
class NewsItem:
    title: str
    link: str
    pub_date: str
    sub_rubrics: str
    tags: str
    description: str
    guid: str
    img_url: str

    def __repr__(self):
        return f"title: {self.title}\n" \
               f"link: {self.link}\n" \
               f"pub_date: {self.pub_date}\n" \
               f"sub_rubrics: {self.sub_rubrics}\n" \
               f"tags: {self.tags}\n" \
               f"description: {self.description}\n" \
               f"guid: {self.guid}\n" \
               f"img_url: {self.img_url}\n"
