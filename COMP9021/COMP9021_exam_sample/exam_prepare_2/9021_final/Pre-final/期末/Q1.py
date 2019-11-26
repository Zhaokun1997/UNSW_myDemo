#Q1
def f(number):
    '''
    >>> f(13024065)
    123456
    >>> f(530021)
    1235
    '''
    str_num=str(number)
    num_list=[]
    for i in str_num:
        if i == '0':
            continue
        else:
            num_list.append(i)
    return int(''.join(sorted(num_list)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print('Test Done! If not show "Test Failed", you pass my test')
