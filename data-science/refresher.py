def contains_vowel(string: str):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for character in string:
        if str(character).lower() in vowels:
            return True

    return False


def is_even(value):
    return value % 2 == 0


def brute_force_sort():
    pass


def sort_even_odd(list_of_integers):
    even_numbers = []
    odd_numbers = []

    for integer in list_of_integers:
        if is_even(integer):
            even_numbers.append(integer)
        else:
            odd_numbers.append(integer)

    even_numbers.sort()
    odd_numbers.sort()

    return tuple(even_numbers + odd_numbers)


def exercise_one():
    string = input("Enter string: \n")
    if contains_vowel(string):
        print("String contains a vowel")
    else:
        print("String does not contain a vowel")


def exercise_two():
    value = int(input("Enter value: \n"))
    if is_even(value):
        print("Even Number")
    else:
        print("Odd Number")


def exercise_three():
    tuple_of_strings = input("Enter all integers, separated by a space: \n").split()

    list_of_integers = []
    for _ in tuple_of_strings:
        list_of_integers .append(int(_))

    sorted_integers = sort_even_odd(list_of_integers)
    print(sorted_integers)


def self_test():
    assert contains_vowel("jfeo") == True
    assert contains_vowel("jfry") == False
    assert is_even(4) == True
    assert is_even(9) == False
    assert sort_even_odd((3, 2, 18, 0, 7, 6)) == (0, 2, 6, 18, 3, 7)


if __name__ == '__main__':
    self_test()

    # print("Exercise One")
    # exercise_one()
    #
    # print("\nExercise Two")
    # exercise_two()
    #
    # print("\nExercise Three")
    # exercise_three()
