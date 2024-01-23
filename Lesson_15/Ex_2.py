'''Create a Python class representing a basic calculator with methods for addition,
subtraction, multiplication, and division.'''


class Calculator:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def addition(self):
        return self.num_1 + self.num_2

    def subtraction(self):
        return self.num_1 - self.num_2

    def multiplication(self):
        return self.num_1 * self.num_2

    def division(self):
        return self.num_1 / self.num_2
