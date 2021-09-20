import re

import openai


from config import *
from keys import OPENAI_API_KEY

def get_interests(interests_txt):


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

print(response)'''
response = {
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": None,
      "text": "Robbie Berglund\nJob Title:Solutions Architect\nSummary:I am a solutions architect skilled at architecting and implementing complex enterprise software systems and at building and managing teams.\nCompany #1 Name:Resonate\nCompany #1 Role:Co-Founder, CTO\nCompany #1 Summary:Resonate developed a SAAS platform that enables credit unions to conduct a unified end-to-end business messaging modernization project.\nCompany #1 Highlight 1:Built a platform that enabled a small team to bring a product to market without a single developer.\nCompany #1 Highlight 2:Managed a small team of developers and designers\nCompany #2 Name:StackAdapt\nCompany #2 Role:CTO\nCompany #2 Summary:StackAdapt built a web-based platform for developers to automate and optimize their cloud infrastructure.\nCompany #2 Highlight 1:Built a platform from scratch to help automate the infrastructure of a variety of customers using a wide variety of technologies\nCompany #2 Highlight 2:Built a large scale distributed system\nPersonal Reference:I have experience working with Robbie both as a peer and as a member of a larger team, and have found him to be a very valuable asset to any team.\nCompany Name #1:Greenhouse Software\nCompany Role #1:Backend Developer\nFirst Company Summary #1: Built various services for a popular software as a service startup.\nCompany #1 Highlight 1:Worked on a variety of financial APIs\nCompany #1 Highlight 2:Designed and implemented a metrics gathering system\nCompany #2 Name:Greenhouse Software\nCompany #2 Role:Software Engineer / Developer\nCompany #2 Summary:Part time work while at Fullstack Academy. Worked on various JavaScript applications utilizing MEAN stack (Angular, Express, Node.js, MongoDB)\nPersonal Reference:Robbie is extremely personable and always willing to go above and beyond to help his teammates and his customers. I was happy to have him as part of my team at Greenhouse Software!\nInterests: Graphic Design. Sailing. Designing and building things.\n"
    }
  ],
  "created": 1632169880,
  "id": "cmpl-3kKEabFvRuqHwDScUsSNkPEgDUGj6",
  "model": "davinci:2020-05-03",
  "object": "text_completion"
}

text = response["choices"][0]["text"]

#text = "John Anderson\nJob Title:Software Engineer\nSummary:I have been a software engineer for the last 10 years. I have been working primarily in Java and .NET, with a little bit of python and javascript on the side. In the last year, I have been involved with a React / Redux application that is a PWA.\nCompany #1 Name:Community Foods\nCompany #1 Role:Front End Engineer\nCompany #1 Summary:Community Foods is a family-owned grocery store that has been a staple in the Northern Virginia community for over 50 years. I helped build a new, single page SPA that is react, react-router, redux, webpack, node, mongodb, docker, and isomorphic.\nCompany #1 Highlight 1:Built a very large and complex React / Redux application. It works on all platforms and has IOS/Android builds due to it being a PWA. (wrapped it in React Native though only implementing a WebView)\nCompany #1 Highlight 2:Hosted on a mixture of Heroku Apps and EC2 servers.\nCompany #2 Name:Spartan Cycles\nCompany #2 Role:Senior Software Engineer\nCompany #2 Summary:I was responsible for maintaining and extending the PHP based e-commerce web site that is responsible for managing millions of dollars of online retail bicycle sales.\nCompany #2 Highlight 1:Increased the capacity of the e-commerce website by 40% without any downtime by rewriting the shopping cart to use SQL instead of the previously used MongoDB\nCompany #2 Highlight 2:Migrated the website to microservices using NGINX for load balancing, Service Discovery, and Envoy Proxy\nPersonal Reference:John is an outstanding engineer who has always gone above and beyond to complete his work. He has demonstrated excellent skills with both front end and back end development, as well as helping out on some of the infrastructure projects I have given him. He is very good at taking complex problems and breaking them down into manageable pieces.\nInterests: Travel. Soccer.\n"
deliverable = {
  "basics": {
    "name": re.search('^([\w\s]+)\n', text).group(1),
    "label": re.search('Job Title:([\w\s]+)\n', text).group(1),
    "summary": re.search('Summary:(.+)\n', text).group(1)
  },
  "work": [{
    "name": re.search('Company #1 Name:(.+)\n', text).group(1),
    "position": re.search('Company #1 Role:(.+)\n', text).group(1),
    "summary": re.search('Company #1 Summary:(.+)\n', text).group(1),
    "highlights": [
      re.search('Company #1 Highlight 1:(.+)\n', text).group(1),
      re.search('Company #1 Highlight 2:(.+)\n', text).group(1),
    ]
  },
  {
    "name": re.search('Company #2 Name:(.+)\n', text).group(1),
    "position": re.search('Company #2 Role:(.+)\n', text).group(1),
    "summary": re.search('Company #2 Summary:(.+)\n', text).group(1),
    "highlights": [
      re.search('Company #2 Highlight 1:(.+)\n', text).group(1),
      re.search('Company #2 Highlight 2:(.+)\n', text).group(1),
    ]
  }],
  "references": [{
    "reference": re.search('Personal Reference:(.+)\n', text).group(1)
  }],
  "interests": [{
    "name": get_interests(re.search('Interests: (.+)\n', text).group(1))
  },
  {
    "name": re.search('Interests: ([\w]+)\. ([\w]+)\.\n', text).group(2)
  }]
}

print(deliverable)