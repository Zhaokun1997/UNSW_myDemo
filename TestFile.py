pair = [(1, 2), (2, 3)]
with open('writeFile.tex', 'w') as file:
    file.write(f'    \\draw {pair[0]} -- {pair[1]};')
