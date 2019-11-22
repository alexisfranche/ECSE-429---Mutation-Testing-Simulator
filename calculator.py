

class Calculator():

    def operation1(self, a, b):
        return a - b

    def operation2(self, a, b):
        result = self.operation1(self, a, b) + 10
        return result

    def operation3(self, a, b):
        result = self.operation2(self, a, b) / 8
        return result

    def operation4(self, a, b):
        result = self.operation3(self, a, b) * 4
        # original code returns 4
        return result