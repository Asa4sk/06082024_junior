class Car:
    def __init__(self, year, manufacturer, model, fuel_consumption):
        self.year = year
        self.manufacturer = manufacturer
        self.model = model
        self.mileage = 0
        self.fuel_consumption = fuel_consumption

    def drive(self):
        print(f"Авто марки {self.model}")

    @property
    def cost_of_service(self):
        return self.mileage * 7.6


car1 = Car(year=2020, manufacturer="Toyota", model="Corolla", fuel_consumption=6.5)
car2 = Car(year=2018, manufacturer="BMW", model="X3", fuel_consumption=8.3)
car3 = Car(year=2022, manufacturer="Tesla", model="Model S", fuel_consumption=0.0)


car1.mileage = 12000
car2.mileage = 8000

print(f"Вартість обслуговування для {car1.model}: {car1.cost_of_service} грн")


car3.drive()
