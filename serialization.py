import json
from comments import Comment
import datetime
from teachers import Teacher


# ########################  TIME  ######################
def serialize_time(time: datetime.datetime) -> str:
    return json.dumps(time, indent=4, sort_keys=True, default=str)


def deserialize_time(time: str) -> datetime.datetime:
    return datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')


# ######################  COMMENTS ######################
def serialize_comment(comment: Comment) -> str:
    return json.dumps([comment.title, comment.comment, serialize_time(comment.time)])


def deserialize_comment(comment: str) -> Comment:
    json_data = json.loads(comment)
    return Comment(json_data.title, json_data.comment, deserialize_time(json_data.time))


# #######################  TEACHERS  ###################
def serialize_teacher(teacher: Teacher) -> str:
    return json.dumps([teacher.name, teacher.description, teacher.score, teacher.id])


def deserialize_teacher(teacher: str) -> Teacher:
    json_data = json.loads(teacher)
    return Teacher(json_data.name, json_data.description, json_data.score, json_data.id)
