from dotenv import load_dotenv
from pathlib import Path
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
load_dotenv()
pdf_path = Path(__file__).parent / "nodejs.pdf"

loader =  PyPDFLoader(file_path=pdf_path)
docs =  loader.load()

#split docs into smaller chunks

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size =  1000,
    chunk_overlap=400

)

chunks = text_splitter.split_documents(documents=docs)
#vector embedings
embedding_model = OllamaEmbeddings(
    model=os.getenv("OLLAMA_MODEL", "nomic-embed-text"),
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
)
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url=os.getenv("QDRANT_URL", "http://localhost:6033"),
    collection_name = "learning_rag"
)
print("Indexing of DOCS done....")