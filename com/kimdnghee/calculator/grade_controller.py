
from com.kimdnghee.calculator.grade_model import GradeModel
from com.kimdnghee.calculator.grade_service import GradeService


class GradeController:
    def __init__(self,**kwargs):
      print("🙂name :", kwargs.get("name")) #kwargs["num1"] = num1(라우터 소속.....)
      print("😮korean :", kwargs.get("korean"))
      print("😎english :", kwargs.get("english"))
      print("🙂math :", kwargs.get("math")) #kwargs["num1"] = num1(라우터 소속.....)
      print("😮society :", kwargs.get("society"))
      print("😎science :", kwargs.get("science"))
      self.name = kwargs.get("name")
      self.korean = int(kwargs.get("korean"))
      self.english = int(kwargs.get("english"))
      self.math = int(kwargs.get("math"))
      self.society = int(kwargs.get("society"))
      self.math = int(kwargs.get("math"))
      self.science = int(kwargs.get("science"))
    
    def getResult(self) -> GradeModel:
       grade = GradeModel()
       grade.name = self.name
       grade.korean = self.korean
       grade.english = self.english
       grade.math = self.math
       grade.society = self.society
       grade.math = self.math
       grade.science = self.science 
       service = GradeService() #여기에서 컨트롤러가 서비스에게 grade라는 상자 속에 각각의 이름들(예: name, korean, english 등)을 보낸다.

       return service.execute(grade) #컨트롤러를 다녀오고 나서 진행되어야 한다.....이 반환은 나중에 어디로 보내야 할까?
     #반환은 호출된 곳으로 보내면 된다.



      