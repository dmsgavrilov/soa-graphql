FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY /app .

# set python environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH="." \
    FLASK_APP="app/main.py"

EXPOSE 5000

CMD ["python3", "app/main.py"]
