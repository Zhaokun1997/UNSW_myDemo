

# recursion
def can_merge(first_str, second_str, last_str):
    if not first_str and second_str == last_str:
        return True
    if not second_str and first_str == last_str:
        return True
    if not first_str or not second_str:
        return False
    if first_str[0] == last_str[0] and can_merge(first_str[1:], second_str, last_str[1:]):
        return True
    if second_str[0] == last_str[0] and can_merge(first_str, second_str[1:], last_str[1:]):
        return True
    return False


while 1:
    ranks = ['first', 'second', 'third']
    strings = [input(f'Please input the {rank} string:') for rank in ranks]
    last = strings[0]
    if len(last) < len(strings[1]):
        last = strings[1]
    if len(strings[1]) < len(strings[2]):
        last = strings[2]

    if last == strings[0]:
        first, second = strings[1], strings[2]
    if last == strings[1]:
        first, second = strings[0], strings[2]
    if last == strings[2]:
        first, second = strings[0], strings[1]

    if len(last) != len(first) + len(second) or not can_merge(first, second, last):
        print(f'No solution ')
    else:
        index = strings.index(last)
        print(f'the {ranks[index]} string can be obtained by merging the other two. ')
