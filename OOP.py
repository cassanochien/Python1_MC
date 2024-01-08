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
        print( '='*40+'\nClass infomation: \n- Class name: '+str(Employee.__name__)+
            '\n- Base Classes: '+str(Employee.__bases__)+
            '\n- Number of Employee: ,→ '+str(Employee.emp_count)+
            '\n- Number of Person: '+str(Person.count)+'\n'+'='*40)
# overriding special method
    def __str__(self):
        return super().__str__()+"\nMy salary is "+str(self.__salary)+"\nMY ROLE , →IS EMPLOYEE"
c = Employee("C", 21, 600)
d = Employee("D", 20, 650)
c.greeting()
print(c)
d.greeting()
print(d)
Employee.cls_information()