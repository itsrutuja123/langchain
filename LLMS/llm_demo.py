from langchain_openai import OpenAI # library through which lanchain can communicate
from dotenv import load_dotenv #to import key

#load file
load_dotenv()

#create an object and specify model to communicate
llm= OpenAI(model='gpt-3.5-turbo-instruct')

#invoke method to communicate and write the prompt

result = llm.invoke("prompt")

print(result)

#both input and output is string
