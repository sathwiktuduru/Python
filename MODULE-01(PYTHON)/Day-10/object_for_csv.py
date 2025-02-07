import csv
class Employee:
    def employee_details(self, name, id, age):
        self.name=name
        self.id=id
        self.age=age
    def get_details(self):
        return [self.name, self.id, self.age]
    
def main():
    employee_input=Employee()
    employee_input.employee_details("sathwik", 218, 21)
    file_name="employee_csv.csv"
    with open(file_name, mode="w", newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["name", "id", "age"])
        writer.writerow(employee_input.get_details())
main()
