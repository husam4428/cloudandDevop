FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# التطبيق الثاني سيعمل على بورت 5001 لتجنب التعارض
EXPOSE 5001
CMD ["python", "app.py"]