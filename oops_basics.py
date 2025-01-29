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


#
class Educational_institute:
    def __init__(self):
        print("Institute here!!")
    
    def staff(self):
        print("Faculty here!!")
    def students(self):
        print("Students here!!")

class College(Educational_institute):
    def 