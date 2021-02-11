class Employee(object):

    def __init__(self, name: str, employee_id: int):
        self.name = name
        self.employee_id = employee_id

    def earn(self) -> float:
        pass

    def __str__(self):
        return f"Name: {self.name} \nId: {self.employee_id} \nEarns: {self.earn()}"
