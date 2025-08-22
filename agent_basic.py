from vertexai import init
from vertexai.generative_models import GenerativeModel
import os

class SimpleAgent:
    def __init__(self, model_name="gemini-2.0-flash"):
        init(project=os.environ["GOOGLE_CLOUD_PROJECT"], location=os.environ.get("REGION", "us-central1"))
        self.model = GenerativeModel(model_name)

    def ask(self, message: str) -> str:
        resp = self.model.generate_content(message)
        return resp.text

if __name__ == "__main__":
    agent = SimpleAgent()
    print(agent.ask("우리 워크숍의 목표를 2줄로 요약해줘"))
