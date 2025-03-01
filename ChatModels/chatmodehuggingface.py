#using open source hugging face api
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint 
from dotenv import load_dotenv #load env file

load_dotenv()
#llm specifies which model is being used along with task and path 
llm= HuggingFaceEndpoint(repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",task="text-generation")
#create a object and specify the model to use
model=ChatHuggingFace(llm=llm) 

#invoke method and prompt
result=model.invoke("what is the capital of india?")
print(result) 
#input is string but output contains multiple things along with ans
#to print only answer 
print(result.content)



