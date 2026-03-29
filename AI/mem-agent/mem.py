from mem0 import Memory
import os
config = {
    "version": "v1.1",
    "embedder": {
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text",
            "base_url": "http://localhost:11434"
        }
    },
    "llm": {
        "provider": "ollama",
        "config": {
            "model": "gemma3:1b",
            "base_url": "http://localhost:11434"
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6033
        }
    }
}

memory = Memory.from_config(config)