from fastapi import APIRouter
from openai.types.chat.chat_completion_user_message_param import ChatCompletionUserMessageParam

from app.di import AIClientDep, StorageDep, EmbeddingServiceDep
from app.types import QuestionAnswer

from .schemas import AIResponseSchema, AskAISchema

router = APIRouter()


@router.post('/ask')
async def ask_ai_handler(
    ai_client: AIClientDep,
    storage: StorageDep,
    embedding_service: EmbeddingServiceDep,
    ask_question: AskAISchema,
):
    faq = await storage.read_entries()
    embbeding_list = embedding_service.build_embedding_list(faq)
    query_embedding = embedding_service.query_embedding(ask_question.question)
    similar_result_indices = embedding_service.find_top_k_indices(query_embedding, embbeding_list)
    print(f'similar_result_indices: {similar_result_indices}')
    similar_results = '\n\n'.join(faq[i]['answer'] for i in similar_result_indices)
    print(f'similar_result: {similar_results}')
    context = (
        'Use the following context to answer the question.\n\n'
        f'Context:\n{similar_results}\n\n'
        f'Question:\n{ask_question.question}'
    )
    response = await ai_client.make_request([
        ChatCompletionUserMessageParam(content=ask_question.question, role='user'),
        ChatCompletionUserMessageParam(content=context, role='user')
    ])
    await storage.save_entry(QuestionAnswer(question=ask_question.question, answer=response))
    return AIResponseSchema(content=response)
