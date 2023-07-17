from abc import ABC, abstractmethod

class CarFactory(ABC):
    @abstractmethod
    def create_sedan_car(self):
        print("автомобиль седан создан")

    @abstractmethod
    def create_coupe_car(self):
        print("автомобиль купе создан")


class ToyotaFactory(CarFactory):
    def create_sedan_car(self):
        print("Произведён автомобиль - ToyotaSedan")

    def create_coupe_car(self):
        print("Произведён автомобиль - ToyotaCoupe")


class FordFactory(CarFactory):
    def create_sedan_car(self):
        print("Произведён автомобиль - FordSedan")

    def create_coupe_car(self):
        print("Произведён автомобиль - FordCoupe")
def execute_application():
    # Тойота
    toyota_factory = ToyotaFactory()
    toyota_factory.create_sedan_car()
    toyota_factory.create_coupe_car()
    # Форд
    ford_factory = FordFactory()
    ford_factory.create_sedan_car()
    ford_factory.create_coupe_car()


if __name__ == "__main__":
    execute_application()