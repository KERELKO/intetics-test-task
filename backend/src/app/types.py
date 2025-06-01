from typing import TypedDict


class QuestionAnswer(TypedDict, total=True):
    question: str
    answer: str
    user_id: int
