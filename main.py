from abc import ABC, abstractmethod


# Задание 1.
# Реализуйте архитектуру приложения, используя паттерн «Фабричный
# метод».
# Представьте, что вы создали программу управления доставкой еды. В
# программе в качестве единственного средства доставки используется электросамокат.
# Ваши курьеры на электро-самокатах развозят еду из пункта А в
# пункт Б. Все просто.
# Программа набирает популярность и ваш бизнес растет. Парк самокатов
# ограничен и вы решаете подключить к вашей системе доставки велосипеды и
# автомобили. Вам важно знать когда будет доставлена еда и сколько единиц
# продуктов может забрать курьер. У транспортных средств разная скорость и
# вместимость.

class Transport(ABC):
    __speed = None
    __max_capacity = None

    @abstractmethod
    def speed(self):
        raise NotImplementedError

    @abstractmethod
    def max_capacity(self):
        raise NotImplementedError

    @abstractmethod
    def deliver(self):
        raise NotImplementedError


class ElectricScooter(Transport):
    __speed = 30
    __max_capacity = 4

    @property
    def speed(self):
        return self.__speed

    @property
    def max_capacity(self):
        return self.__max_capacity

    def deliver(self):
        print(
            f"Доставка еды транспортом типа Электросамокат"
            f", скорость - {self.__speed}, вместимость - {self.__max_capacity}")


class Bicycle(Transport):
    __speed = 20
    __max_capacity = 3

    @property
    def speed(self):
        return self.__speed

    @property
    def max_capacity(self):
        return self.__max_capacity

    def deliver(self):
        print(f"Доставка еды транспортом типа Велосипед,"
              f" скорость - {self.__speed}, вместимость - {self.__max_capacity}")


class Car(Transport):
    __speed = 100
    __max_capacity = 22

    @property
    def speed(self):
        return self.__speed

    @property
    def max_capacity(self):
        return self.__max_capacity

    def deliver(self):
        print(f"Доставка еды транспортом типа Автомобиль"
              f", скорость - {self.__speed}, вместимость - {self.__max_capacity}")


class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        raise NotImplementedError


class ScooterLogistic(Logistics):
    def create_transport(self):
        return ElectricScooter()


class BicycleLogistic(Logistics):
    def create_transport(self):
        return Bicycle()


class CarLogistic(Logistics):
    def create_transport(self):
        return Car()