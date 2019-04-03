import pygsheets
from Tools.scripts import db2pickle
from typing import List
from comments import Comment

gc = pygsheets.authorize()

class CommentsDatabase:
    def __init__(self,):
        self.db = gc.open('comments').sheet1

    def _get_lowest_empty_row(self) -> int:
        for i in range(0, self.db.rows):
            if self._row_is_empty():
                return i
        print("You shouldn't be here; can't find an empty row")
        return 1    # In case it can't find any, return the first row (should be the oldest)

    def _row_is_empty(self, row: int):
        return self.db.get_value((row, 1)) == ""

    def _get_comment_from_row(self) -> Comment:
        pass

    def _insert_comment(self, comment: Comment, row: int) -> None:
        self.db.update_value((row, 1), comment.title)
        self.db.update_value((row, 2), comment.comment)
        self.db.update_value((row, 3), comment.time)

    def get_comments_list(self) -> List[Comment]:
        comments = list()
        for record in self.db.get_all_records():
            comments.append(Comment(record['title'], record['comment'], record['time']))
        return comments

    def add_comment(self, comment: Comment) -> None:
        self._insert_comment(comment, self._get_lowest_empty_row())
