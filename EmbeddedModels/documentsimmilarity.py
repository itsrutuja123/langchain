from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)
documents = ["Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.", "Ms Dhoni is former Indian captain famous for his calm demeanor and finishing skills.","Sachin Tendulkar , also known as 'God of Cricket',holds many batting records","Rohot sharma is known for his elegant batting and record-breaking double centuries","Jasprit Bumrah is an Indian fast bowler know for his unorthodox action and yorkers"]

query = 'tell me about virat kohli?'

doc_embeddings = embedding.embed_documents(documents)
query_embeddings = embedding.embed_query(query)

similarity_scores = cosine_similarity([query_embeddings], doc_embeddings)[0]
index,score=(sorted(list(enumerate(similarity_scores)),key=lambda x:x[1])[-1])

print(query)
print(documents[index])
print("similarity_score is:" ,similarity_scores)
