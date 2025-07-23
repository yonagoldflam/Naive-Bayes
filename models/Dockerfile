FROM python:3.11-slim

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn scikit-learn pandas

WORKDIR /app
COPY . .

EXPOSE 8000
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
