
from com.kimdnghee.auth.login_model import LoginModel
from com.kimdnghee.auth.login_service import LoginService



class LoginController:
    def __init__(self,**kwargs):
    
        print("😉username:", kwargs.get("username"))
        print("🙄passworld:", kwargs.get("password"))
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")



    def getResult(self) -> LoginModel:  #login:LoginModel 파라미터 -> LoginModel 나가는 값:
        service = LoginService()
        login = LoginModel()
        login.username = self.username
        login.password = self.password
        return service.execute(login)