import sys

while 1:
    word = input('please enter a word with lower case')
    if not word.islower():
        print('Incorrect input.')
        sys.exit()

    letter_a = ord('a')
    consecutive_list = []
    for i in range(len(word)):
        j = i + 1
        start = i
        temp = list()
        temp.append(word[start])
        while j < len(word):
            if ord(word[start]) + 1 == ord(word[j]):
                temp.append(word[j])
                start = j
            j += 1
        consecutive_list.append(temp)
    max_len = 0
    length = [len(w) for w in consecutive_list]
    for w in consecutive_list:
        if len(w) == max(length):
            print(f'The solution is: '+''.join(i for i in w))
            break
