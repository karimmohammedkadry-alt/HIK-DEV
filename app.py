from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #هنا البايthون يقوم بتشغيل وعرض صفحة الـ HTML اللي فوق تلقائياً
    return render_template('index.html')

if __name__ == '__main__':
    # لتشغيل السيرفر المحلي لديك
    app.run(debug=True, port=5000)
