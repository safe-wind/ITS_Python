
class Calculator:
    def __init__(self, a:int, b:int) -> None:
        self.a = a
        self.b = b
    
    def addiction(self) -> int:
        return int(self.a+self.b)

    def subtraction(self) -> int:
        return int(self.a-self.b)
    
    def multiplication(self) -> int:
        return int(self.a*self.b)
    
    def division(self) -> float:
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return round(self.a/self.b)