
from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
import os
client = OpenAI(
        base_url="http://localhost:11434/v1",
    api_key="ollama",
)
CHAT_MODEL = os.getenv("OLLAMA_CHAT_MODEL", "gemma3:4b")
load_dotenv()
embedding_model = OllamaEmbeddings(
    model=os.getenv("OLLAMA_EMBED_MODEL", os.getenv("OLLAMA_MODEL", "nomic-embed-text")),
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
)

vector_db = QdrantVectorStore.from_existing_collection(
      embedding=embedding_model,
    url=os.getenv("QDRANT_URL", "http://localhost:6033"),
    collection_name = "learning_rag"
)
# Take User Input

user_query = input("❔Ask Something : ")

search_results = vector_db.similarity_search(query = user_query)
context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results ])
SYSTEM_PROMPT= f"""
You are a helpful AI assistant who answers user query based on the avaialable Context retrieved from a PDF file along with page_contents and page number.

You should only ans the user based on the following context and navigate the user to open the right page number to know more.

Context:
{context} """

response=client.chat.completions.parse(
    model=CHAT_MODEL,
        messages=[
            {"role": "system","content": SYSTEM_PROMPT},
            {"role": "user","content": user_query}

        ],
    )
print(f"🤖:{response.choices[0].message.content}")
        