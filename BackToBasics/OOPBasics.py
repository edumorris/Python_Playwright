class Calculator():
    multiplier = 7

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def multiply(self):
        return self.x * self.y

if __name__ == '__main__':
    calculator = Calculator(10, 20)
    print(calculator.multiply())