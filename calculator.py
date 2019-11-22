

class Calculator():

    def subtract(self, num1, num2):
        result = num1 - num2
        return result

    def add(self, returned_num1, num3):
        result = returned_num1 + num3
        return result

    def divide(self, returned_num2, num4):
        result = returned_num2 / num4
        return result

    def multiply(self, returned_num3, num5):
        result = returned_num3 * num5       
        return result

    def use_calculator(self, num1, num2, num3, num4, num5):
        returned_num1 = self.operation1(self, num1, num2)
        returned_num2 = self.operation2(self, returned_num1, num3)
        returned_num3 = self.operation3(self, returned_num2, num4)
        result = self.operation4(self, returned_num3, num5)

        return result


