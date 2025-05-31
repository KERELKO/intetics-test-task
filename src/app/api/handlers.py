from fastapi import APIRouter

from app.di import AIClientDep

from .schemas import AIResponseSchema, AskAISchema

router = APIRouter()


@router.post('/ask')
async def ask_ai_handler(
    ai_client: AIClientDep,
    ask_question: AskAISchema,
):
    response = await ai_client.make_request(ask_question.question)
    return AIResponseSchema(content=response)
