from com.kimdnghee.calculator.calc_model import CalcModel


class CalcService:
    def __init__(self):
        pass

    def execute(self,calc: CalcModel) -> CalcModel : #app에서 가져온 것을 service인 여기에다가 줬다. #CalcModel에서 정해진 값이 타입에 따라 출력되겠다.여기서 x값은 calc이다.  
        num1 = calc.num1 #controller에서 가져온 calc라는 밖스를 풀었다.....
        num2 = calc.num2
        opcode = calc.opcode
        if opcode == '+' : #이건 로직이라 도메인에 들어가야한다...이건 기능이니까 서비스에 들어가야 한다. 도메인에서는 메쏘드를 만들어야 한다.
         result = int(num1) + int(num2)
        elif opcode == '-' :
         result = int(num1) - int(num2)
        elif opcode == '*' :
         result = int(num1) * int(num2)
        elif opcode == '/' :
         result = int(num1) / int(num2)
        else:
         result = "연산자가 잘못되었음"
        
        calc.result = result #calc라는 밖스 안에 result를 app.py에 다시 보낸다.
        
        return calc