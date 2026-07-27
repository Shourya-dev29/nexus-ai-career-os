# NEXUS – AI Career Operating System

![NEXUS Cover](https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&q=80&w=1200)

**NEXUS** is an AI-first Career Operating System that transforms unstructured career artifacts (resumes, certificates, internship letters, codebases, project reports) into an interactive **Digital Twin**, **Neo4j Knowledge Graph**, and **AI Digital Memory**.

---

## 🚀 Key Features

- **Async AI Ingestion Pipeline**: PyMuPDF + Tesseract OCR → Gemini 2.5 Flash entity extraction → Human-in-the-Loop verification → ChromaDB vector storage + Neo4j Graph traversal.
- **Flagship AI Digital Memory**: Execute hybrid RAG queries (*"Show everything related to Python"*) connecting projects, certificates, internships, and timeline events with source references.
- **Explainable Career Readiness**: Calculates target role readiness (e.g. Senior AI Systems Engineer = 92%) with explicit mathematical breakdowns and AI-generated reasoning.
- **Agentic AI Assistant**: Performs automated actions like preparing for Google interviews, building web portfolios, generating ATS resumes, and crafting learning roadmaps.
- **Interactive Multi-Hop Knowledge Graph**: Visualizes 9 entity types and 8 multi-hop relationships (`HAS_SKILL`, `WORKED_ON`, `CERTIFIED_IN`, `INTERNED_AT`, `USES`).
- **Shareable Public Recruiter Profile**: Dynamic public candidate showcase URL (`/recruiter/alex-vance-ai`).

---

## 🏗️ Architecture & AI Workflow

```
[ Upload Document (PDF/DOCX/PNG/JPG) ]
                  │
                  ▼
   [ Async Processing Queue ]
                  │
                  ├──> 1. OCR Engine (PyMuPDF + Tesseract) + OCR Confidence Score
                  ├──> 2. Document Duplicate & Versioning Checker
                  ├──> 3. Gemini 2.5 Flash Structuring (10 Entity Types) + Confidence
                  ├──> 4. Human-in-the-Loop Entity Verification Modal (Accept/Edit/Reject)
                  ├──> 5. SentenceTransformers Embedding Generation -> ChromaDB Vector Store
                  ├──> 6. Neo4j Knowledge Graph Multi-Hop Injection
                  └──> 7. Interactive Timeline & Connected Memory Linker
```

---

## 🛠️ Tech Stack

- **Frontend**: Next.js 15 (App Router), TypeScript, TailwindCSS, Framer Motion, Lucide Icons
- **Backend API**: FastAPI, Pydantic V2, PyMuPDF, PyTesseract, Uvicorn
- **AI & Vectors**: Gemini 2.5 Flash, SentenceTransformers (`all-MiniLM-L6-v2`), ChromaDB
- **Graph Database**: Neo4j Graph Engine
- **Storage & Database**: Supabase PostgreSQL + Auth + Storage
- **Orchestration**: Docker & Docker Compose

---

## ⚙️ Getting Started & Local Setup

### 1. Prerequisites
- Node.js >= 18.x
- Python >= 3.11
- Docker Desktop (Optional for container deployment)

### 2. Frontend Installation
```bash
cd frontend
npm install
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) to view the application.

### 3. Backend Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
API Swagger documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs).

### 4. Running with Docker Compose
```bash
docker-compose up --build
```

---

## 📜 License
Licensed under the MIT License.
