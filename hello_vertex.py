from vertexai import init
from vertexai.generative_models import GenerativeModel
import os

project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")

vertexai.init(project=my-project-40086', location='us-central1')

model = GenerativeModel("gemini-1.5-flash")

resp = model.generate_content("안녕! 넌 누구야? 한 줄로 답해줘")

print(resp.text)
