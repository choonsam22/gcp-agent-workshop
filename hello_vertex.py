from vertexai import init
from vertexai.generative_models import GenerativeModel
from config import PROJECT_ID, LOCATION, MODEL_NAME

init(project=PROJECT_ID, location=LOCATION)
model = GenerativeModel(MODEL_NAME)

resp = model.generate_content("안녕! 넌 누구야? 한 줄로 답해줘")
print(resp.text)
