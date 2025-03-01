#uisng openai
from langchain_openai import ChatOpenAI #chatopenai class for chatmodels
from dotenv import load_dotenv #load env file

load_dotenv()
#create a object and specify the model to use
model=ChatOpenAI(model='gpt-4',tempreture=1.5) #tempreture defines the creativity or randomness of the model range from(0-2)

#invoke method and prompt
result=model.invoke("prompt")
print(result) 
#input is string but output contains multiple things along with ans
#to print only answer 
print(result.content)



