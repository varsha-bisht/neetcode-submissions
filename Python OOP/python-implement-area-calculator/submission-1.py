import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length, width=None):
        if width != None:
            area = length * width
            return area
        area = math.pi * (length*length)
        return round(area, 2)
    
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
