def rearrange(L, from_first=True):
    # from first, then last
    new_L = []
    if L:
        if from_first:
            if len(L) == 1:
                new_L.append(L[0])
            elif len(L) >= 2:
                i_index = 0
                j_index = len(L) - 1
                while i_index < j_index:
                    new_L.append(L[i_index])
                    new_L.append(L[j_index])
                    i_index += 1
                    j_index -= 1
                    if i_index == j_index:
                        new_L.append(L[i_index])
                        break
        else:
            if len(L) == 1:
                new_L.append(L[0])
            elif len(L) >= 2:
                i_index = 0
                j_index = len(L) - 1
                while i_index < j_index:
                    new_L.append(L[j_index])
                    new_L.append(L[i_index])
                    i_index += 1
                    j_index -= 1
                    if i_index == j_index:
                        new_L.append(L[i_index])
                        break
    return new_L


L = [10, 20]
print(tuple((rearrange(L), L)))
L = [10, 20, 30]
print(tuple((rearrange(L), L)))
L = [10, 20, 30, 40]
print(tuple((rearrange(L, False), L)))
L = [10, 20, 30, 40, 50]
print(tuple((rearrange(L, False), L)))
L = [10, 20, 30, 40, 50, 60]
print(tuple((rearrange(L), L)))
L = [10, 20, 30, 40, 50, 60, 70]
print(tuple((rearrange(L), L)))
