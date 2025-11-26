import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

# load .env
load_dotenv()


# Correct: first create an HF endpoint
endpoint = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    
    temperature=0.7,
)

# Correct: wrap endpoint inside ChatHuggingFace
llm = ChatHuggingFace(llm=endpoint)

message=llm.invoke("Explain the theory of relativity in simple terms.")
print(message.content)
