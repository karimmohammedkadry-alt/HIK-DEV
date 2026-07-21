from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #هنا البايthون يقوم بتشغيل وعرض صفحة الـ HTML اللي فوق تلقائياً
    return render_template('index.html')

if __name__ == '__main__':
    # لتشغيل السيرفر المحلي لديك
    app.run(debug=True, port=5000)
    
    
    
    from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
import gspread

app = Flask(__name__)
CORS(app)  # عشان نسمح لموقعك يبعت بيانات للسيرفر من غير مشاكل أمان

# الاتصال بجوجل شيت
gc = gspread.service_account(filename="credentials.json")
sh = gc.open("HIK Store Order")  # اسم جوجل شيت بتاعك
worksheet = sh.sheet1


@app.route("/order", methods=["POST"])
def receive_order():
  data = request.json
  name = data.get("name")
  phone = data.get("phone")
  product = data.get("product")
  current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  # تسجيل الأوردر في جوجل شيت تلقائياً
  worksheet.append_row([name, phone, product, current_time])

  return jsonify({"status": "success", "message": "تم تسجيل الأوردر!"})


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)

