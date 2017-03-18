##Labaratory work 2.6

####Description

Write the code to do following:

o Generate two sets with not unique numbers and few symbols 
o Print 1st set 
o Create tuple from intersection of first and second set 
o Create tuple from difference first and second set 
o Slice first 3 symbols from first tuple 
o Print only symbols with numbers from second set 
o Reverse tuple using slice 
o Convert both tuples into list

####Here is its solution code:

*solution_2_6
```
python
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
```