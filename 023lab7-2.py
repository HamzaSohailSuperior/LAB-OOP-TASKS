class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def xyz(self):
        print(f"Name: {self.name}, Position: {self.position}")

class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)
        self.department = department

    def xyz(self):
        print(f"Department: {self.department}")

class Worker(Employee):
    def __init__(self, name, position, hours_worked):
        super().__init__(name, position)
        self.hours_worked = hours_worked

    def xyz(self):
        print(f"Hours Worked: {self.hours_worked}")

if __name__ == "__main__":
    manager = Manager("Alice Smith", "Project Manager", "IT")
    worker = Worker("Bob Johnson", "Software Developer", 40)

    manager.xyz()
    worker.xyz()
