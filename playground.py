
def add(*args):
    s = " + ".join([str(n) for n in args]) + " = " + str(sum(args))
    print(s)
    
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


class Car():
    
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

        


add(1, 2, 3, 4, 5, 6, 7, 8, 9)
calculate(2, add=3, multiply=5)

new_car = Car()