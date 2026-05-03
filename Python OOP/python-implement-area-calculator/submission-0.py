import math

class AreaCalc:
    # TODO: Implement calculate method
    
    def calculate(self, length: int, width: int = 0) -> float:
        if width is 0:
            val = (math.pi)*length*length
            return round(val,2)
        return length*width
        

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
