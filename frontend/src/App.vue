<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const question = ref('');
    const answer = ref('');
    const loading = ref(false);
    const error = ref('');
    // Using a default user_id for demonstration
    const USER_ID = 1;

    const askQuestion = async () => {
      if (!question.value.trim() || loading.value) return;
      
      loading.value = true;
      error.value = '';
      
      try {
        const response = await axios.post(`http://localhost:8000/api/ask?user_id=${USER_ID}`, {
          question: question.value
        });
        answer.value = response.data.content;
        question.value = '';
      } catch (err) {
        error.value = 'Failed to get an answer. Please try again.';
        console.error('Error:', err);
      } finally {
        loading.value = false;
      }
    };

    return {
      question,
      answer,
      loading,
      error,
      askQuestion
    };
  }
};
</script>

<template>
  <div class="app">
    <div class="chat-container">
      <div class="header">
        <h1>AI Assistant</h1>
        <p class="subtitle">Ask me anything!</p>
      </div>

      <div class="chat-box" :class="{ 'has-answer': answer }">
        <div v-if="answer" class="answer-bubble">
          <p>{{ answer }}</p>
        </div>
      </div>

      <div class="input-container">
        <div class="error-message" v-if="error">{{ error }}</div>
        <div class="input-group">
          <textarea
            v-model="question"
            placeholder="Type your question here..."
            :disabled="loading"
            @keyup.enter="askQuestion"
          ></textarea>
          <button 
            @click="askQuestion" 
            :disabled="loading || !question.trim()"
            :class="{ 'loading': loading }"
          >
            <span v-if="!loading">Ask</span>
            <span v-else>...</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  overflow: hidden;
}

.app {
  min-height: 100vh;
  height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  overflow: hidden;
}

.chat-container {
  width: 100%;
  max-width: 1200px;
  min-width: 800px;
  height: 80vh;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.header {
  padding: 30px;
  text-align: center;
  background: white;
  border-bottom: 1px solid #eee;
  flex-shrink: 0;
}

.header h1 {
  color: #2d3748;
  font-size: 2.5em;
  margin-bottom: 5px;
}

.subtitle {
  color: #718096;
  font-size: 1.2em;
}

.chat-box {
  padding: 40px;
  flex: 1;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  scrollbar-width: none; /* Firefox */
  -ms-overflow-style: none; /* IE and Edge */
}

.chat-box::-webkit-scrollbar {
  display: none; /* Chrome, Safari, Opera */
}

.answer-bubble {
  background: #667eea;
  color: white;
  padding: 25px;
  border-radius: 15px;
  margin-bottom: 20px;
  animation: fadeIn 0.5s ease-out;
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2);
  max-width: 80%;
}

.answer-bubble p {
  line-height: 1.6;
  font-size: 1.2em;
}

.input-container {
  padding: 30px;
  background: white;
  border-top: 1px solid #eee;
  flex-shrink: 0;
}

.input-group {
  display: flex;
  gap: 20px;
  max-width: 100%;
}

textarea {
  flex: 1;
  padding: 20px;
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  font-size: 1.1em;
  resize: none;
  height: 80px;
  transition: border-color 0.3s ease;
  overflow: auto;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

textarea::-webkit-scrollbar {
  display: none;
}

textarea:focus {
  outline: none;
  border-color: #667eea;
}

button {
  padding: 0 40px;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 1.1em;
  cursor: pointer;
  transition: all 0.3s ease;
  min-width: 120px;
  flex-shrink: 0;
}

button:hover:not(:disabled) {
  background: #5a6fe4;
  transform: translateY(-1px);
}

button:disabled {
  background: #a0aec0;
  cursor: not-allowed;
}

button.loading {
  animation: pulse 1.5s infinite;
}

.error-message {
  color: #e53e3e;
  margin-bottom: 15px;
  text-align: center;
  font-size: 1em;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pulse {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 0.7;
  }
  100% {
    opacity: 1;
  }
}

/* Only apply mobile styles for very small screens */
@media (max-width: 840px) {
  .app {
    padding: 0;
  }
  
  .chat-container {
    min-width: unset;
    height: 100vh;
    border-radius: 0;
  }
  
  .input-group {
    flex-direction: column;
  }
  
  button {
    height: 50px;
  }
}
</style>
