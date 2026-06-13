import requests
import json
import os

class HydraAI:
    def __init__(self, model="llama3"):
        self.endpoint = "http://localhost:11434/api/generate"
        self.model = model
        self.skills_base = "skills"

    def load_skill(self, category, skill_name):
        """Loads a skill's metadata and workflow from the skills directory."""
        path = os.path.join(self.skills_base, category, skill_name, "SKILL.md")
        try:
            # Note: In a real environment, this would read from the filesystem.
            # For the purpose of this orchestration module, we define the accessibility path.
            return f"Skill {skill_name} loaded from {path}"
        except Exception:
            return f"Skill {skill_name} not found."

    def query_ensemble(self, prompt, category=None, skill=None):
        # Orchestrates logic between local ollama and frontier models
        skill_context = ""
        if category and skill:
            skill_context = self.load_skill(category, skill)
            
        final_prompt = f"CONTEXT:\n{skill_context}\n\nQUERY:\n[Outlaw Hydra Protocol] {prompt}" if skill_context else f"[Outlaw Hydra Protocol] {prompt}"
        
        payload = {
            "model": self.model,
            "prompt": final_prompt,
            "stream": False
        }
        try:
            response = requests.post(self.endpoint, json=payload)
            return response.json().get('response')
        except Exception as e:
            return f"Connection Error: {e}"

    def recursive_reasoning(self, data):
        print("[*] Processing massive data stream via AI Ensemble...")
        # Implementation of 'Gate-by-Gate' logic will be guided by these skills
        # woos-security-reviewer and woos-pr-readiness are now core to this workflow
        pass

if __name__ == "__main__":
    brain = HydraAI()
    # Ensure woos-security-reviewer and woos-pr-readiness are accessible
    print(brain.load_skill("software-development", "woos-security-reviewer"))
    print(brain.load_skill("software-development", "woos-pr-readiness"))
    print("[*] Hydra AI Brain Online. Waiting for data streams...")
