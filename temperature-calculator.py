from utils import *


def celsius_to_fahrenheit(temperature_in_celsius):
    """ function to convert temperature in celsius to fahrenheit """
    # logic here
    # (0°C × 9/5) + 32 = 32°F
    return add(((multiply(temperature_in_celsius, 9)) / 5), 32)


# celsius_input = float(input("Enter temperature in celsius: "))
# print(celsius_to_fahrenheit(celsius_input))
#

celsius_input = input('Enter temperature values in celsius, separated by comma: ')
celsius_input_list = celsius_input.split(',')

for celsius_input in celsius_input_list:
    print(str(celsius_input) + "C is " + str(celsius_to_fahrenheit(float(celsius_input))) + "F")
