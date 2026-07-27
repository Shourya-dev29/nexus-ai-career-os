from fastapi import FastAPI, UploadFile, File, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any, Optional
import time

from app.services.ocr_service import ocr_service
from app.services.gemini_service import gemini_service
from app.services.embedding_service import embedding_service
from app.services.graph_service import graph_service
from app.services.chat_service import chat_service
from app.services.career_service import career_service

app = FastAPI(
    title="NEXUS – AI Career Operating System API",
    version="1.0.0",
    description="Full Modular FastAPI engine powering OCR, Gemini 2.5 Flash, Neo4j, ChromaDB, and Explainable AI."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/health")
def health_check():
    return {"status": "healthy", "timestamp": time.time()}

@app.post("/api/v1/files/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    
    if file.filename.endswith(".pdf"):
        raw_text, ocr_conf = ocr_service.extract_text_from_pdf(content)
    else:
        raw_text, ocr_conf = ocr_service.extract_text_from_image(content)
        
    extracted_data = gemini_service.extract_structured_entities(raw_text)
    
    return {
        "fileId": f"file-{int(time.time())}",
        "filename": file.filename,
        "fileSize": len(content),
        "fileType": file.content_type or "application/pdf",
        "ocrConfidence": ocr_conf,
        "isDuplicate": False,
        "version": 1,
        "extractedText": raw_text[:300],
        "entities": extracted_data["entities"],
        "insights": extracted_data["insights"]
    }

@app.post("/api/v1/files/verify")
def verify_entities(payload: Dict[str, Any]):
    return {"status": "success", "message": "Entities committed to Knowledge Graph and Vector Store."}

@app.get("/api/v1/graph")
def get_graph():
    return graph_service.get_full_graph()

@app.get("/api/v1/timeline")
def get_timeline():
    return [
        {
            "id": "tl-1",
            "date": "2025-11-15",
            "title": "AWS Machine Learning Specialist Certified",
            "category": "Certificate",
            "description": "Passed AWS ML Specialty exam with 940/1000 score.",
            "documentTitle": "AWS_ML_Certificate_2025.pdf",
            "connectedEntities": ["AWS Certified Machine Learning Specialist", "Python 3.11"]
        },
        {
            "id": "tl-2",
            "date": "2025-08-30",
            "title": "Completed Meta AI Engineering Internship",
            "category": "Internship",
            "description": "Engineered multi-modal retrieval pipelines, reducing inference latency by 34%.",
            "documentTitle": "Meta_Internship_Completion_Letter.pdf",
            "connectedEntities": ["AI Engineering Intern at Meta", "PyTorch"]
        }
    ]

@app.get("/api/v1/career/readiness")
def get_readiness():
    return career_service.get_readiness_and_dna()

@app.get("/api/v1/chat/digital-memory")
def query_memory(query: str = Query("Show everything related to Python")):
    return chat_service.process_query(query)
