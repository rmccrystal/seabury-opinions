from typing import List


class Teacher:
    name: str
    score: int

    def __init__(self, name: str, score: int=0) -> None:
        self.name = name
        self.score = score


_teachers = list()


def _add_teacher(teacher: Teacher) -> None:
    _teachers.append(teacher)


def add_teacher(name: str, score: int=0):
    _add_teacher(Teacher(name, score))


def get_teachers() -> List[Teacher]:
    return _teachers


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
        add_teacher(line)
