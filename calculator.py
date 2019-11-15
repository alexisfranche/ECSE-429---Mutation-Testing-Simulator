
class Calculator():

    def operation1(self):
        return 1 - 3

    def operation2(self):
        result = self.operation1() + 10
        return result

    def operation3(self):
        result = self.operation2() / 8
        return result

    def operation4(self):
        result = self.operation3() * 4
        # original code returns 4
        return result