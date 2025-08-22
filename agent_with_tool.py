from vertexai import init
from vertexai.generative_models import GenerativeModel
from config import PROJECT_ID, LOCATION, MODEL_NAME
import json
from agent_tools import get_sales_by_region

init(project=PROJECT_ID, location=LOCATION)
model = GenerativeModel(MODEL_NAME)

TOOLS = {"get_sales_by_region": get_sales_by_region}

SYSTEM_PROMPT = (
    "너는 회사 내부 데이터에 친절히 답하는 비서야. 사용자가 '지역 매출'을 물으면 "
    "JSON으로 {\"tool\": \"get_sales_by_region\", \"args\": {\"region\": \"...\"}} 형식으로 먼저 응답해. "
    "그 다음 함수 결과를 받아 자연어로 최종 답해."
)

def run(query: str):
    plan = model.generate_content(
        f"{SYSTEM_PROMPT}\n\n사용자 질문: {query}\n도구 호출 JSON만 출력:"
    ).text.strip()
    try:
        plan_json = json.loads(plan)
        tool_name = plan_json.get("tool")
        args = plan_json.get("args", {})
        if tool_name in TOOLS:
            tool_result = TOOLS[tool_name](**args)
            return model.generate_content(
                f"질문: {query}\n도구 결과: {tool_result}\n이를 바탕으로 한국어로 간단히 답해"
            ).text
        return "해당 도구를 찾을 수 없습니다."
    except Exception:
        return model.generate_content(query).text

if __name__ == "__main__":
    print(run("seoul 지역 매출 알려줘"))
