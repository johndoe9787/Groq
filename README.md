# GroqApp
- This is an application that takes input as prompt and sends a request via the Groq api and model qwen/qwen3-32b and prints out the response as text.

## Feature
- Groq(): creates a connection instance
- client.chat.completions.create(...): Sends your prompt to Groq's cloud servers. It specifies the AI model (qwen/qwen3-32b) and formats your prompt into a structured message history (role: user).Why it is used: It handles the netw

## How to run
-Run in terminal `groqApp.py`