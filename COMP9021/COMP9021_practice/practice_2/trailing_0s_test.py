import sys
from math import factorial


def first_computation(number):
    count = 0
    while number % 10 == 0:
        number = number // 10
        count += 1
    return count


def second_computation(number):
    # count = 0
    # string = str(number)
    # for i in range(-1, -len(string) - 1, -1):
    #     if string[i] == '0':
    #         count += 1
    #     else:
    #         break
    # return count
    if len(number) < 2:
        return 0
    i = 1
    while 1:
        if number[-i] != 0:
            return i - 1
        i += 1


def third_computation(number):
    count = 0
    power_of_five = 5
    while number >= power_of_five:
        count += number // power_of_five
        power_of_five *= 5
    return count


try:
    the_input = int(input('Input a nonnegative integer: '))
    if the_input < 0:
        raise ValueError
except ValueError:
    print('Incorrect input')
    sys.exit()

input_factorial = factorial(the_input)
print(f'Computing the number of trailing 0s in {the_input}! by dividing by 10 for long enough:',
      first_computation(input_factorial))
print(f'Computing the number of trailing 0s in {the_input}! by converting it into a string:',
      second_computation(str(input_factorial)))
print(f'Computing the number of trailing 0s in {the_input}! the smart way:',
      third_computation(the_input))
