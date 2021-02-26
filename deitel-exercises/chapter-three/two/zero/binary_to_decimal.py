def binary_to_decimal(value_in_binary: int):
    value_in_decimal = power = 0

    while value_in_binary > 0:
        rem = value_in_binary % 10
        value_in_binary //= 10
        value_in_decimal += rem * 2**power
        power += 1

    return value_in_decimal

