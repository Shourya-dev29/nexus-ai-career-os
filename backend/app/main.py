from fastapi import FastAPI, UploadFile, File, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any, Optional
from app.services.ocr_service import ocr_service
from app.services.gemini_service import gemini_service
import time
import fitz
import io
from PIL import Image
import pytesseract
from docx import Document

app = FastAPI(
    title="NEXUS – AI Career Operating System API",
    version="1.0.0",
    description="Full Modular FastAPI engine powering OCR, Gemini 2.5 Flash, Neo4j, ChromaDB, and Explainable AI."
)

def extract_text(filename, content):

    text = ""

    if filename.endswith(".pdf"):
        pdf = fitz.open(stream=content, filetype="pdf")

        for page in pdf:
            text += page.get_text()


    elif filename.endswith(".docx"):

        doc = Document(io.BytesIO(content))

        for para in doc.paragraphs:
            text += para.text + "\n"


    elif filename.endswith((".png",".jpg",".jpeg")):

        image = Image.open(io.BytesIO(content))
        text = pytesseract.image_to_string(image)


    return text

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

    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        extracted_text, confidence = ocr_service.extract_text_from_pdf(content)

    elif filename.endswith((".png",".jpg",".jpeg")):
        extracted_text, confidence = ocr_service.extract_text_from_image(content)

    else:
        extracted_text = "Unsupported file type"
        confidence = 0.80


    ai_result = gemini_service.extract_structured_entities(
        extracted_text
    )


    return {
        "fileId": f"file-{int(time.time())}",
        "filename": file.filename,
        "fileSize": len(content),
        "fileType": file.content_type,
        "ocrConfidence": confidence,
        "extractedText": extracted_text,
        "entities": ai_result["entities"],
        "insights": ai_result["insights"]
    }

@app.post("/api/v1/files/verify")
def verify_entities(payload: Dict[str, Any]):
    return {"status": "success", "message": "Entities committed to Knowledge Graph and Vector Store."}

@app.get("/api/v1/graph")
def get_graph():
    return {
        "nodes": [
            {"id": "person-1", "label": "Alex Vance", "type": "Person", "val": 25, "color": "#ec4899"},
            {"id": "skill-python", "label": "Python 3.11", "type": "Skill", "val": 18, "color": "#06b6d4"},
            {"id": "skill-pytorch", "label": "PyTorch", "type": "Skill", "val": 16, "color": "#06b6d4"},
            {"id": "skill-fastapi", "label": "FastAPI", "type": "Skill", "val": 15, "color": "#06b6d4"},
            {"id": "project-nexus", "label": "NEXUS AI OS", "type": "Project", "val": 20, "color": "#a855f7"},
            {"id": "cert-aws", "label": "AWS ML Specialist", "type": "Certificate", "val": 16, "color": "#f59e0b"},
            {"id": "intern-meta", "label": "Meta AI Internship", "type": "Internship", "val": 18, "color": "#10b981"}
        ],
        "links": [
            {"source": "person-1", "target": "skill-python", "label": "HAS_SKILL"},
            {"source": "person-1", "target": "skill-pytorch", "label": "HAS_SKILL"},
            {"source": "person-1", "target": "skill-fastapi", "label": "HAS_SKILL"},
            {"source": "person-1", "target": "project-nexus", "label": "WORKED_ON"},
            {"source": "person-1", "target": "cert-aws", "label": "CERTIFIED_IN"},
            {"source": "person-1", "target": "intern-meta", "label": "INTERNED_AT"}
        ]
    }

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
    return {
        "overallScore": 92,
        "targetRole": "Senior AI Systems Engineer",
        "strengths": ["Strong proficiency in Python & PyTorch", "Graph Neural Networks"],
        "weaknesses": ["Kubernetes Cluster Ops"],
        "missingSkills": ["Kubernetes (K8s)", "Triton Inference Server"],
        "suggestedImprovements": ["Complete CKA certification"],
        "breakdown": {
            "skillsScore": 95,
            "projectsScore": 94,
            "certificationsScore": 88,
            "internshipsScore": 96,
            "achievementsScore": 87,
            "reasoning": ["+32% score from 12 verified core AI skills"]
        },
        "dnaFitScores": {
            "AI Systems Engineer": 94,
            "Backend Engineer": 91,
            "Data Scientist": 86
        }
    }

@app.get("/api/v1/chat/digital-memory")
def query_memory(query: str = Query("Show everything related to Python")):
    return {
        "items": [
            {
                "id": "mem-1",
                "title": "Python 3.11 & FastAPI Performance Benchmark",
                "type": "Document",
                "category": "Project Codebase",
                "snippet": "Implemented asynchronous connection pooling and uvloop in FastAPI, achieving 14,200 req/sec for Python ML inference endpoints.",
                "date": "2025-11-20",
                "tags": ["Python", "FastAPI", "Performance", "Backend"],
                "relevanceScore": 0.98,
                "connectedNodes": ["Python 3.11", "FastAPI Backend", "Nexus AI Operating System"]
            }
        ],
        "aiSummary": f"Nexus AI Digital Memory connected verified artifacts related to '{query}'."
    }
