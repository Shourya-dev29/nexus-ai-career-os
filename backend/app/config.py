import os
import json
import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class Settings:
    PROJECT_NAME: str = "NEXUS AI Career Operating System"
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    NEO4J_URI: str = os.getenv("NEO4J_URI", "neo4j://localhost:7687")
    NEO4J_USER: str = os.getenv("NEO4J_USER", "neo4j")
    NEO4J_PASSWORD: str = os.getenv("NEO4J_PASSWORD", "password")
    EMBEDDING_MODEL_NAME: str = "sentence-transformers/all-MiniLM-L6-v2"
    CHROMA_PERSIST_DIR: str = "./chroma_db"

settings = Settings()
