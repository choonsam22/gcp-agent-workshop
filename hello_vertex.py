from vertexai import init
from vertexai.generative_models import GenerativeModel
import os

project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")

model_name = "gemini-2.0-flash"
location = "us-central1"

init(project=project_id, location=location)

model = GenerativeModel(model_name)

resp = model.generate_content("안녕! 넌 누구야? 한 줄로 답해줘")

print(resp.text)
