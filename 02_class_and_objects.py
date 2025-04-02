class testClass:
    pass # use pass for empty class

class addition:
    value = 'This is global variable of class'
    def add(self, a: int, b: int): #self is used to use current instance in class.
        d = a + b
        print(d)
        print(self.value)

class subtraction:
    def __init__(self, a, b): #constructor
        self.a = a
        self.b = b

    def subtract(self, a: int, b: int):
        c = b - a
        print(c)
        d = self.b - self.a
        print(d)

# creating object and function call
callAddition = addition()
callAddition.add(5, 10)

callSubtract = subtraction(13, 25)
callSubtract.subtract(10, 25)