class CarManager:
    all_cars = []
    total_cars = 0

    def __init__(self, make, model, year, mileage, services = []):
        #update total_cars and create an id for this car
        self._id = CarManager.total_cars
        CarManager.total_cars += 1
        
        #update all cars
        CarManager.all_cars.append(self)
        self.make = make
        self.model = model
        # self.year = _year
        # self.mileage = _mileage
        self.services = services

    def __repr__(self):
        return f"ID {self._id} | Make {self.make} | Model {self.model}"
      
    def add_service(self, service):
        self._services.append(service)   

    

print("total cars: " + str(CarManager.total_cars))
car1 = CarManager("Honda", "Civic")
print(car1._id)
print(CarManager.all_cars)

print("total cars: " + str(CarManager.total_cars))
car2 = CarManager("Jeep", "Wrangler")
print(car2._id)
print(CarManager.all_cars)