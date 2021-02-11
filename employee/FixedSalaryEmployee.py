from Employee import Employee


class FixedSalaryEmployee(Employee):

    def __init__(self, name: str = "", employee_id: int = 0, fixed_salary: float = 0.0):
        # super(FixedSalaryEmployee, self).__init__(name, employee_id)
        super().__init__(name, employee_id)
        self.salary = fixed_salary

    def earn(self) -> float:
        return self.salary

    def __str__(self):
        return "Fixed salary employee\n" + \
               super(FixedSalaryEmployee, self).__str__()
