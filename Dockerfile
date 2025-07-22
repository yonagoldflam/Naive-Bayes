# 1. תשתית פייתון
FROM python:3.11-slim

# 2. התקנת pip וחבילות פייתון
RUN pip install --upgrade pip
RUN pip install fastapi uvicorn scikit-learn pandas

# 3. העתקת הקבצים
WORKDIR /app
COPY . /app

# 4. פתיחת פורט והרצה
EXPOSE 8000
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
