from fastapi import APIRouter
from openai.types.chat.chat_completion_user_message_param import ChatCompletionUserMessageParam

from app.di import AIClientDep, StorageDep, EmbeddingServiceDep
from app.types import QuestionAnswer

from .schemas import AIResponseSchema, AskAISchema, QuestionAnswerSchema

router = APIRouter()


@router.post('/ask')
async def ask_ai_handler(
    ai_client: AIClientDep,
    storage: StorageDep,
    embedding_service: EmbeddingServiceDep,
    ask_question: AskAISchema,
    user_id: int
):
    faq = await storage.read_entries()

    embbeding_list = embedding_service.build_embedding_list(faq)

    query_embedding = embedding_service.query_embedding(ask_question.question)

    similar_result_indices = embedding_service.find_top_k_indices(query_embedding, embbeding_list)
    similar_results = '\n\n'.join(faq[i]['answer'] for i in similar_result_indices)

    context = (
        'Use the following context to answer the question.\n\n'
        f'Context:\n{similar_results}\n\n'
        f'Question:\n{ask_question.question}'
    )
    response = await ai_client.make_request([
        ChatCompletionUserMessageParam(content=ask_question.question, role='user'),
        ChatCompletionUserMessageParam(content=context, role='user')
    ])

    await storage.save_entry(
        QuestionAnswer(question=ask_question.question, answer=response, user_id=user_id)
    )
    return AIResponseSchema(content=response)


@router.get('/history')
async def get_history_handler(
    storage: StorageDep,
    user_id: int,
) -> list[QuestionAnswerSchema]:
    user_qa_list = await storage.get_entries_by_user(user_id)
    return [
        QuestionAnswerSchema(question=qa['question'], answer=qa['answer']) for qa in user_qa_list
    ]
