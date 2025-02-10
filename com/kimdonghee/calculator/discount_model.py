from dataclasses import dataclass #data를 클레스로 만드는 것이다. 클래스 만든다는 것은 데이터를 객체로 만든다는 것이다.

@dataclass 
class DiscountModel: 
    train : object 
    test : object
    context : str # 경로를 주는 코드이다..
    #num1 :int 즉, 기계(인터프리터)가 초기화시킬 것이다.
    fname :str # =''는 파일명을 주는 코드이다.
    id : str #즉, id = ' '로 변환시키겠다는 의미이다. 아이디와 라벨은 정해져 있다. 답(생존여부)을 라벨이라고 한다.
    label : str #str은 문자열로 변환시키느 것이다. 지금 모든 작업이 다 이니셜라이징(초기화, 즉 이름 붙이는 작업)이다.

    @property # 위에 있는 문자열로 변환한 변수(property)를
    def train(self) -> object:
        return self._train                          #자기 자신을 읽는 과정.읽기 과정
    
    @train.setter #setter는 쓰고 설정하다라는 의미이다. 
    def train(self, train):
        self._train = train                         #자기 자신을 쓰는 과정. 쓰기 과정
    
    @property # 위에 있는 문자열로 변환한 변수(property)를
    def test(self) -> object:           #-> (리턴 타입) 결과값을 오브젝트에 줘,,,라는 의미이다.....
        return self._test                          #자기 자신을 읽는 과정.읽기 과정 즉, 내가 송금한 걸 잘 됬는지 보는 것을 의미하는 것....
    
    @test.setter #setter는 쓰고 설정하다라는 의미이다. 
    def test(self, test):
        self._test = test                         #자기 자신을 쓰는 과정. 쓰기 과정, 즉, 내가 송금하는 것,,,, #setter과정(쓰기 과정)과 getter과정(읽기 과정)은 한 묶음이다. setter

    @property
    def context(self) -> object:         
        return self._context                   
    
    @context.setter 
    def context(self, context):
        self._context = context

    @property
    def fname(self) -> object:         
        return self._fname                   
    
    @fname.setter 
    def fname(self, fname):
        self._fname = fname

    @property
    def id(self) -> object:         
        return self._id                   
    
    @id.setter 
    def id(self, id):
        self._id = id
    
    @property
    def label(self) -> object:         
        return self._label                   
    
    @label.setter 
    def label(self, label):
        self._label = label

    
# csv파일을 객체로 만드는 클래스 만드는 작업
# 데이터를 품고있는 상태
# csv에서 데이터 데이터 셋에 가져오는 것/////
# 클래스인데 데이터를 글고 오니까 데이터 클래스라고 한다.