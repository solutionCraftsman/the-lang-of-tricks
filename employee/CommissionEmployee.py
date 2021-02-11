from Employee import Employee


class CommissionEmployee(Employee):

    def __init__(self, name: str = "", employee_id: int = 0, commission_rate: float = 0.0):
        # super(CommissionEmployee, self).__init__(name, employee_id)
        super().__init__(name, employee_id)
        self.gross_sales = 0
        self.commission_rate = commission_rate

    def earn(self) -> float:
        return self.commission_rate * self.gross_sales

    def __str__(self):
        return "Commission employee\n" + \
               super(CommissionEmployee, self).__str__()

    def set_gross_sales(self, gross_sales: float):
        self.gross_sales = gross_sales
