from openai import AsyncOpenAI
from openai.types.chat.chat_completion_system_message_param import \
    ChatCompletionSystemMessageParam
from openai.types.chat.chat_completion_user_message_param import \
    ChatCompletionUserMessageParam

DEEPSEEK_CHAT_MODEL = 'deepseek-chat'
DEEPSEEK_BASE_URL = 'https://api.deepseek.com'


class DeepSeek:
    def __init__(self, api_key: str) -> None:
        self.client = AsyncOpenAI(api_key=api_key, base_url=DEEPSEEK_BASE_URL)

    async def make_request(self, text: str) -> str:
        response = await self.client.chat.completions.create(
            messages=[
                ChatCompletionSystemMessageParam(
                    role='system', content=text,
                ),
                ChatCompletionUserMessageParam(role='user', content=text),
            ],
            model=DEEPSEEK_CHAT_MODEL,
            stream=False,
        )
        return response.choices[0].message.content  # type: ignore
