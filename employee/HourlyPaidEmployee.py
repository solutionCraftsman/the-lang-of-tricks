from Employee import Employee


class HourlyPaidEmployee(Employee):

    def __init__(self, name: str, employee_id: int, hourly_rate: float):
        # super(HourlyPaidEmployee, self).__init__(name, employee_id)
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.num_of_hours = 0

    def earn(self) -> float:
        if self.num_of_hours <= 40:
            earning = self.num_of_hours * self.hourly_rate
        else:
            earning = 40 * self.hourly_rate
            earning += (self.hourly_rate - 40) * (self.hourly_rate * 1.5)

        return earning

    def __str__(self):
        return "Hourly paid employee\n" + \
               super(HourlyPaidEmployee, self).__str__()

    def set_num_of_hours(self, num_of_hours: int):
        self.num_of_hours = num_of_hours
