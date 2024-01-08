class Person:
    count = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.increment_count()

    @classmethod
    def increment_count(cls):
        cls.count += 1
    def greeting():
        print("-----Hello-----")

    @staticmethod
    def cls_information():
        print('=' * 40 +
              '\n Class information: \n- Class name: ' + str(Person.__name__) +
              '\n- Base Classes: ' + str(Person.__base__) +
              '\n- Number of Person: ' + str(Person.count) +
              '\n' + '=' * 40)

    def __str__(self):
        return 'My name is ' + self.__name + "\nI am " + str(self.__age) + " years old"


a = Person("An", 19)
print(a)
greeting()

b = Person("Lục Văn An", 20)
print(b)
greeting()

Person.cls_information()


class Employee(Person):
    emp_count = 0

    def __init__(self, name, age, salary, role=None):
        super().__init__(name, 0)
        super().__init__(name, age)
        self._salary = salary
        if role is None:
            self._role = "EMPLOYEE"
        else:
            self._role = role
        Employee.increment_count()

    @classmethod
    def increment_count(cls):
        cls.emp_count += 1

    def _get_salary(self):
        return super()._get_salary() + self._bonus

    @staticmethod
    def cls_information():
        print('=' * 40 +
              '\n Class information: \n- Class name: ' + str(Employee.__name__) +
              '\n- Base Classes: ' + str(Employee.__base__) +
              '\n- Number of Employee: ' + str(Employee.count) +
              '\n- Number of Person: ' + str(Person.count) +
              '\n' + '=' * 40)

    def __str__(self):
        return ('My name is ' + self.__name +
                "\nI am " + str(self.__age) + " years old" +
                "\nMy salary is " + str(self._salary) +
                "\nMY ROLE IS " + str(self._role))


c = Employee("Chien Le Minh", 19, 15000)
print(c)
greeting()

d = Employee("Ngô Bá Khá", 29, 250000)
print(d)
greeting()

Employee.cls_information()
