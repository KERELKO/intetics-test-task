from fastapi import APIRouter

from app.di import AIClientDep, StorageDep

from .schemas import AIResponseSchema, AskAISchema

router = APIRouter()


@router.post('/ask')
async def ask_ai_handler(
    ai_client: AIClientDep,
    storage: StorageDep,
    ask_question: AskAISchema,
):
    faq = await storage.read_entries()
    print(faq)
    response = await ai_client.make_request(ask_question.question)
    await storage.save_entry(ask_question.question, answer=response)
    return AIResponseSchema(content=response)
