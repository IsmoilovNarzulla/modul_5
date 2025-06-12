# 1-USUL: http.server moduli (eng oddiy veb server)
# Bu usul hech qanday kutubxona o‘rnatmasdan, statik fayllarni (HTML, CSS, JS) ko‘rsatish uchun ishlatiladi.
#
# 📁 Tuzilishi:
# pgsql
# Копировать
# Редактировать
# my_server/
# ├── index.html
# └── server.py
# 📄 index.html
# html
# Копировать
# Редактировать
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Simple Server</title>
# </head>
# <body>
#     <h1>Python Veb Server ishlayapti!</h1>
# </body>
# </html>
# 📄 server.py
# python
# Копировать
# Редактировать
# import http.server
# import socketserver
#
# PORT = 8000
#
# Handler = http.server.SimpleHTTPRequestHandler
#
# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print(f"Server ishga tushdi: http://localhost:{PORT}")
#     httpd.serve_forever()
# ▶ Terminalda ishga tushiring:
#
# bash
# Копировать
# Редактировать
# python server.py
# 📥 Kirish: http://localhost:8000

# ✅ 2-USUL: Flask asosida dinamik veb server
# Agar siz formalar, ma'lumot yuborish, JSON bilan ishlashni istasangiz — Flask juda qulay.
#
# 🔧 Flask o‘rnatish:
# bash
# Копировать
# Редактировать
# pip install flask
# 📄 app.py
# python
# Копировать
# Редактировать
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Oddiy sahifa
@app.route('/')
def home():
    return render_template_string("""
    <h2>Flask server ishlayapti!</h2>
    <form method="POST" action="/hello">
        Ismingiz: <input name="name">
        <button type="submit">Yuborish</button>
    </form>
    """)

# POST orqali ma'lumot qabul qilish
@app.route('/hello', methods=['POST'])
def hello():
    name = request.form['name']
    return f"<h3>Salom, {name}!</h3>"

if __name__ == '__main__':
    app.run(debug=True)

# ▶ Terminalda ishga tushiring:
#
# bash
# Копировать
# Редактировать
# python app.py
# 📥 Kirish: http://127.0.0.1:5000
#
# 💡 Qaysi birini tanlash kerak?
# Maqsad	Tavsiya
# Faqat statik HTML xizmatga tushurish	http.server (oddiy va tez)
# Interaktiv sahifa, ma’lumot yuborish	Flask (prof darajada)

