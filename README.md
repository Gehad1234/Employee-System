
 
# Employee Management System(OOP with Python)

## Description

This Python project is an Employee Management System designed to manage employee records efficiently. It provides a simple command-line interface for users to perform various operations on employee data, such as adding new employees, printing employee information, deleting employees by age, and updating salaries by name. The project is organized into three classes: `Employee`, `EmployeesManager`, and `FrontendManager`.

## Classes

### 1. Employee

The `Employee` class represents individual employees with attributes like name, age, and salary. It has a constructor method `__init__` to initialize these attributes.

### 2. EmployeesManager

The `EmployeesManager` class is responsible for managing a list of employee records. It has the following functionalities:

- `add_employee(name, age, salary)`: Adds a new employee to the list.
- `print_employees()`: Prints the details of all employees in the list.
- `delete_by_age(age)`: Deletes employees with a specific age from the list.
- `update_salary_by_name(name, salary)`: Updates the salary of an employee by name.

### 3. FrontendManager

The `FrontendManager` class serves as the user interface of the Employee Management System. It presents a menu to the user and handles their input. The available options include:

- Adding a new employee.
- Printing the details of all employees.
- Deleting employees by age.
- Updating an employee's salary by name.
- Exiting the program.

## Usage

To run the program, execute the `FrontendManager` class. It will display a menu where users can select the desired operation by entering a number. The program will continue to run until the user chooses to exit.

## Getting Started

To use this project, follow these steps:

1. Clone or download the project from GitHub.
2. Ensure you have Python installed on your system.
3. Run the `FrontendManager` class to start the Employee Management System.
4. Follow the on-screen prompts to perform various operations on employee data.

Feel free to modify and extend this project to suit your specific needs or integrate it into a larger system. Contributions and improvements are welcome!
