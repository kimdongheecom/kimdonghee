from flask import Flask, render_template, request, redirect, url_for
from com.kimdonghee.auth.login_controller import LoginController
from com.kimdonghee.auth.login_model import LoginModel
from com.kimdonghee.calculator.calc_controller import CalcController
from com.kimdonghee.calculator.calc_model import CalcModel
app = Flask(__name__)

@app.route('/')
def intro():

   return render_template("auth/login.html")



@app.route('/home')
def home():
   print("🛕홈페이지로 이동")
   #return 'This is Home! 헬로우 월드 5'
   return render_template("index.html")

@app.route('/discount', methods=["POST","GET"])
def discount():
   print("할인")
   if request.method == "POST":
      amount = request.form.get('amount')
      print("amount:", amount) # string값 뒤에 , 찍고 값을 준다.
      
   else:
       return render_template("calculator/discount.html")

@app.route('/calc', methods=["POST","GET"])
def calc():
   print("계산기")
   if request.method == "POST":

      num1= request.form.get('num1') #이 세개는 라우터에서 해줘야 한다
      num2= request.form.get('num2')
      opcode= request.form.get('opcode')
      eq = "="
      print("🙂num1 :", num1)
      print("😮num2 :", num2)
      print("😎opcode :", opcode)

      calc = CalcModel()
      calc.num1 = int(num1) #num1을 calc라는 밖스에 담는 과정......밖스에 담는 의미는 정수로 변환시키겠다.
      calc.num2 = int(num2) #app.py에서는 상수 상태로 되어있다. int는 상수로 변환시킨다는 말, str은 문자열로 변환시키겠다는 말
      calc.opcode = opcode

      controller = CalcController()
      resp : CalcModel = controller.getResult(calc)

      print(f"{resp.num1} {resp.opcode} {resp.num2} = {resp.result}")
      print("😎플러스 성공")
      return render_template("calculator/calc.html", num1 = resp.num1, opcode = resp.opcode, num2 = resp.num2, result = resp.result)
   else:
      return render_template("calculator/calc.html")
                           
@app.route('/login',methods=["POST"]) #라우팅(데이터를 전송하는 방법) 과정
def login(): #함수가 실행될 때 로그인 처리를 담당, 사용자가 로그인 정보를 입력하고 제출하면, Flask가 login() 함수를 실행
   
   print("😁로그인 알고리즘")

   username= request.form.get('username') #input
   password= request.form.get('password') #input
   print("😉username:", username)
   print("🙄passworld:", password)

   login = LoginModel()
   login.username = username #login 상자 안에 username 칸막이에 username을 담았다....결국, 보내는 것은 login상자만 넘기니까....
   login.password = password #..아래에 resp:LoginModel = controller.getResult(login)에 login 상자를 담았다.
   controller = LoginController()
   resp:LoginModel = controller.getResult(login)
 
   
   return redirect(url_for(resp.result)) #resp.result는 Lo

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