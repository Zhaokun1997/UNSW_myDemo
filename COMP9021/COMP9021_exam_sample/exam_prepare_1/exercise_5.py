# You might find the ord() function useful.

def longest_leftmost_sequence_of_consecutive_letters(word):
    if len(word) == 0:
        return ''
    elif len(word) == 1:
        return word
    else:
        i = 0
        lst = []
        while i < len(word):
            temp_str = ''
            temp_str += word[i]
            length = 1
            j = i + 1
            if j == len(word):
                break
            while ord(word[j]) - ord(word[i]) == 1:
                temp_str += word[j]
                length += 1
                i += 1
                j += 1
                if j == len(word):
                    break
            if length >= 1:
                lst.append(temp_str)
                i = j
            else:
                i += 1
        max_length = max(len(word) for word in lst)
        for word in lst:
            if len(word) == max_length:
                result = word
                break
        return result


print(longest_leftmost_sequence_of_consecutive_letters(''))
print(longest_leftmost_sequence_of_consecutive_letters('a'))
print(longest_leftmost_sequence_of_consecutive_letters('zuba'))
print(longest_leftmost_sequence_of_consecutive_letters('ab'))
print(longest_leftmost_sequence_of_consecutive_letters('bcab'))
print(longest_leftmost_sequence_of_consecutive_letters('aabbccddee'))
print(longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt'))
print(longest_leftmost_sequence_of_consecutive_letters('efghuvwijlrstuvabcde'))
