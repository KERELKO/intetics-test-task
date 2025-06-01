from openai import AsyncOpenAI
from openai.types.chat.chat_completion_system_message_param import \
    ChatCompletionSystemMessageParam
from openai.types.chat.chat_completion_user_message_param import \
    ChatCompletionUserMessageParam

DEEPSEEK_CHAT_MODEL = 'deepseek-chat'
OPENAI_MODEL = 'gpt-4.1-nano'
DEEPSEEK_BASE_URL = 'https://api.deepseek.com'


class DeepSeek:
    """
    A wrapper class for interacting with the DeepSeek chat model via OpenAI-compatible API.
    """

    def __init__(self, api_key: str) -> None:
        self.client = AsyncOpenAI(api_key=api_key, base_url=DEEPSEEK_BASE_URL)

    async def make_request(
        self, messages: list[ChatCompletionSystemMessageParam | ChatCompletionUserMessageParam],
    ) -> str:
        """
        Send a list of messages to the DeepSeek chat model and get a response.

        Args:
            messages (list): A list of chat messages (system/user) to send to the model.

        Returns:
            str: The model's response message content.
        """
        response = await self.client.chat.completions.create(
            messages=messages,
            model=DEEPSEEK_CHAT_MODEL,
            stream=False,
        )
        return response.choices[0].message.content  # type: ignore


class ChatGPT:
    """
    A wrapper class for interacting with OpenAI's GPT chat model asynchronously.
    """

    def __init__(self, api_key: str | None = None) -> None:
        self.client = AsyncOpenAI(api_key=api_key or None)

    async def make_request(
        self, messages: list[ChatCompletionSystemMessageParam | ChatCompletionUserMessageParam],
    ) -> str:
        """
        Send a list of messages to the OpenAI chat model and get a response.

        Args:
            messages (list): A list of chat messages (system/user) to send to the model.

        Returns:
            str: The model's response message content.
        """
        response = await self.client.chat.completions.create(
            messages=messages,
            model=OPENAI_MODEL,
            stream=False,
        )
        return response.choices[0].message.content  # type: ignore
