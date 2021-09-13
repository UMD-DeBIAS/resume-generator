import openai

from config import *
from keys import OPENAI_API_KEY


openai.api_key = OPENAI_API_KEY

with open(GPT_REQUEST_FILE, 'r') as f:
    gpt_request = f.read()

response = openai.Completion.create(
  engine="davinci",
  prompt=gpt_request,
  temperature=0.8,
  max_tokens=896,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["====="]
)

print(response)
