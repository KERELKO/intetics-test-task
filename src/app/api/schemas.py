from pydantic import BaseModel


class AskAISchema(BaseModel):
    question: str


class AIResponseSchema(BaseModel):
    content: str


class QuestionAnswerSchema(BaseModel):
    question: str
    answer: str
