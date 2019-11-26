# COMP9021 19T3 - Rachid Hamadi
# Sample Exam 2


'''
Given a word w, a good subsequence of w is defined as a word w' such that
- all letters in w' are different;
- w' is obtained from w by deleting some letters in w.

Returns the list of all good subsequences, without duplicates, in lexicographic order
(recall that the sorted() function sorts strings in lexicographic order).

The number of good sequences grows exponentially in the number of distinct letters in w,
so the function will be tested only for cases where the latter is not too large.

'''

from itertools import combinations


def good_subsequences(word):
    '''
    >>> good_subsequences('')
    ['']
    >>> good_subsequences('aaa')
    ['', 'a']
    >>> good_subsequences('aaabbb')
    ['', 'a', 'ab', 'b']
    >>> good_subsequences('aaabbc')
    ['', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
    >>> good_subsequences('aaabbaaa')
    ['', 'a', 'ab', 'b', 'ba']
    >>> good_subsequences('abbbcaaabccc')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb']
    >>> good_subsequences('abbbcaaabcccaaa')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    >>> good_subsequences('abbbcaaabcccaaabbbbbccab')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    '''
    # Insert your code here
    # abbcaaabcccaaa --> abcabca
    if word:
        new_word = ''
        new_word += word[0]
        for i in range(1, len(word)):
            if word[i - 1] != word[i]:
                new_word += word[i]
        result = ['']
        for length in range(1, len(set(new_word)) + 1):
            temp_result = []
            for item in combinations(new_word, length):
                if len(item) == len(set(item)):
                    temp_result.append(''.join(item))
            for e in temp_result:
                result.append(e)
        s = set(result)
        result = [x for x in s]
        result.sort(reverse=False)
        return result
    else:
        return ['']


# Possibly define another function


if __name__ == '__main__':
    import doctest

    doctest.testmod()
