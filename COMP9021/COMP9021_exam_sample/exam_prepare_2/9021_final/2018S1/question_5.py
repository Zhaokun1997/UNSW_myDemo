def f(word):
    '''
    Recall that if c is an ascii character then ord(c) returns its ascii code.
    Will be tested on nonempty strings of lowercase letters only.

    >>> f('x')
    The longest substring of consecutive letters has a length of 1.
    The leftmost such substring is x.
    >>> f('xy')
    The longest substring of consecutive letters has a length of 2.
    The leftmost such substring is xy.
    >>> f('ababcuvwaba')
    The longest substring of consecutive letters has a length of 3.
    The leftmost such substring is abc.
    >>> f('abbcedffghiefghiaaabbcdefgg')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is bcdefg.
    >>> f('abcabccdefcdefghacdef')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is cdefgh.
    '''
    if word:
        if len(word) == 1:
            print(f'The longest substring of consecutive letters has a length of 1.')
            print(f'The leftmost such substring is {word[0]}.')
        else:
            result = []
            for i in range(len(word)):
                temp_str = ''
                temp_str += word[i]
                index = i
                if index + 1 <= len(word) - 1:
                    while ord(word[index + 1]) - ord(word[index]) == 1:
                        temp_str += word[index + 1]
                        index += 1
                        if index == len(word) - 1:
                            break
                result.append(temp_str)
            max_len = 1
            for e in result:
                if len(e) > max_len:
                    max_len = len(e)
            for e in result:
                if len(e) == max_len:
                    sub_string = e
                    break

            print(f'The longest substring of consecutive letters has a length of {max_len}.')
            print(f'The leftmost such substring is {sub_string}.')


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    f('ababcuvwaba')
