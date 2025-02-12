from com.kimdnghee.calculator.calc_model import CalcModel
from com.kimdnghee.calculator.calc_service import CalcService


class CalcController:
    def __init__(self,**kwargs): #kwargs는 변수의 순서 상관없이 위험성을 줄이기 위해 한 것이다.
      print("🙂num1 :", kwargs.get("num1")) #kwargs["num1"] = num1(라우터 소속.....)
      print("😮num2 :", kwargs.get("num2"))
      print("😎opcode :", kwargs.get("opcode"))
      self.num1 = int(kwargs.get("num1"))
      self.num2 = int(kwargs.get("num2"))
      self.opcode = kwargs.get("opcode")

      

    def getResult(self) -> CalcModel: #getresult에서 self하나가 있었다/..여기서 ctrl+클릭을 하면 원래 getresult로 간다.여기서 셀프는 컨트롤러 셀프이다.
        service = CalcService()
        calc = CalcModel()
        calc.num1 = self.num1 
        calc.num2 = self.num2 #라우터에서 넘어온 외부변수를 자기변수로 만들겠다라는 의미입니다. 
        calc.opcode = self.opcode
        return service.execute(calc) #calcService를 가지고 와서....execute에 넣는다