from typing import *
import collections
from jinja2 import utils
import datetime
import timeago


class Comment:
    title: str
    comment: str
    time: datetime.datetime

    def __init__(self, title: str, comment: str, time: int=None) -> None:
        self.title = utils.escape(title)[:100]
        self.comment = utils.escape(comment)[:2000]
        if not time:
            self.time = datetime.datetime.now()
        else:
            self.time = datetime.datetime(second=time)

    def get_title(self) -> str:
        return self.title

    def get_comment(self) -> str:
        return self.comment

    def get_timestamp(self) -> str:
        return timeago.format(self.time, datetime.datetime.now())


_comments = list()


def get_comments() -> List[Comment]:
    return _comments


def _add_comment(comment: Comment) -> None:
    _comments.append(comment)


def add_comment(comment_title: str, comment: str) -> None:
    _add_comment(Comment(comment_title, comment))

