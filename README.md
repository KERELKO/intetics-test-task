# AI-Enabled Q&A Web Application

This is a full-stack web application that provides an AI-powered question-answering system with retrieval-augmented generation (RAG) capabilities. The application allows users to ask questions and receive AI-generated answers based on a knowledge base.

## Features

- Modern web interface for asking questions and viewing answers
- RESTful API endpoints for question handling
- Retrieval-augmented generation (RAG) using embeddings-based search
- OpenAI-powered response generation
- Question-answer history logging per user
- Automated testing suite

## Tech Stack

### Backend
- Python 3.12
- FastAPI for the REST API
- LangChain for AI/LLM integration
- OpenAI API for embeddings and completions
- Pydantic for data validation
- Uvicorn as ASGI server

### Frontend
- Vue.js
- Vite
### Dependencies
- fastapi >= 0.115.12
- langchain >= 0.3.25
- openai >= 1.82.1
- uvicorn >= 0.34.2
- python-dotenv >= 1.1.0
- aiofiles >= 24.1.0
- numpy >= 2.2.6
- aiocsv >= 1.3.2

## Setup Instructions

### Prerequisites
- Python 3.12 or higher
- Poetry for dependency management

### Installation

1. Clone the repository:
```bash
git clone https://github.com/KERELKO/intetics-test-task
cd intetics-test-task
```
2. Set up environment variables in /backend:
```bash
cd backend
cp .env.example .env
# Edit .env file with your OpenAI API key and other configurations
```

## Running the Application

1. Start the backend server with Docker compose in root folder:
```bash
docker compose up --build
```

The application will be available at:
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## API Endpoints

### POST /api/ask
Submit a question and receive an AI-generated answer using RAG.

Request body:
```json
{
    "question": "Your question here"
}
```

Response:
```json
{
    "content": "AI-generated answer"
}
```

### GET /api/history
Retrieve the history of questions and answers for a user.

Response:
```json
[
    {
        "question": "Previous question",
        "answer": "Previous answer"
    }
]
```

## Running Tests

Execute the test suite using:
```bash
poetry run pytest
```

## Project Structure

```
intetics-ai-enabled-app/
├── src/
│   └── app/
│       ├── api/
│       │   ├── handlers.py
│       │   └── schemas.py
│       ├── clients/
│       ├── services/
│       ├── storages/
│       ├── config.py
│       ├── di.py
│       ├── main.py
│       └── types.py
├── tests/
├── pyproject.toml
├── poetry.lock
├── Dockerfile
├── docker-compose.yaml
└── README.md
```

## Design Approach

### Retrieval Process
- Uses embedding-based similarity search for finding relevant context
- Converts questions into embeddings using OpenAI's embedding model
- Finds top-k most similar questions using cosine similarity
- Combines retrieved context with user question for enhanced responses

### AI Integration
- Utilizes OpenAI's API for both embeddings and chat completions
- Implements retrieval-augmented generation (RAG) for more accurate answers
- Uses LangChain for streamlined AI/LLM integration
- Structured prompt engineering with context injection

## Known Limitations and Future Improvements

1. **Knowledge Base**
   - Currently uses a simple storage system
   - Could be upgraded to a vector database for better similarity search performance

2. **AI Model**
   - Depends on OpenAI API
   - Could be enhanced with local model options or model fallbacks

3. **Scalability**
   - Basic implementation focused on functionality
   - Would need caching and optimization for production-scale usage

4. **Features**
   - Basic Q&A functionality implemented
   - Could add user authentication, rate limiting, and response streaming

## License

This project is licensed under the MIT License - see the LICENSE file for details.
