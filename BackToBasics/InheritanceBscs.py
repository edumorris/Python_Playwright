from OOPBasics import Calculator

class Adder(Calculator):
    summer = 5

    def __init__(self):
        super().__init__(10, 20)

    def add(self):
        return self.y + self.x + self.summer

if __name__ == '__main__':
    adder = Adder()

    print(adder.add())