import httpx
import pytest

BASE_API_URL = 'http://localhost:8000/api'


@pytest.mark.asyncio
async def test_can_make_successful_request_to_api():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=f'{BASE_API_URL}/ask', params={'user_id': 1}, json={'question': 'Hello!'}
        )
        assert response.is_success
        data = response.json()
        assert 'content' in data
        assert isinstance(data['content'], str)
