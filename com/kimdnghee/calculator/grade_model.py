from dataclasses import dataclass

@dataclass
class GradeModel: 
    name : str #int로 들어오게 하려고 저렇게 하고......
    korean : int
    english : int 
    math : int
    society : int 
    science : int
    result : str #result를 쓰는 이유는 서비스에서 연산을 하는 과정이 있으니까 리저트가 나오니까......그래서 먼저 리저트를 먼저 선언해주기....

    @property 
    def name(self) -> str:
        return self._name                       
    
    @name.setter 
    def name(self, name):
        self._name = name                         
    
    @property 
    def korean(self) -> int:           
        return self._korean                          
    
    @korean.setter 
    def korean(self, korean):
        self._korean = korean                         

    @property
    def english(self) -> int:         
        return self._english                 
    
    @english.setter 
    def english(self, english):
        self._english = english
    
    @property
    def math(self) -> int:         
        return self._math                 
    
    @math.setter 
    def math(self, math):
        self._math = math
    
    @property 
    def society(self) -> int:           
        return self._society                          
    
    @society.setter 
    def society(self, society):
        self._society = society                         

    @property
    def science(self) -> int:         
        return self._science                 
    
    @science.setter 
    def science(self, science):
        self._science = science
    
    @property
    def result(self) -> str:         
        return self._result                 
    
    @result.setter 
    def result(self, result):
        self._result = result
    
