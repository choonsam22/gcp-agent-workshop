FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -U pip && pip install -r requirements.txt && pip install streamlit
ENV PORT=8080
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
