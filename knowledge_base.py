from dataclasses import dataclass
from typing import List

@dataclass
class MedicalCondition:
    amharic_keywords: List[str]
    english_name: str
    urgency: str
    urgency_score: int
    medication: str
    red_flags: str


medical_knowledge_base = [
    MedicalCondition(
        amharic_keywords=["ሆድ", "ሆዴ", "ሆዴን"],
        english_name="Abdominal Pain",
        urgency="Urgent",
        urgency_score=2,
        medication="Antacid / Omeprazole",
        red_flags="Vomiting or severe pain"
    ),
    MedicalCondition(
        amharic_keywords=["ራስ", "ራሴ", "ራሴን"],
        english_name="Headache",
        urgency="Routine",
        urgency_score=1,
        medication="Paracetamol",
        red_flags="Blurred vision"
    ),
    MedicalCondition(
        amharic_keywords=["ሳል", "ሳሌ"],
        english_name="Persistent Cough",
        urgency="Urgent",
        urgency_score=2,
        medication="Amoxicillin",
        red_flags="Difficulty breathing"
    ),
    MedicalCondition(
        amharic_keywords=["ትኩሳት", "ሙቀት"],
        english_name="High Fever",
        urgency="Emergency",
        urgency_score=3,
        medication="Paracetamol / Ibuprofen",
        red_flags="Seizure or stiffness"
    )
]