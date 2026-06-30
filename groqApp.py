from dotenv import load_dotenv
from groq import Groq

def get_input():
    return input("Enter a prompt: ")

prompt = get_input()
# Load environment variables from the .env file
load_dotenv()

# The client will now automatically find GROQ_API_KEY from your .env
client = Groq()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    model="qwen/qwen3-32b",
)



print(chat_completion.choices[0].message.content)
