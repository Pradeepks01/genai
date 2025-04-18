from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings # type: ignore
from langchain_qdrant import QdrantVectorStore # type: ignore
from qdrant_client import QdrantClient # type: ignore
import getpass
import os
from google import genai

import pprint

file_path = '/home/gopal/projects/genai/paper.pdf'


loader = PyPDFLoader(file_path) 

docs = loader.load()

# print('docs',docs[10])

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_docs = text_splitter.split_documents(documents=docs) # type: ignore

os.environ["GOOGLE_API_KEY"] = "your api key"

embedder = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

query = input('>>')

# vector_store = QdrantVectorStore.from_documents(
#     documents=[],
#     collection_name="genai",
#     url="http://localhost:6333",
#     embedding=embedder
# )

# vector_store.add_documents(split_docs)


print('injection done')

print('docs',len(docs))
print('split_docs',len(split_docs))

retriver = QdrantVectorStore.from_existing_collection(
    collection_name="genai",
    url="http://localhost:6333",
    embedding=embedder
)

relevent_chunks = retriver.similarity_search(
    query=query,
)

# print('relevent_chunks',relevent_chunks)



system_prompt = f"""
you are an AI Assistant who is specalized in resolving query form the give context

context:
{relevent_chunks}
"""

# print(system_prompt)

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=query,
    config={
        'max_output_tokens': 40,
        'temperature': 0.9,
        'system_instruction':system_prompt
    }
)

print(response.text)


