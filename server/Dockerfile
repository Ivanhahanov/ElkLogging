FROM python:3.9-alpine
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY app /app
CMD python3 /app/server.py