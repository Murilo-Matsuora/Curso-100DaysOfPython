def add(*args):
    total_sum = 0
    for n in args:
        total_sum += n
    return total_sum

def calculte(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]

    return n

class Car:
    def __init__(self, **kwargs):
        self.model = kwargs.get("model")
        self.brand = kwargs.get("brand")

print(add(1, 2, 3))

print(calculte(2, add=3, multiply=6))

c = Car(model="HB20")
print(c.brand)
