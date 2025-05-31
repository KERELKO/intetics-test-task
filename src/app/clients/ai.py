from openai import AsyncOpenAI
from openai.types.chat.chat_completion_system_message_param import \
    ChatCompletionSystemMessageParam
from openai.types.chat.chat_completion_user_message_param import \
    ChatCompletionUserMessageParam

DEEPSEEK_CHAT_MODEL = 'deepseek-chat'
OPENAI_MODEL = 'gpt-4.1-nano'
DEEPSEEK_BASE_URL = 'https://api.deepseek.com'


class DeepSeek:
    def __init__(self, api_key: str) -> None:
        self.client = AsyncOpenAI(api_key=api_key, base_url=DEEPSEEK_BASE_URL)

    async def make_request(
        self, messages: list[ChatCompletionSystemMessageParam | ChatCompletionUserMessageParam],
    ) -> str:
        response = await self.client.chat.completions.create(
            messages=messages,
            model=DEEPSEEK_CHAT_MODEL,
            stream=False,
        )
        return response.choices[0].message.content  # type: ignore


class ChatGPT:
    def __init__(self, api_key: str | None = None) -> None:
        self.client = AsyncOpenAI(api_key=api_key or None)

    async def make_request(
        self, messages: list[ChatCompletionSystemMessageParam | ChatCompletionUserMessageParam],
    ) -> str:
        response = await self.client.chat.completions.create(
            messages=messages,
            model=OPENAI_MODEL,
            stream=False,
        )
        return response.choices[0].message.content  # type: ignore
