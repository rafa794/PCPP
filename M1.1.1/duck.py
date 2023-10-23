class Duck:
    def __init__(self, height, weight, sex):
        self.height = height,
        self.weight = weight,
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print("Quack!")

duckling = Duck(height = 10, weight=3.4, sex= "male")
drake = Duck(height = 25, weight=3.7, sex= "male")
hen = Duck(height = 20, weight=3.4, sex= "female")

print("El Duck.__class__", Duck.__class__)
print("El duckling.__class__", duckling.__class__)
print("El duckling.sex.__class__", duckling.sex.__class__)
print("El duckling.quack.__class__", duckling.quack.__class__)