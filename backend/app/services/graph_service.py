import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class GraphService:
    def get_full_graph(self) -> Dict[str, Any]:
        """Return connected graph nodes and relationships."""
        return {
            "nodes": [
                {"id": "person-1", "label": "Alex Vance", "type": "Person", "val": 25, "color": "#ec4899"},
                {"id": "skill-python", "label": "Python 3.11", "type": "Skill", "val": 18, "color": "#06b6d4"},
                {"id": "skill-pytorch", "label": "PyTorch", "type": "Skill", "val": 16, "color": "#06b6d4"},
                {"id": "skill-fastapi", "label": "FastAPI", "type": "Skill", "val": 15, "color": "#06b6d4"},
                {"id": "project-nexus", "label": "NEXUS AI OS", "type": "Project", "val": 20, "color": "#a855f7"},
                {"id": "cert-aws", "label": "AWS ML Specialist", "type": "Certificate", "val": 16, "color": "#f59e0b"},
                {"id": "intern-meta", "label": "Meta AI Internship", "type": "Internship", "val": 18, "color": "#10b981"},
                {"id": "tech-neo4j", "label": "Neo4j", "type": "Technology", "val": 14, "color": "#6366f1"},
                {"id": "tech-chroma", "label": "ChromaDB", "type": "Technology", "val": 14, "color": "#6366f1"},
                {"id": "edu-stanford", "label": "Stanford CS", "type": "Education", "val": 17, "color": "#f43f5e"}
            ],
            "links": [
                {"source": "person-1", "target": "skill-python", "label": "HAS_SKILL"},
                {"source": "person-1", "target": "skill-pytorch", "label": "HAS_SKILL"},
                {"source": "person-1", "target": "skill-fastapi", "label": "HAS_SKILL"},
                {"source": "person-1", "target": "project-nexus", "label": "WORKED_ON"},
                {"source": "person-1", "target": "cert-aws", "label": "CERTIFIED_IN"},
                {"source": "person-1", "target": "intern-meta", "label": "INTERNED_AT"},
                {"source": "person-1", "target": "edu-stanford", "label": "STUDIED_AT"},
                {"source": "project-nexus", "target": "skill-python", "label": "USES"},
                {"source": "project-nexus", "target": "tech-neo4j", "label": "USES"},
                {"source": "project-nexus", "target": "tech-chroma", "label": "USES"},
                {"source": "intern-meta", "target": "skill-pytorch", "label": "LEARNED"}
            ]
        }

graph_service = GraphService()
