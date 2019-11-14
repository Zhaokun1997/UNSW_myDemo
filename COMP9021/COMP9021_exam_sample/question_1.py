# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 1 


from random import seed, randint
import sys


def f(arg_for_seed, nb_of_elements, max_element):
    if nb_of_elements < 0:
        sys.exit()
    seed(arg_for_seed)
    L = [randint(0, max_element) for _ in range(nb_of_elements)]
    print('Here is L:', L)
    R = []
    # Insert your code here
    if L:
        temp = []
        for i in range(len(L)):
            if i == 0:
                temp.append(L[i])
            else:
                if L[i] not in temp:
                    if temp:
                        if L[i] > temp[-1]:
                            temp.append(L[i])
                        else:
                            R.append(temp)
                            temp = list()
                            temp.append(L[i])
                    else:
                        temp.append(L[i])
                else:
                    R.append(temp)
                    temp = []
        if temp:
            R.append(temp)

    print('The decomposition of L into increasing sequences,')
    print('    with consecutive duplicates removed, is:\n   ', R)
    print('\n')



f(0, 0, 10)
f(0, 1, 10)
f(0, 2, 10)
f(0, 3, 10)
f(0, 4, 10)
f(0, 5, 10)
f(0, 6, 10)
f(0, 7, 10)
f(3, 10, 6)
f(3, 15, 8)
