from dataclasses import dataclass #data를 클레스로 만드는 것이다. 클래스 만든다는 것은 데이터를 객체로 만든다는 것이다.

@dataclass 
class DiscountModel: 
    amount : int 
    result : str

    @property
    def amount(self) -> object:
        return self._amount                          
    
    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property 
    def result(self) -> object:
        return self._result                         
    
    @result.setter 
    def sale(self, result):
        self._result = result                         

                    