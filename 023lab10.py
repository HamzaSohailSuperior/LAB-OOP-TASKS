import csv

class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary


class Manager(Employee):
    def __init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.__team_size = team_size

    def get_team_size(self):
        return self.__team_size

    def set_team_size(self, team_size):
        self.__team_size = team_size


class Worker(Employee):
    def __init__(self, name, age, salary, overtime_hours):
        super().__init__(name, age, salary)
        self.__overtime_hours = overtime_hours

    def get_overtime_hours(self):
        return self.__overtime_hours

    def set_overtime_hours(self, overtime_hours):
        self.__overtime_hours = overtime_hours


def save_to_csv(file_name, employees):
    headers = ["Name", "Age", "Salary", "Team Size", "Overtime Hours"]
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for employee in employees:
            if isinstance(employee, Manager):
                writer.writerow(
                    [
                        employee.get_name(),
                        employee.get_age(),
                        employee.get_salary(),
                        employee.get_team_size(),
                        None,
                    ]
                )
            elif isinstance(employee, Worker):
                writer.writerow(
                    [
                        employee.get_name(),
                        employee.get_age(),
                        employee.get_salary(),
                        None,
                        employee.get_overtime_hours(),
                    ]
                )


def load_from_csv(file_name):
    employees = []
    try:
        with open(file_name, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Team Size"]:
                    employees.append(
                        Manager(
                            row["Name"],
                            int(row["Age"]),
                            float(row["Salary"]),
                            int(row["Team Size"]),
                        )
                    )
                elif row["Overtime Hours"]:
                    employees.append(
                        Worker(
                            row["Name"],
                            int(row["Age"]),
                            float(row["Salary"]),
                            int(row["Overtime Hours"]),
                        )
                    )
        return employees
    except FileNotFoundError:
        return []


def add_employee(employees):
    print("\nAdd Employee")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))
    role = input("Enter role (Manager/Worker): ").strip().lower()

    if role == "manager":
        team_size = int(input("Enter team size: "))
        employees.append(Manager(name, age, salary, team_size))
    elif role == "worker":
        overtime_hours = int(input("Enter overtime hours: "))
        employees.append(Worker(name, age, salary, overtime_hours))
    else:
        print("Invalid role. Employee not added.")


def display_employees(employees):
    if not employees:
        print("\nNo employees found.")
        return
    print("\nEmployees:")
    for i, employee in enumerate(employees, start=1):
        print(f"\nEmployee {i}:")
        print(f"Name: {employee.get_name()}")
        print(f"Age: {employee.get_age()}")
        print(f"Salary: {employee.get_salary()}")
        if isinstance(employee, Manager):
            print(f"Team Size: {employee.get_team_size()}")
        elif isinstance(employee, Worker):
            print(f"Overtime Hours: {employee.get_overtime_hours()}")


def update_employee(employees):
    name = input("\nEnter the name of the employee to update: ")
    for employee in employees:
        if employee.get_name() == name:
            print("\nUpdate Employee:")
            employee.set_name(input("Enter new name: "))
            employee.set_age(int(input("Enter new age: ")))
            employee.set_salary(float(input("Enter new salary: ")))
            if isinstance(employee, Manager):
                employee.set_team_size(int(input("Enter new team size: ")))
            elif isinstance(employee, Worker):
                employee.set_overtime_hours(int(input("Enter new overtime hours: ")))
            print("Employee updated successfully.")
            return
    print("Employee not found.")


def delete_employee(employees):
    name = input("\nEnter the name of the employee to delete: ")
    for i, employee in enumerate(employees):
        if employee.get_name() == name:
            employees.pop(i)
            print("Employee deleted successfully.")
            return
    print("Employee not found.")


def menu():
    employees = load_from_csv("employees.csv")
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            display_employees(employees)
        elif choice == "3":
            update_employee(employees)
        elif choice == "4":
            delete_employee(employees)
        elif choice == "5":
            save_to_csv("employees.csv", employees)
            print("Changes saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()