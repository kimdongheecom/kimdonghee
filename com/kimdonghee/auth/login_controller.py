from com.kimdonghee.auth.login_model import LoginModel
from com.kimdonghee.auth.login_service import LoginService


class LoginController:
    def __init__(self):
        pass

    def getResult(self, login:LoginModel) -> LoginModel:  #login:LoginModel 파라미터 -> LoginModel 나가는 값:
        service = LoginService()
        return service.execute(login)