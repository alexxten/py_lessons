class Calculator:
    def __init__(self, variable_first: int, variable_second: int, math_operation: str):
        self.variable_first = variable_first
        self.variable_second = variable_second
        self.math_operation = math_operation

    def addition(self):
        return self.variable_first + self.variable_second

    def subtraction(self):
        return self.variable_first - self.variable_second

    def division(self):
        return self.variable_first / self.variable_second

    def multiplication(self):
        return self.variable_first * self.variable_second