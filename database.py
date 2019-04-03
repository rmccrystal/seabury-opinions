import pygsheets
from typing import List
from comments import Comment
import datetime
import json


gc = pygsheets.authorize()


def serialize_time(time: datetime.datetime) -> str:
    return json.dumps(time, indent=4, sort_keys=True, default=str)


def deserialize_time(time: str) -> datetime.datetime:
    return datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')


class CommentsDatabase:         #TODO: Make it queue comments and keep a local database to remove delays.
    def __init__(self):
        self.db = gc.open('comments').sheet1

    def _get_lowest_empty_row(self) -> int:
        for i in range(1, self.db.rows):
            if self._row_is_empty(i):
                return i
        print("You shouldn't be here; can't find an empty row")
        return 1    # In case it can't find any, return the first row (should be the oldest)

    def _row_is_empty(self, row: int):
        return self.db.get_value((row, 1)) == ""

    def _insert_comment(self, comment: Comment, row: int) -> None:
        self.db.update_value((row, 1), comment.title)
        self.db.update_value((row, 2), comment.comment)
        self.db.update_value((row, 3), str(comment.time))

    def get_comments_list(self) -> List[Comment]:
        comments = list()
        for record in self.db.get_all_records():
            comments.append(Comment(record['title'], record['comment'], deserialize_time(record['time'])))
        return comments

    def add_comment(self, comment: Comment) -> None:
        self._insert_comment(comment, self._get_lowest_empty_row())
