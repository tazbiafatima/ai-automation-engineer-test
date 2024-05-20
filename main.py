#step one let's import all the neccary libraries 
#setup openai api key 
#take input via terminal in plain test 
#prompt - few-shot 
#idea - you are going to individually take in headline, article, post and fill it up in the Json format. (Or you can use guardrails - look this up later)
# prompt chaining to get all three values 
#system context - for tone & seo best practices look this up 
#setup a test function 
#

#seo looks like it's the main subject and angle mentioned in this article 

import json
import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv
import sys 


# Load .env file
load_dotenv()

#setup openai api key 
apiKey = os.getenv("OPENAI_API_KEY")
client = OpenAI()
 
#get the example inputs
f = open('data/sfc_article_001.txt', 'r')
example_1 = f.read() 
f.close()

f = open('data/sfc_article_002.txt', 'r')
example_2 = f.read() 
f.close()

f = open('data/sfc_article_003.txt', 'r')
example_3 = f.read() 
f.close()

#f = open('data/test_article.txt', 'r')
#inputArticle = f.read() 
#f.close()

#get input 

print("Hi, this script helps you generate headline, SEO URL and social media post suggestions. Enter your article here: ")

inputSentences = []
while True:
    line = input()
    if line == "":
        break
    inputSentences.append(line)
inputArticle = "\n".join(inputSentences)

if inputArticle:
    #prompt for headline 
    response = client.chat.completions.create(
    model="gpt-4o",
    response_format={ "type": "json_object"},
    temperature = 0.8,
    messages=[
        {"role": "system", "content": "You are an Audience Editor at Hearst Newspapers. You are also an SEO specialist who produces Headlines, SEO URLs and give Social Media Post Suggestions. Maintain the tone and style of the input article and return a JSON ouput. Here are examples of the Headline, URL, and Social media posts for the article."},
        {"role": "assistant", "content": example_1},
        {"role": "assistant", "content": example_2},
        {"role": "assistant", "content": example_3},
        {"role": "user", "content": "For the input article: " + inputArticle + "Generate a one-sentence Headline, SEO URL's Article Permalink and a Social Media Post and return as the value for the JSON keys 'Headline', 'Article' and 'Social Media Post'"}
    ]
    )
    
    result = (response.choices[0].message.content)
    
    outputJson = json.loads(result)
    
    print("Output: ", outputJson)
    
else: 
    print("Error. Please re-enter the input.")
    
    




