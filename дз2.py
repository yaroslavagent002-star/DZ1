# Завдання 1: Клас Car
class Car:
    def __init__(self, make, model, year):
        self.make = make        # Марка автомобіля
        self.model = model      # Модель автомобіля
        self.year = year        # Рік випуску

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"



my_car = Car("Toyota", "Corolla", 2020)
print(my_car.get_info())


# Завдання 2
class Employee:
    def __init__(self, name, position, salary):
        self.name = name            # Ім'я працівника
        self.position = position    # Посада
        self.salary = salary        # Заробітна плата

    def get_salary_info(self):
        return f"Заробітна плата {self.name}: {self.salary}"



employee1 = Employee("Давид", "Програміст", 1500)
print(employee1.get_salary_info())
