
age = int(input("How old are you?: "))
max_heart_rate = 220 - age
target_heart_rate_lower = (50 * max_heart_rate) / 100
target_heart_rate_upper = (85 * max_heart_rate) / 100

print(f"max_heart_rate = {max_heart_rate}")
print(f"target_heart_rate = ({target_heart_rate_lower} - {target_heart_rate_upper})")

