import re


class GeminiService:

    def extract_structured_entities(self,text:str):

        entities=[]


        skills=[
            "Python",
            "Java",
            "JavaScript",
            "React",
            "Next.js",
            "FastAPI",
            "Django",
            "AWS",
            "Docker",
            "Kubernetes",
            "Machine Learning",
            "AI",
            "SQL"
        ]


        for skill in skills:
            if skill.lower() in text.lower():

                entities.append(
                    {
                    "id":f"ent-{len(entities)+1}",
                    "name":skill,
                    "type":"Skill",
                    "confidence":0.95,
                    "status":"accepted"
                    }
                )


        return {

            "category":"Document",

            "ocrConfidence":0.95,

            "entities":entities,

            "insights":{

                "documentsProcessed":1,

                "skillsFound":len(entities),

                "projectsFound":0,

                "certificationsFound":0,

                "careerInsights":[
                    "Skills extracted from uploaded document"
                ],

                "recommendedNextSteps":[
                    "Add more project documents"
                ]

            }

        }


gemini_service=GeminiService()