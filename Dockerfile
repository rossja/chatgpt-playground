FROM python:3-alpine
WORKDIR /app

COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src/runner.py .

CMD ["python", "runner.py"]