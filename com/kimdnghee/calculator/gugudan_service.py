from com.kimdnghee.calculator.gugudan_model import GugudanModel


class GugudanService:
    def __init__(self):
        pass


    def execute(self, gugudan: GugudanModel)-> GugudanModel: #execute를 실행하면, 구구단 값이 원래 있던 곳으로 반환된다..... 
        
        gugudan.result = []
        for i in range(1, 10):
            gugudan.result.append(f"{gugudan.dan} x {i} = {gugudan.dan * i}")

        return gugudan