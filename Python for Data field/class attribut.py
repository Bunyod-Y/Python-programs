class Car:
    def __init__(self, model, year, color, for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale

car1=Car("Toyota", 2025, "Red", False)

print(car1.model, car1.year)