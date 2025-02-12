
from flask import redirect, url_for
from com.kimdnghee.auth.login_model import LoginModel



class LoginService: #첫번째로, 먼저 만들기(controller 포함).... 모델만 다르고,
    def __init__(self):
        pass

    def execute(self,login: LoginModel) -> LoginModel: #app에서 가져온 것을 service인 여기에다가 줬다.  
        username = login.username #calc라는 밖스를 풀었다.....
        password = login.password

        if username == "kdh" and password == '1234': #이건 로직이라 도메인에 들어가야한다...이건 기능이니까 서비스에 들어가야 한다. 도메인에서는 메쏘드를 만들어야 한다.
          print("😎로그인 성공")
          result = 'home' #로그인 성공하면 home으로 간다
        else:
          print("😥로그인 실패")
          result = 'intro' #로그인 실패하면 intro로 보낸다.
        
        login.result = result

        return login

        
        
        

