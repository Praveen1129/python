class Vehicle:
    def _init_(self, brand, model, year):
        self.__brand = brand  
        self.__model = model  
        self.__year = year  

   
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    
    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def displayInfo(self):
        print(f"{self._brand}, {self.model}, {self._year}")


class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super()._init_(brand, model, year)
        self.__fuel_type = fuel_type

    def get_fuel_type(self):
        return self.__fuel_type

   
    def set_fuel_type(self, fuel_type):
        self.__fuel_type = fuel_type

    def displayInfo(self):
        print(f"{self.get_brand()}, {self.get_model()}, {self.get_year()}, Fuel: {self.__fuel_type}")

    def startEngine(self):
        print(f"The {self.get_brand()} {self.get_model()}  car starts with a engine sound!")


class Bike(Vehicle):
    def  __init__(self, brand, model, year, engine_capacity):
        super()._init_(brand, model, year)
        self.__engine_capacity = engine_capacity 

    
    def get_engine_capacity(self):
        return self.__engine_capacity

    def set_engine_capacity(self, engine_capacity):
        self.__engine_capacity = engine_capacity

    def displayInfo(self):
        print(f"{self.get_brand()}, {self.get_model()}, {self.get_year()}, Engine: {self.__engine_capacity}")

    def startEngine(self):
        print(f"The {self.get_brand()} {self.get_model()} starts widely with {self.__engine_capacity} engine sound and gets hi chinnu.")



car = Car("Toyota", "Corolla", 2015, "Petrol")
bike = Bike("YAMAHA", "mt15", 2024, "155cc")

car.displayInfo()
car.startEngine()

bike.displayInfo()
bike.startEngine()