def rearrange(number):
    num_list = []
    string = str(number)
    for i in string:
        if i != '0':
            num_list.append(int(i))
    num_list.sort(reverse=False)
    returnStr = ""
    for i in num_list:
        returnStr += str(i)

    return returnStr


print(rearrange(1))
print(rearrange(200))
print(rearrange(395))
print(rearrange(10029001))
print(rearrange(301302004))
print(rearrange(9409898038908908934890))
