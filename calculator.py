

class Calculator():

    def operation1(self, num1, num2):
        return num1 - num2

    def operation2(self, returned_num1, num3):
        result =  returned_num1 + num3
        return result

    def operation3(self, returned_num2, num4):
        result = returned_num2 / num4
        return result

    def operation4(self, returned_num3, num5):
        result = returned_num3 * num5       
        return result

    def use_calculator(self, num1, num2, num3, num4, num5):

        returned_num1 = self.operation1(num1, num2)
        returned_num2 = self.operation2(returned_num1, num3)
        returned_num3 = self.operation3(returned_num2, num4)
        result = self.operation4(returned_num3, num5)

        return result


#Hardcoded test to see if this works -- To be removed before submission
#num1 = 1
#num2 = 3
#num3 = 10
#num4 = 8
#num5 = 4

#my_calculator = Calculator()
#This should return 4
#print(my_calculator.use_calculator(num1, num2, num3, num4, num5))
