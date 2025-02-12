
from typing import Self
from com.kimdnghee.calculator.discount_model import DiscountModel
from com.kimdnghee.calculator.discount_service import DiscountService


class DiscountController: #csv파일을 가져와서 다음 일을 하는 과정이다.

    def __init__(self, amount): # (1)amount는 html에서 나온 값이다.
        self.amount = amount #(2)내 안에 amount라는 변수를 만들었다라는 것을 의미함. amount라고 했다.

    def getResult(self) -> DiscountModel: #(3)
        service = DiscountService()
        discount = DiscountModel
        discount.amount = self.amount
        return service.execute(discount)