
# p = 100
# r = 7/100
# n = [10, 20, 30]
#
# for year in n:
#     a = p * (1 + r)**year
#     print(f"year = {year}, a = {a:.2f}")


# p = 100
# r = 7/100
# n = 10
# a = p * (1 + r)**n
# print(f"year = {n}, a = {a:.2f}")
#
# n = 20
# a = p * (1 + r)**n
# print(f"year = {n}, a = {a:.2f}")
#
# n = 30
# a = p * (1 + r)**n
# print(f"year = {n}, a = {a:.2f}")


def calculate_amount_on_deposit(p: float, r: float, n: float):
    return p * (1 + r)**n


def main():
    p_given = 1000
    r_given = 7/100
    years_given = [10, 20, 30]

    for year in years_given:
        amount = calculate_amount_on_deposit(p_given, r_given, year)
        print(f"year = {year}, return = {amount:.2f}")


if __name__ == '__main__':
    main()
