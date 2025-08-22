from vertexai import init
from vertexai.generative_models import GenerativeModel
import os

project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")

model_name = "gemini-2.5-flash-lite"

# 서울 리전 대신 global 지정
location = os.environ.get("REGION", "asia-northeast3")
if model_name.startswith("gemini-2.5"):
    location = "global"

init(project=project_id, location=location)
# 더 작은 모델로 전환
model = GenerativeModel(model_name)
resp = model.generate_content("안녕! 넌 누구야? 한 줄로 답해줘")
print(resp.text)
