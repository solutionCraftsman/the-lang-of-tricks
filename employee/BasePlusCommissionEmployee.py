from FixedSalaryEmployee import FixedSalaryEmployee
from CommissionEmployee import CommissionEmployee


class BasePlusCommissionEmployee(FixedSalaryEmployee, CommissionEmployee):

    def __init__(self, name: str, employee_id: int, fixed_salary: float, commission_rate: float):
        FixedSalaryEmployee.__init__(self, name, employee_id, fixed_salary)
        CommissionEmployee.__init__(self, name, employee_id, commission_rate)

    def earn(self) -> float:
        return FixedSalaryEmployee.earn(self) + CommissionEmployee.earn(self)

    def __str__(self):
        return "Base plus commission employee\n" + \
               super(BasePlusCommissionEmployee, self).__str__()
