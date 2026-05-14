from flask import Flask, request, render_template_string
import redis

app = Flask(__name__)

# الاتصال بـ Redis باستخدام اسم الخدمة "redis" كما سيحدد في docker-compose
cache = redis.Redis(host='redis', port=6379, decode_responses=True)

HTML_TEMPLATE = '''
<h1>DevOpsHub - Message Collector</h1>
<p>Total Visits: {{ visits }}</p>
<form method="POST" action="/send">
    <input type="text" name="message" placeholder="Enter your feedback" required>
    <button type="submit">Send</button>
</form>
'''

@app.route('/')
def index():
    # زيادة عداد الزيارات في كل مرة يتم فيها تحميل الصفحة 
    visits = cache.incr('visit_count')
    return render_template_string(HTML_TEMPLATE, visits=visits)

@app.route('/send', methods=['POST'])
def send():
    msg = request.form.get('message')
    if msg:
        # إضافة الرسالة إلى قائمة في Redis (كـ Log دائم) [cite: 3, 5]
        cache.lpush('messages_list', msg)
    return 'Message sent! <a href="/">Go back</a>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)