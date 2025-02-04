from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def intro():

   return render_template("auth/login.html")

@app.route('/home')
def home():
   print("🛕홈페이지로 이동")
   #return 'This is Home! 헬로우 월드 5'
   return render_template("index.html")

@app.route('/calc', methods=["POST","GET"])
def calc():
   print("계산기")
   if request.method == "POST":

      num1= request.form.get('num1')
      num2= request.form.get('num2')
      opcode= request.form.get('opcode')
      eq = "="
      print("🙂num1 :", num1)
      print("😮num2 :", num2)
      print("😎opcode :", opcode)

      if opcode == '+' :
         num3 = int(num1) + int(num2)
      elif opcode == '-' :
         num3 = int(num1) - int(num2)
      elif opcode == '*' :
         num3 = int(num1) * int(num2)
      elif opcode == '/' :
         num3 = int(num1) / int(num2)
      else:
         num3 = "연산자가 잘못되었음"

      print(f"{num1} {opcode} {num2} = {num3}")
      print("😎플러스 성공")
      return render_template("calculator/calc.html", num1 = num1, opcode = opcode, num2 = num2, num3 = num3)
   else:
      return render_template("calculator/calc.html")
                           
@app.route('/login',methods=["post"])
def login2():
   print("😁로그인 알고리즘")
   username= request.form.get('username')
   password= request.form.get('password')
   print("😉username:", username)
   print("🙄passworld:", password)
   if username == "hong" and password == "1234":
       print("😎로그인 성공")
       return redirect(url_for('home'))
   else:
       print("😥로그인 실패")
       return render_template("auth/fail.html")

@app.route('/manufacture_fin_review')
def manufacture_fin_review():

   return render_template("esg/finchat_reports/manufacture_fin_review.html")

@app.route('/finance_visuals')
def finance_visuals():

   return render_template("esg/finchat_reports/finance_visuals.html")

@app.route('/retail_finbot')
def retail_finbot():

   return render_template("esg/finchat_reports/retail_finbot.html")




@app.route('/energy_esg_collector')
def energy_esg_collector():

   return render_template("esg/esg_analytics/energy_esg_collector.html")

@app.route('/esg_fin_viz_analystics')
def esg_fin_viz_analystics():

   return render_template("esg/esg_analytics/esg_fin_viz_analystics.html")

@app.route('/manufacture_esg_reporter')
def manufacture_esg_reporter():

   return render_template("esg/esg_analytics/manufacture_esg_reporter.html")






@app.route('/build_finance_auto')
def build_finance_auto():

   return render_template("esg/esg_finimpact/build_finance_auto.html")

@app.route('/health_care_fin_Bot')
def health_care_fin_Bot():

   return render_template("esg/esg_finimpact/health_care_fin_Bot.html")

@app.route('/retail_finance_auto')
def retail_finance_auto():

   return render_template("esg/esg_finimpact/retail_finance_auto.html")



if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True