import openai
from os import environ
from dotenv import load_dotenv
import numpy as np

load_dotenv()
openai.key = environ.get("OPENAI_API_KEY")

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

text = 'big pink elephant'
image = '...'
model = 'text-embedding-ada-002'
original_embedding = openai.embeddings.create(input=[text], model='text-embedding-ada-002')
while True:
    query = input("Enter a query: ")
    if query == "exit":
        break
  
    embd = openai.embeddings.create(input=[query], model='text-embedding-ada-002')
    print(f"Similarity: {cosine_similarity(original_embedding.data[0].embedding, embd.data[0].embedding)}")
