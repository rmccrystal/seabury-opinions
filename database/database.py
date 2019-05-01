from typing import List
from database.datatypes import *
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker


engine = db.create_engine('mysql://db:password@db:3306/db', echo=True)
conn = engine.connect()
meta = db.MetaData()
meta.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def get_comment_list() -> List[Comment]:
    return session.query(Comment).all()


def add_comment_data(title: str, comment: str) -> bool:
    add_comment(Comment(title=title, comment=comment))


def add_comment(comment: Comment) -> None:
    session.add(comment)
    session.commit()


def get_teacher_list() -> List[Teacher]:
    return session.query(Teacher).all()


def add_teacher(teacher: Teacher) -> None:
    session.add(teacher)
    session.commit()
