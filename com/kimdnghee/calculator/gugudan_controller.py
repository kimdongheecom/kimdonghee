

from com.kimdnghee.calculator.gugudan_model import GugudanModel
from com.kimdnghee.calculator.gugudan_service import GugudanService


class GugudanController:
    def __init__(self,**kwargs): #kwargs는 변수의 순서 상관없이 위험성을 줄이기 위해 한 것이다.
      print("🙂dan :", kwargs.get("dan")) #kwargs["num1"] = num1(라우터 소속.....)
      self.dan = int(kwargs.get("dan"))

    def getResult(self) -> GugudanModel: #getresult에서 self하나가 있었다/..여기서 ctrl+클릭을 하면 원래 getresult로 간다.여기서 셀프는 컨트롤러 셀프이다.
        gugudan = GugudanModel() #구구단모델은 속성을 말한다. 즉 값을 말한다. 그래서 구구단은 값이다. 
        gugudan.dan = self.dan #
        
        service = GugudanService() #컨트롤러는 서비스에 전달한다...... # service안에 구구단 모델의 값인 구구단을 넣어서 실행한ㄷ.......
        return service.execute(gugudan) 