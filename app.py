from flask import Flask, render_template, request, redirect, url_for
from com.kimdnghee.auth.login_controller import LoginController
from com.kimdnghee.auth.login_model import LoginModel
from com.kimdnghee.calculator.bmi_controller import BmiController
from com.kimdnghee.calculator.bmi_model import BmiModel
from com.kimdnghee.calculator.calc_controller import CalcController
from com.kimdnghee.calculator.calc_model import CalcModel
from com.kimdnghee.calculator.discount_controller import DiscountController
from com.kimdnghee.calculator.discount_model import DiscountModel
from com.kimdnghee.calculator.grade_controller import GradeController
from com.kimdnghee.calculator.grade_model import GradeModel
from com.kimdnghee.calculator.gugudan_controller import GugudanController
from com.kimdnghee.calculator.gugudan_model import GugudanModel

app = Flask(__name__)

@app.route('/')
def intro():

   return render_template("auth/login.html")

@app.route('/home')
def home():
   print("🛕홈페이지로 이동")
   #return 'This is Home! 헬로우 월드 5'
   return render_template("index.html")

@app.route('/bmi', methods=["POST","GET"])
def bmi():
   print("계산기")

   if request.method == "POST":

      height= request.form.get('height') #이 세개는 라우터에서 해줘야 한다
      weight= request.form.get('weight')
      
      controller = BmiController(height=height,weight=weight)

      resp: BmiModel = controller.getRe
      
      render_html ='<h3>결과 보기</h3>'
      return render_template("calculator/bmi.html", num1 = resp.num1, opcode = resp.opcode, num2 = resp.num2, result = resp.result, render_html = render_html)
 
      print("😎플러스 성공")
      
   else: 
      return render_template("calculator/bmi.html")


@app.route('/discount', methods=["POST","GET"])
def discount():
   print("할인")
   if request.method == "POST":
      amount = request.form.get('amount')
      print("amount:", amount) # string값 뒤에 , 찍고 값을 준다.
      
      discount = DiscountModel()
      discount.amount = int(amount)

      controller = DiscountController()
      resp: DiscountModel = controller.getResult(discount)

      print(f"{resp.discounted_price} = {amount} * (1 - {resp.sale})")

      return render_template("calculator/discount.html", amount = resp.amount, discounted_price = resp.discounted_price, sale = resp.sale)

   else:
       return render_template("calculator/discount.html")
   
@app.route('/gugudan', methods=["POST","GET"])
def gugudan():
   print("구구단")
   if request.method == "POST":
      print("🤦‍♀️POST 방식으로 전송된 데이터")
      dan = request.form.get('dan')
      # gugudan = GugudanModel() #구구단 모델 객체 생성하였다. 그 이름을 구구단이라고 한다.
      # gugudan.dan = int(dan) #문자열을 정수로 변환 후 객체의 속성 값에 저장하였다. 예를 들어, dan ="5"로 문자열로 주어진 값이 있다면 정수로 변환하기 위한 과정이다.

      controller = GugudanController(dan=dan) #구구단 컨트롤러 객체 생성하였다. 즉, 구구단 컨트롤러 클래스의 새로운 객체를 생성하여 컨트롤러 공간에 dan이라는 값을 dan이라는 이름으로 저장한 것이다.
      resp: GugudanModel = controller.getResult() #controller(객체).get Result매서드(gugudan)의 실행 결과가 GugudnaModel객체이고, 이를 resp라는 변수에 저장하였다.
      #print(f"{resp.gugudan} = {amount} * (1 - {resp.sale})")
      
      render_html ='<h3>결과보기</h3>'
      for i in resp.result:
            print(i)
            render_html += i+ "<br/>"

      return render_template("calculator/gugudan.html", render_html = render_html)

   else:
      return render_template("calculator/gugudan.html")

@app.route('/grade', methods=["POST","GET"])
def grade():
   print("학점")
   if request.method == "POST":

      name= request.form.get('name')
      korean= request.form.get('korean') #이 세개는 라우터에서 해줘야 한다
      english= request.form.get('english')
      math= request.form.get('math')
      society= request.form.get('society')
      science= request.form.get('science')

      controller = GradeController(name=name,korean=korean,english=english,math=math,society=society,science=science) #controller에 보내는 건 3개(num1, num2,num3).....하지만, 셀프가 있다는 건 알고있어야한다. 근데 셀프는 보내는 건 아니다.
      resp : GradeModel = controller.getResult() #여기에서 getresult 안에 self가 포함되어 있다. 그런데 여기에서 self라고 쓰면 안된다. 왜냐하면 여기는 라우터이고, 라우터 셀프이기 때문에.....

      render_html ='<h3>결과 보기</h3>'
      render_html += f"{resp.name}님의 학점은 {resp.result}입니다."

      print(f"{resp.name}님의 학점은 {resp.result}입니다.")

      print("😎플러스 성공")
      return render_template("grade/grade.html", render_html = render_html)
   else: #return은 전 단계로 돌린다는 뜻이다. 80번 줄에서 resp는 CalcModel을 resp로 닉네임을 붙여줬다. 근데 윗줄에 보면 num1은 resp안에 있는 num1을 불러왔으니까....num1 = resp.num1이라는 걸 불ㄹ온ㄴ 것이다.
      return render_template("grade/grade.html")





@app.route('/calc', methods=["POST","GET"])
def calc():
   print("계산기")
   if request.method == "POST":

      num1= request.form.get('num1') #이 세개는 라우터에서 해줘야 한다
      num2= request.form.get('num2')
      opcode= request.form.get('opcode')
      eq = "="

      controller = CalcController(num1=num1,num2=num2,opcode=opcode) #controller에 보내는 건 3개(num1, num2,num3).....하지만, 셀프가 있다는 건 알고있어야한다. 근데 셀프는 보내는 건 아니다.
      resp : CalcModel = controller.getResult() #여기에서 getresult 안에 self가 포함되어 있다. 그런데 여기에서 self라고 쓰면 안된다. 왜냐하면 여기는 라우터이고, 라우터 셀프이기 때문에.....

      render_html ='<h3>결과 보기</h3>'
      render_html += f"{resp.num1} {resp.opcode} {resp.num2} {eq} {resp.result}"

      print(f"{resp.num1} {resp.opcode} {resp.num2} = {resp.result}")
      print("😎플러스 성공")
      return render_template("calculator/calc.html", num1 = resp.num1, opcode = resp.opcode, num2 = resp.num2, result = resp.result, render_html = render_html)
   else: #return은 전 단계로 돌린다는 뜻이다. 80번 줄에서 resp는 CalcModel을 resp로 닉네임을 붙여줬다. 근데 윗줄에 보면 num1은 resp안에 있는 num1을 불러왔으니까....num1 = resp.num1이라는 걸 불ㄹ온ㄴ 것이다.
      return render_template("calculator/calc.html")
                           
@app.route('/login',methods=["POST"]) #라우팅(데이터를 전송하는 방법) 과정
def login(): #함수가 실행될 때 로그인 처리를 담당, 사용자가 로그인 정보를 입력하고 제출하면, Flask가 login() 함수를 실행
   username= request.form.get('username') #input
   password= request.form.get('password') #input
   print("😁로그인 알고리즘")

   controller = LoginController(username=username,password=password)
   resp:LoginModel = controller.getResult()
 
   
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