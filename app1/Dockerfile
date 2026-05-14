# استخدام نسخة خفيفة من بايثون
FROM python:3.9-slim

# تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملف المكتبات وتثبيتها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ الكود بالكامل
COPY . .

# تشغيل التطبيق على منفذ 5000
EXPOSE 5000
CMD ["python", "app.py"]