# class car:
#     def __init__(self, brand, model):
#         self.brand=brand
#         self.model=model
#     def display(self):
#         print("The car brand is: ",self.brand,"The car is: ",self.model)
# car_obj=car("Lamborghini", "Avendator SVJ")
# car_obj.display()

# class Employee:
#     def __init__(self, name, salary):
#         self.__name=name
#         self.__salary=salary
    
#     def set_salary(self, salary):
#         self.__salary=salary
    
#     def get_salary(self):
#         return self.__salary
    
#     def salary_deduction(self):
#         print("")

# emp=Employee("Sathwik", 10000)
# print("Salary before update",emp.get_salary())
# employee_salary_deduction=emp.get_salary()
# salary_deduction=employee_salary_deduction-(employee_salary_deduction*0.5)
# print("Salary after deduction: ",salary_deduction)
# employee_get_salary=input("ENter the salary: ")
# emp.set_salary(employee_get_salary)
# print("salary after update: ",emp.get_salary())


# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
    
#     def set_salary(self,salary):
#         self.salary=salary
        
#     def get_salary(self):
#         return self.salary
    
#     def allowance(self,allowances):
#         food_allowance=allowances*0.08
#         travel_allowance=allowances*0.1
#         self.salary=allowances+food_allowance+travel_allowance
#         return self.salary
#     def deduction(self,amount):
#         self.salary=amount-amount*0.05
#         return self.salary
    
# def main():
#     employee_details=Employee(input("Enter the name: "),int(input("Enter the salary: ")))
#     print("Salary before deduction: ",employee_details.get_salary())
#     allowances=employee_details.allowance(employee_details.get_salary())
#     deductions=employee_details.deduction(allowances)
#     print("Salary after deductions: ",deductions)
# main()


#Constructor
# class Parent:
#     def __init__(self):
#         self.height="160cm"
#         # self.display_parent()
#     def display_parent(self):
#         print("This is the parent class")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
        
# child=Child()
# child.display_parent()


#Constructor with static variable
# class Static_variable:
#     def __init__(self):
#         self.__name="sathwik"
#     def display(self):
#         print(self.__name)
# asd=Static_variable()
# asd.display()


#polymorphism
# class Porsche:
#     def air_flow(self):
#         print("Turbo Charger")
# class Dodge:
#     def air_flow(self):
#         print("Super charger")
        
# list_of_item=[Porsche(), Dodge()]
# for car in list_of_item:
#     car.air_flow()
#polymorphism end


# class Example:
#     def __init__(self, name):
#         print(f"First constructir: Hello {name}")
        
#     def __init__(self, age):
#         print(f"Second constructor: Age is {age}")
        
# obj=Example(15) #Calls only the second constructor
#even if 
# class Example:
#     def __init__(self, *args):
#         if len(args) == 1:
#             print(f"Hellow {args[0]}")
#         elif len(args) == 2:
#             print(f"Hellow {args[0]}, you are {args[1]} years old")


# class Example:
#     def __init__(self, studentName, **kwargs):
#         self.studentName=studentName
#         if "name" in kwargs and "age" in kwargs:
#             print(f"Hellow {kwargs['name]}, you")
            
            
# class DestructorExample:
#     def __init__(self, name):
#         self.name=name
#         print(f"Object {self.name} is created")
        
#     def __del__(self):
#         print(f"Object {self.name} is destroyed")

# obj=DestructorExample("Try")
# del obj


# class Bird:
#     def fly(self):
#         return "This bird can fly"

# class Mammal:
#     def walk(self):
#         return "This mammal can walk"
    
# class Bat(Bird, Mammal):
#     pass

# bat=Bat()
# print(bat.fly())
# print(bat.walk())
# m1=Mammal()
# m1=Bat()
# print(m1.walk())


#HeirarchicalInterface
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14*self.radius**2

class Square(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    
