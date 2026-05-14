from flask import Flask, render_template_string
import redis

app = Flask(__name__)

# الاتصال بـ Redis (نفس قاعدة البيانات التي يستخدمها App 1)
cache = redis.Redis(host='redis', port=6379, decode_responses=True)

HTML_TEMPLATE = '''
<h1>DevOpsHub - Dashboard</h1>
<div style="border: 1px solid #ccc; padding: 10px; margin-bottom: 10px;">
    <h3>Total Messages Collected: {{ msg_count }}</h3>
</div>
<div style="border: 1px solid #ccc; padding: 10px;">
    <h3>Total Page Visits (from App 1): {{ visits }}</h3>
</div>
<p><button onclick="location.reload()">Refresh Data</button></p>
'''

@app.route('/')
def dashboard():
    # 1. جلب عدد الرسائل (طول القائمة في Redis)
    msg_count = cache.llen('messages_list')
    
    # 2. جلب عدد الزيارات الكلي
    visits = cache.get('visit_count')
    if visits is None:
        visits = 0
        
    return render_template_string(HTML_TEMPLATE, msg_count=msg_count, visits=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)