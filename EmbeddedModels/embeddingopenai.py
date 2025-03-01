from langchain_openai import OpenAIEmbeddings #library for embedding model
from dotenv import load_dotenv #import env file
load_dotenv() #load env file

#specifying configuration and creating object
embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

#call embedding with embed_query function and can pass single query
result = embedding.embed_query("Delhi is the capital of india")
#query generates vector output of 32 dimension convert in string
print(str(result))


