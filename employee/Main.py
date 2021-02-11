from BasePlusCommissionEmployee import BasePlusCommissionEmployee
from CommissionEmployee import CommissionEmployee
from FixedSalaryEmployee import FixedSalaryEmployee
from HourlyPaidEmployee import HourlyPaidEmployee


def main():
    h = HourlyPaidEmployee("H", 11, 1000.0)
    h.set_num_of_hours(40)
    print(h.earn())
    print(h)

    print()

    f = FixedSalaryEmployee("F", 12, 500_000.0)
    print(f.earn())
    print(f)

    print()

    c = CommissionEmployee("C", 13, 5 / 100)
    c.set_gross_sales(10_000.0)
    print(c.earn())
    print(c)

    print()

    b = BasePlusCommissionEmployee("B", 14, 500_000.0, 5 / 100)
    b.set_gross_sales(10_000.0)
    print(b.earn())
    print(b)


if __name__ == '__main__':
    main()
