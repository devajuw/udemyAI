from mem0 import Memory
import os
from dotenv import load_dotenv
load_dotenv()

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text",
            "ollama_base_url": "http://localhost:11434",
        },
    },
    "llm": {
        "provider": "ollama",
        "config": {
            "model": "gemma3:1b",
            "base_url": "http://localhost:11434",
        },
    },
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": os.getenv("NEO4J_URI"),
            "username": os.getenv("NEO4J_USERNAME"),
            "password": os.getenv("NEO4J_PASSWORD"),
        },
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6033,
        },
    },
}

memory = Memory.from_config(config)

# after runnign this if we give prompt : Dev likes Badminton and chess , it would create new realtionship nodes in neo4j showing new realtions as Dev ->  Likes -> badminton, chess