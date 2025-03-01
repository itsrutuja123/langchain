from langchain_openai import OpenAIEmbeddings #library for embedding model
from dotenv import load_dotenv #import env file
load_dotenv() #load env file

#specifying configuration and creating object
embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

#to give multiple query create doc(dict) write queries and pass that as input
documents =["Delhi is capital of india","paris is capital of france"]

#call embedding with embed_document function and can pass single query
result = embedding.embed_documents("Delhi is the capital of india")
#query generates vector list output of 32 dimension convert in string
print(str(result))


