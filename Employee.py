class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, age, salary):
        employee = Employee(name, age, salary)
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(f"{employee.name} - Age: {employee.age} - Salary: {employee.salary}")

    def delete_by_age(self, age):
        self.employees = [employee for employee in self.employees if employee.age != age]

    def update_salary_by_name(self, name, salary):
        for employee in self.employees:
            if employee.name == name:
                employee.salary = salary


class FrontendManager:
    def __init__(self):
        self.employees_manager = EmployeesManager()

    def run(self):
        while True:
            print("\nPlease choose an option:")
            print("1. Add new employee")
            print("2. Print all employees")
            print("3. Delete by age")
            print("4. Update Salary by name")
            print("5. End the program")

            try:
                choice = int(input("\nEnter your choice: "))

                if choice == 1:
                    name = input("Enter name: ")
                    age = int(input("Enter age: "))
                    salary = float(input("Enter salary: "))
                    self.employees_manager.add_employee(name, age, salary)
                elif choice == 2:
                    self.employees_manager.print_employees()
                elif choice == 3:
                    age = int(input("Enter age to delete: "))
                    self.employees_manager.delete_by_age(age)
                elif choice == 4:
                    name = input("Enter name to update salary: ")
                    salary = float(input("Enter new salary: "))
                    self.employees_manager.update_salary_by_name(name, salary)
                elif choice == 5:
                    break
                else:
                    print("Invalid choice. Please enter a number from 1 to 5.")
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    frontend_manager = FrontendManager()
    frontend_manager.run()