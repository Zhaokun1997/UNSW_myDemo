# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 5


'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''

import csv


def f(year):
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    numbers = '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'

    months_map = {}
    for i in range(len(months)):
        months_map[numbers[i]] = months[i]
    # Insert your code here
    if 1913 <= year <= 2013:
        # 以列表形式访问
        with open('cpiai.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            months_infla = {}
            for item in reader:
                if int(item[0].split('-')[0]) == year:
                    month = item[0].split('-')[1]
                    Inflation = item[2]
                    months_infla[month] = Inflation
            # print(months_infla)
            max_infla = max(list(value for value in months_infla.values()))
            month_list = []
            for key, value in months_infla.items():
                if value == max_infla:
                    month_list.append(key)
            result = []
            for m in month_list:
                result.append(months_map[m])
            final = ', '.join(result)
            print(f'In {year}, maximum inflation was: {max_infla}')
            print(f'It was achieved in the following months: {final} ')


f(1914)
f(1922)
f(1995)
f(2013)

# with open('test.txt', 'r') as file:
#     print(file)
#     lines = file.readlines()
#     print(lines)
#     for line in lines:
#         print(line)
#         print(type(line))
