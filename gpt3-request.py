import re

import openai


from config import *
from keys import OPENAI_API_KEY


'''openai.api_key = OPENAI_API_KEY

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

print()

text = response["choices"][0]["text"]
'''
text = "John Anderson\nJob Title:Software Engineer\nSummary:I have been a software engineer for the last 10 years. I have been working primarily in Java and .NET, with a little bit of python and javascript on the side. In the last year, I have been involved with a React / Redux application that is a PWA.\nCompany #1 Name:Community Foods\nCompany #1 Role:Front End Engineer\nCompany #1 Summary:Community Foods is a family-owned grocery store that has been a staple in the Northern Virginia community for over 50 years. I helped build a new, single page SPA that is react, react-router, redux, webpack, node, mongodb, docker, and isomorphic.\nCompany #1 Highlight 1:Built a very large and complex React / Redux application. It works on all platforms and has IOS/Android builds due to it being a PWA. (wrapped it in React Native though only implementing a WebView)\nCompany #1 Highlight 2:Hosted on a mixture of Heroku Apps and EC2 servers.\nCompany #2 Name:Spartan Cycles\nCompany #2 Role:Senior Software Engineer\nCompany #2 Summary:I was responsible for maintaining and extending the PHP based e-commerce web site that is responsible for managing millions of dollars of online retail bicycle sales.\nCompany #2 Highlight 1:Increased the capacity of the e-commerce website by 40% without any downtime by rewriting the shopping cart to use SQL instead of the previously used MongoDB\nCompany #2 Highlight 2:Migrated the website to microservices using NGINX for load balancing, Service Discovery, and Envoy Proxy\nPersonal Reference:John is an outstanding engineer who has always gone above and beyond to complete his work. He has demonstrated excellent skills with both front end and back end development, as well as helping out on some of the infrastructure projects I have given him. He is very good at taking complex problems and breaking them down into manageable pieces.\nInterests: Travel. Soccer.\n"
deliverable = {
  "basics": {
    "name": re.search('^([\w\s]+)\n', text).group(1),
    "label": re.search('Job Title:([\w\s]+)\n', text).group(1),
    "summary": re.search('Summary:(.+)\n', text).group(1)
  },
  "work": [{
    
  }]
}

print(deliverable)