import numpy as np
import json

class OnDeviceHealthRAG:
    def __init__(self, knowledge_base_path: str):
        # Load local medical guidelines (e.g., WHO, UNICEF)
        with open(knowledge_base_path, 'r') as f:
            self.knowledge_base = json.load(f)
            
    def _simple_embedding(self, text: str) -> np.ndarray:
        """
        In production, use Gemma 4's lightweight embedder token layer locally.
        Simulating keyword/vector mapping here.
        """
        # Placeholder for extracting vector arrays on device
        return np.random.rand(1, 128)

    def retrieve_trusted_context(self, user_query_tokens: str) -> str:
        """Finds the closest verified medical snippet to prevent hallucinations."""
        # Loop through local DB and find the best match
        # Returning a mockup matching context for 'fever'
        best_match = self.knowledge_base.get("fever", "General hydration and rest.")
        return best_match

    def get_safety_system_prompt(self, user_dialect: str) -> str:
        """Strictly restricts Gemma 4 to the context and local language nuances."""
        return f"""
        You are a helpful, empathetic rural health assistant speaking fluent {user_dialect}.
        
        CRITICAL RULES:
        1. Answer ONLY using the provided Trusted Context. Do not invent medical facts.
        2. Speak in simple, non-technical terms. Use local units of measurement.
        3. If symptoms show an emergency (e.g., unconscious, bleeding), stop and trigger EMERGENCY_ALERT.
        4. Output your response directly in audio token formats or native script.
        """
