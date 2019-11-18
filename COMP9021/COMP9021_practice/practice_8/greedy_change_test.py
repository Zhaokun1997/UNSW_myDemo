from collections import defaultdict

face_values = [1, 2, 5, 10, 20, 50, 100]
amount = int(input('Input the desired amount: '))

result_map = defaultdict(int)
for i in range(-1, -len(face_values) - 1, -1):
    while amount // face_values[i]:
        result_map[face_values[i]] += 1
        amount -= face_values[i]

nb_bank_notes = sum(value for value in result_map.values())

print(f'{nb_bank_notes} banknotes are needed ')
for key, value in result_map.items():
    print(f'{"$" + str(key):>4} : {value}')  # >4 右对齐
