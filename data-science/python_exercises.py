
my_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
my_week_1: list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
my_week_2 = list(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])

print(my_week)
print(my_week_1)
print(my_week_2)


def modify_week(weeks):
    first_element = weeks.pop(0)
    weeks.append(first_element)


modify_week(my_week)
print(my_week)

tasks = ("Java", "Sleep", "Python", "Data Science", "Catch Cruise", "Flex", "Flex")


def make_daily_plan(week, tasks):
    my_week_acts: dict = {}
    for day, task in zip(week, tasks):
        my_week_acts[day] = task

    return my_week_acts


def make_daily_plan_2(week, tasks):
    return dict(zip(week, tasks))


mwa = make_daily_plan_2(my_week, tasks)
print(mwa)

x = dict(zip(my_week, tasks))
print(x)
print(type(x))


def squares_thingy(keys):
    my_squares: dict = {}
    value = 0
    for key in keys:
        value += 1
        my_squares[key] = value ** 2

    return my_squares


def squares_thingy_2(keys):
    my_squares: dict = {}
    for key, value in zip(keys, range(1, len(keys) + 1)):
        my_squares[key] = value ** 2

    return my_squares


def squares_thingy_3(keys):
    return dict(zip(keys, [_ ** 2 for _ in range(1, len(keys) + 1)]))


def squares_thingy_4(keys):
    return {_: __ ** 2 for _, __ in zip(keys, range(1, len(keys) + 1))}


squares = ['One', 'Two', 'Three', 'Four', 'Five']
print(squares_thingy(squares))
print(squares_thingy_2(squares))
print(squares_thingy_3(squares))
print(squares_thingy_4(squares))


def do_listings(no_of_groups):
    ds_group_collection = {}

    for i in range(1, no_of_groups + 1):
        y = input(f'Enter names of Group {i} members, separated by a space: ')
        y = y.split()
        ds_group_collection[i] = list(y)

    return ds_group_collection


print(do_listings(3))
