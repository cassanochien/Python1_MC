class Person:
    count = 0

    def __init__(self, name, age):
        self._name = name
        self._age = age
        Person.increment_count()

    @classmethod
    def increment_count(cls):
        cls.count += 1
     # instance method
    def greting(self):
        print("--------Hello-------")

    @staticmethod
    def cls_information():
        print('='*40 +"\nClass information: \n- Class name: " + str(Person.__name__) + '\n Base Classes: ' + str(
            Person.__bases__) + '\n- Number of Person: ' + str(Person.count) + '\n' + '='*40)
    def __str__(self):
        return 'My name is ' + self._name + "\nI am " + str(self._age) + " years old"


# Example usage
person1 = Person("A", 19)
person2 = Person("B", 20)
person1.greting()
print(person1)
person2.greting()
print(person2)

Person.cls_information()


class Employee(Person):
# Class variable
  emp_count=0
# constructor
  def __init__(self, name, age, salary):
    super().__init__(name, age)
    self.__salary= salary
    Employee.increment_count()
  # class method
  @classmethod
  def increment_count(cls):
    cls.emp_count+=1
  # overriding - static method
  @staticmethod
  def cls_information():
    print( '='*40+'\nClass infomation: \n- Class name: '+str(Employee.__name__)+'\n- Base Classes: '+str(Employee.__bases__)+'\n- Number of Employee:'+str(Employee.emp_count)+'\n- Number of Person: '+str(Person.count)+'\n'+'='*40)
  # overriding special method
  def __str__(self):
    return super().__str__()+"\nMy salary is "+str(self.__salary)+'$'+"\nMY ROLE IS EMPLOYEE"
  # overriding special method
  def __str__(self):
    return super().__str__()+"\nMy salary is "+str(self.__salary)+'$'+"\nMY ROLE IS EMPLOYEE"
c = Employee("C", 21, 600)
d = Employee("D", 20, 650)
c.greting()
print(c)
d.greting()
print(d)
Employee.cls_information()

class Manager(Person):
    #Class variables
    man_count = 0
    # constructor
    def __init__(self, name,age,salary,bonus):
        super().__init__(name,age)
        self.__salary = salary
        self.__bonus = bonus
        Manager.increment_count()
    #class methods
    @classmethod
    def increment_count(cls):
        cls.man_count += 1
    # overriding - static methods
    @staticmethod
    def cls_information():
        print( '='*30 +'\nClass information: \n- Class name: '+str(Manager.__name__)+
              '\n- Base Classes: '+str(Manager.__bases__)+
              '\n- Number of Manager: '+ str(Manager.man_count))
    #overriding - special methods
    def __str__(self):
        return super().__str__()+"\nMy salary is "+str(self.__salary)+"\nBonus is "+str(self.__bonus)+ "\nMy total salary is "+str(self.get_salary())+"\nMy ROLE IS MANAGEMENT"

e = (600, 50, 650)

print(e)
Manager.cls_information()




