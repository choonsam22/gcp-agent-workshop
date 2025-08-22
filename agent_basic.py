from vertexai import init
from vertexai.generative_models import GenerativeModel
from config import PROJECT_ID, LOCATION, MODEL_NAME

class SimpleAgent:
    def __init__(self, model_name=MODEL_NAME):
        init(project=PROJECT_ID, location=LOCATION)
        self.model = GenerativeModel(model_name)

    def ask(self, message: str) -> str:
        return self.model.generate_content(message).text

if __name__ == "__main__":
    agent = SimpleAgent()
    print(agent.ask("우리 워크숍의 목표를 2줄로 요약해줘"))
