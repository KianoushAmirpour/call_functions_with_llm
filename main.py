import ollama
from utils import build_prompt

query = "Which five products show the greatest absolute variance between their popularity index and return rate?"

prompt = build_prompt(query)

response = ollama.chat(
    model="nexusraven:13b-q3_K_S",
    messages=[{"role": "user", "content": prompt, }],
    stream=False,
)
print(response.message.content)
