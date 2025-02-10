from com.kimdonghee.calculator.calc_model import CalcModel
from com.kimdonghee.calculator.calc_service import CalcService


class CalcController:
    def __init__(self):
        pass

    def getResult(self, calc:CalcModel) -> CalcModel:
        service = CalcService()
        return service.execute(calc) #calcService를 가지고 와서....execute에 넣는다