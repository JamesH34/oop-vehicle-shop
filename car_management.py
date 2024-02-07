class CarManager:
   all_cars = []
   total_cars = 0

   def __init__(self, make, model, year, mileage, services = []):
      self._id = CarManager.total_cars
      self._make = make
      self._model = model
      self._year = year
      self._mileage = mileage
      self._services = services
      CarManager.total_cars += 1
      CarManager.all_cars.append(self)
    
   def __str__(self):
      return f"ID: {self._id} | Make: {self._make} | Model: {self._model} | Year: {self._year}| Mileage: {self._mileage} | Services: " + ", ".join(self._services)
   
   def add_car():
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = int(input("Enter car year: "))
    mileage = int(input("Enter car mileage: "))
    services = input("Enter services (comma-separated): ").split(",")
    CarManager(make, model, year, mileage, services)
    print("Car added successfully!")

   def view_all_cars():
    print("\nAll Cars:")
    for car in CarManager.all_cars:
        print(car)

   def view_total_cars():
        print(f"\nTotal number of cars: {CarManager.total_cars}")


   def see_car_details():
    car_id = int(input("Enter car ID: "))
    for car in CarManager.all_cars:
        if car._id == car_id:
            print(car)
            return
    print("Car not found!")

   def service_car():
    car_id = int(input("Enter car ID: "))
    for car in CarManager.all_cars:
        if car._id == car_id:
            service = input("Enter service: ")
            car._services.append(service)
            print("Service added successfully!")
            return
    print("Car not found!")

   def update_mileage():
    car_id = int(input("Enter car ID: "))
    for car in CarManager.all_cars:
        if car._id == car_id:
            new_mileage = int(input("Enter new mileage: "))
            car._mileage = new_mileage
            print("Mileage updated successfully!")
            return
    print("Car not found!")

   def main():
    print("---- WELCOME ----")
    while True:
        print("\n1. Add a car\n2. View all cars\n3. View total number of cars\n4. See a car's details\n5. Service a car\n6. Update mileage\n7. Exit to terminal")
        choice = input("Enter your choice: ")

        if choice == '1':
            CarManager.add_car()
        elif choice == '2':
            CarManager.view_all_cars()
        elif choice == '3':
            CarManager.view_total_cars()
        elif choice == '4':
            CarManager.see_car_details()
        elif choice == '5':
            CarManager.service_car()
        elif choice == '6':
            CarManager.update_mileage()
        elif choice == '7':
            print("Thank you for using the car management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    CarManager.main()

   



car1 = CarManager("Toyota", "Camry", 2020, 15000, ["Oil Change", "Tire Rotation"])
car2 = CarManager("Honda", "Civic", 2005, 120000, ["Brake Fluid"])


print("\nAll cars:")
for car in CarManager.all_cars:
    print(car)

  