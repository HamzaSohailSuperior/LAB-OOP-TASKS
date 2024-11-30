import csv


# Parent Class
class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    # Getters
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_salary(self, salary):
        self.__salary = salary

    def to_dict(self):
        return {
            "name": self.__name,
            "age": self.__age,
            "salary": self.__salary,
        }


# Child Class of Employee
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.__department = department

    # Getters
    def get_department(self):
        return self.__department

    # Setters
    def set_department(self, department):
        self.__department = department

    def to_dict(self):
        data = super().to_dict()
        data["department"] = self.__department
        data["hours_worked"] = None
        return data


# Child Class of Employee
class Worker(Employee):
    def __init__(self, name, age, salary, hours_worked):
        super().__init__(name, age, salary)
        self.__hours_worked = hours_worked

    # Getters
    def get_hours_worked(self):
        return self.__hours_worked

    # Setters
    def set_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked

    def to_dict(self):
        data = super().to_dict()
        data["department"] = None
        data["hours_worked"] = self.__hours_worked
        return data


# File handling 
FILE_NAME = "employees.csv"


def save_to_file(employees):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age", "salary", "department", "hours_worked"])
        writer.writeheader()
        for emp in employees:
            writer.writerow(emp.to_dict())


def load_from_file():
    employees = []
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["department"]:
                    employees.append(Manager(row["name"], int(row["age"]), float(row["salary"]), row["department"]))
                elif row["hours_worked"]:
                    employees.append(Worker(row["name"], int(row["age"]), float(row["salary"]), int(row["hours_worked"])))
    except FileNotFoundError:
        print("No employee records found. Starting fresh!")
    return employees


# Employee management 
def add_employee(employees):
    print("\nAdd a New Employee")
    name = input("Enter  employee's name: ").strip()
    age = int(input("Enter  employee's age: "))
    salary = float(input("Enter  employee's salary: "))
    role = input("Enter  role (Manager/Worker): ").strip().lower()

    if role == "manager":
        department = input("Enter  manager's department: ").strip()
        employees.append(Manager(name, age, salary, department))
        print(f"Manager '{name}' added successfully.")
    elif role == "worker":
        hours_worked = int(input("Enter  number of hours worked: "))
        employees.append(Worker(name, age, salary, hours_worked))
        print(f"Worker '{name}' added successfully.")
    else:
        print("Invalid entr. Please try again.")
        return
    save_to_file(employees)


def display_employees(employees):
    print("\nEmployee Records")
    if not employees:
        print("No employees found. Errorrr 404")
        return
    for i, emp in enumerate(employees, 1):
        print(f"#{i}: {emp.to_dict()}")


def update_employee(employees):
    print("\nUpdate Employee Details")
    name = input("Enter name of employee to update: ").strip()
    for emp in employees:
        if emp.get_name().lower() == name.lower():
            print(f"Found employee: {emp.to_dict()}")
            emp.set_age(int(input("Enter new age: ")))
            emp.set_salary(float(input("Enter new salary: ")))
            if isinstance(emp, Manager):
                emp.set_department(input("Enter new department: ").strip())
            elif isinstance(emp, Worker):
                emp.set_hours_worked(int(input("Enter new hours worked: ")))
            save_to_file(employees)
            print(f"Details for '{name}' updated successfully.")
            return
    print("Employee not found. Erorrr 404")


def delete_employee(employees):
    print("\nDelete Employee")
    name = input("Enter name of employee to delete: ").strip()
    for emp in employees:
        if emp.get_name().lower() == name.lower():
            employees.remove(emp)
            save_to_file(employees)
            print(f"Employee '{name}' deleted successfully.")
            return
    print("Employee not found. Please try again.")


# Main function with menu-driven interface
def main():
    employees = load_from_file()

    while True:
        print("\n=== Employee Management System ===")
        print("1. Add a New Employee")
        print("2. Display All Employees")
        print("3. Update Employee Details")
        print("4. Delete an Employee")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            display_employees(employees)
        elif choice == "3":
            update_employee(employees)
        elif choice == "4":
            delete_employee(employees)
        elif choice == "5":
            print("Goodbye! Thank you for using the Employee Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
