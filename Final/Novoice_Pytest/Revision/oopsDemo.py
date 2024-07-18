class Calculator:
    num = 100
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("I am automatically called when object is created")
    def getData(self):
        print("I am now now executing as a method in class")
    def sumation(self):
        return self.a+self.b+Calculator.num
