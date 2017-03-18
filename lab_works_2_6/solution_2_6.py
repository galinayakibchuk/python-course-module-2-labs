"""
Generate two sets with not unique numbers and few symbols
"""
bdg = set('galina1608')
bdm = set('mother1701')

"""
Print 1st set
"""
print('bdg: {}'.format(bdg))

"""
Create tuple from intersection of first and second set
"""
t_1 = tuple(bdg & bdm)

"""
Create tuple from difference first and second set
"""
t_2 = tuple(bdg - bdm)

"""
Slice first 3 symbols from first tuple
"""
print(t_1[0:2])

"""
Print only symbols with numbers from second set
"""
symbol_list = set('mother1701')
symbol = []

for s in symbol_list:
    try:
        symbol.append(int(s))
    except ValueError:
        pass

print(symbol)

"""
Reverse tuple using slice
"""
t_1 = t_1[::-1]
t_2 = t_2[::-1]

"""
Convert both tuples into list
"""
l_1 = list(t_1)
l_2 = list(t_2)

print(l_1, l_2)