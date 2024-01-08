from abc import ABC, abstractclassmethod, abstractmethod


class Person(ABC):
    # constructor
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # abstract class
    @abstractmethod
    def get_salary(self):
        pass

    def increment_count(cls):
        pass

    @staticmethod
    def cls_information():
        pass

    # special method
    def __str__(self):
        return '-' * 40 + '\nHello' + '\nMy name is ' + self.__name + "\nI am " + str(self.__age) + " years old"


class Employee(Person):
    # class variable
    emp_count = 0

    # constructor
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary
        Employee.increment_count()

    # class method
    @classmethod
    def increment_count(cls):
        cls.emp_count += 1

    # overriding - get_salary method
    def get_salary(self):
        return self.__salary

    # overriding - static method
    @staticmethod
    def cls_information():
        print('=' * 40 + '\nClass infomation: \n- Class name: ' + str(Employee.__name__) + '\n- Base Classes: ' + str(
            Employee.__bases__) + '\n- Number of Employee: ' + str(Employee.emp_count))

    # overriding special method
    def __str__(self):
        return super().__str__() + "\nMy salary is " + str(self.__salary) + "\nMy total salary is " + str(
            self.get_salary()) + "\nMy role is Employee"


class Manager(Person):
    # class variable
    man_count = 0

    # constructor
    def __init__(self, name, age, salary, bonus):
        super().__init__(name, age)
        self.__salary = salary
        self.__bonus = bonus
        Manager.increment_count()

    # class method
    @classmethod
    def increment_count(cls):
        cls.man_count += 1

    # overriding - get_salary() method
    def get_salary(self):
        return self.__salary + self.__bonus

    # overriding - static method
    @staticmethod
    def cls_information():
        print('=' * 30 + '\nClass infomation: \n- Class name: ' + str(Manager.__name__) + '\n- Base Classes: ' + str(
            Manager.__bases__) + '\n- Number of Managers: ' + str(Manager.man_count))

    # overriding special method
    def __str__(self):
        return super().__str__() + "\nMy salary is " + str(self.__salary) + "\nBonus is " + str(
            self.__bonus) + "\nMy total salary is " + str(self.get_salary()) + "\nMy role is Management"


a = Employee("Luc Van An", 20, 10000)
b = Employee("Jang Hang Seo", 22, 23000)
print(a)
print(b)
Employee.cls_information()

c = Manager("Chien Minh Le", 25, 30000, 2000)
d = Manager("Vincenzo Cassano", 24, 27000, 2000)
print(c)
print(d)
Manager.cls_information()
