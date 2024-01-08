class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    def __get__salary(self):
        return super().get_salary() + self.__bonus

Employee.cls_information()