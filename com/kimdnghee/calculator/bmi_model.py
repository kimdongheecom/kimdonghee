from dataclasses import dataclass #모델만 만든다..이 첫문장.

@dataclass
class BmiModel:
    height: float
    weight: float

    @property 
    def height(self) -> int:
        return self._height                       
    
    @height.setter 
    def height(self, height):
        self._height = height                         
    
    @property 
    def weight(self) -> int:           
        return self._weight                          
    
    @weight.setter 
    def weight(self, weight):
        self._weight = weight
