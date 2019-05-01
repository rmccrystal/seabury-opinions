import datetime
import timeago

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
Base = declarative_base()


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, default=0)
    title = Column(VARCHAR(255), default='')
    comment = Column(TEXT(20000))
    time = Column(DateTime, default=datetime.datetime.utcnow)

    def get_relative_timestamp(self):
        now = datetime.datetime.now()
        return timeago.format(self.time, now)


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    score = Column(Integer, default=0)
    name = Column(VARCHAR(255))
    description = Column(TEXT(1000), default='')
