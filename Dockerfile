FROM python:3.7-slim
FROM pytorch/pytorch:latest 
WORKDIR /app

COPY . ./

RUN pip install -r ./requirements.txt

CMD exec gunicorn --bind :8080 --workers 1 --worker-class uvicorn.workers.UvicornWorker --threads 8 --timeout 0 app:app
