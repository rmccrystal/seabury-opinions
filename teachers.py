from typing import List
import operator
import random


class Teacher:
    name: str
    score: int
    description: str

    def __init__(self, name: str, description: str="", score: int=0) -> None:
        self.name = name
        self.score = score
        self.description = description


_teachers = list()


def _add_teacher(teacher: Teacher) -> None:
    _teachers.append(teacher)


def add_teacher(name: str, description: str="", score: int=0):
    _add_teacher(Teacher(name, description, score))


def get_teachers() -> List[Teacher]:
    return sorted(_teachers, key=operator.attrgetter('score'))[::-1]


def _init_teacher_list() -> None:
    for line in """Karmen Brown
Chesa Cipro
Alastair Hebard
Penny Holmes
Emily Lorusso
Lenda McGehee
Kay McLeod
Sally Sefton-Johnston
Joseph Stafford
Kukini Suwa
Emerson Timmins
Jon Toda
Chrissie Tramontin
Stephanie Walsh
Sean Wilson""".splitlines():
        add_teacher(line, score=random.randint(-4,4), description=str(random.randint(100000000000, 99999999999999)))
