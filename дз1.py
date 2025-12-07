class Car:
    def __init__(self, brand):
        self.brand = "Toyota"
        self.speed = 56

    def accelerate(self, amount):
        self.speed += amount
        print(f"{self.brand} прискорився на {amount} км/год.")

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 15
        print(f"{self.brand} пригальмував на {amount} км/год.")

    def show_speed(self):
        print(f"Поточна швидкість {self.brand}: {self.speed} км/год.")
