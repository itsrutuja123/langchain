# Using an open-source Hugging Face model by downloading it locally
from langchain.llms import HuggingFacePipeline
from langchain_huggingface import ChatHuggingFace
from dotenv import load_dotenv  # Load .env file
import os  # To change Hugging Face home directory

# Set Hugging Face cache directory to D:/Langchain instead of default C:/
os.environ['HF_HOME'] = 'D:/Langchain'

# Load environment variables
load_dotenv()

# Ensure Hugging Face API token is set (if required)
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# LLM: Specifies the model, task, and optional parameters
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # Check if the model exists
    task="text-generation",
    pipeline_kwargs=dict(temperature=0.5, max_new_tokens=100)  
)

# Create a ChatHuggingFace object with the LLM
model = ChatHuggingFace(llm=llm)

# Invoke method and prompt
result = model.invoke("What is the capital of India?")
print(result)

# Print only the answer
print(result.content)
