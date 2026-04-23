from knowledge_base import medical_knowledge_base


class TriageAgent:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def analyze(self, patient_input: str):

        # normalize input (IMPORTANT FIX)
        clean_input = patient_input.replace(" ", "")

        best_match = None
        best_score = 0

        # scoring system (FIXED LOGIC)
        for condition in self.knowledge_base:
            score = 0

            for keyword in condition.amharic_keywords:
                if keyword in clean_input:
                    score += 1

            if score > best_score:
                best_score = score
                best_match = condition

        # no match case
        if not best_match:
            return None

        return best_match
    