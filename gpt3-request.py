import json

import openai

from config import *
from keys import OPENAI_API_KEY
from parser import parse_resume_str


def generate_resume_text():
    with open(GPT_REQUEST_FILE, 'r') as f:
        gpt_request = f.read()

    openai.api_key = OPENAI_API_KEY

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

    text = response["choices"][0]["text"]
    
    return text


def main():
    resume_text = generate_resume_text()
    resume_dict = parse_resume_str(resume_text)

    filename = 'resume.json'
    with open(filename, 'w') as f:
        json.dump(resume_dict, f, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    main()