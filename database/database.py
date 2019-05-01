from typing import List
from database.datatypes import *
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker


engine = db.create_engine('mysql://db:pass420@db:3306/db', echo=True)
conn = engine.connect()
meta = db.MetaData()
meta.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def get_comment_list(teacher_id: int = 0) -> List[Comment]:
    return session.query(Comment).filter(Comment.teacher_id == teacher_id)


def add_comment_data(title: str, comment: str, teacher_id=0) -> bool:
    add_comment(Comment(title=title, comment=comment, teacher_id=teacher_id))


def add_comment(comment: Comment) -> None:
    session.add(comment)
    session.commit()


def get_teacher_list() -> List[Teacher]:
    return session.query(Teacher).all()


def get_teacher_by_id(teacher_id: int) -> Teacher:
    result = session.query(Teacher).get(teacher_id)
    if not result:
        return None
    else:
        return result


def add_teacher(teacher: Teacher) -> None:
    session.add(teacher)
    session.commit()
