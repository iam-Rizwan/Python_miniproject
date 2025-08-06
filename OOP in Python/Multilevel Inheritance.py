class Vehicle:
    def start_engine(self):
        return "Engine started"
class Car(Vehicle):
    def drive(self):
        return "Car is in motion"
class SportsCar(Car):
    def race(self):
        return "Sports car racing at high speed"
sports_car = SportsCar()
print(sports_car.start_engine()) 
print(sports_car.drive()) 
print(sports_car.race())