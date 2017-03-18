##Labaratory work 2.4

####Description

Write the code to do following:

* Generate list with lowercase and uppercase alphabet plus numbers 
* Print 1st symbol of list 
* Print last symbol 
* Print 3rd from start and 3rd from the end 
* Slice first 10 symbols 
* Print only symbols with index, which divides on 2 without remaining 
* Print only integer values from list 
* Reverse list using slice 
* Convert base list into string

####Here is its solution code:

*solution_2_4
```
python
"""
 Generate list with lowercase and uppercase alphabet plus numbers
"""
list_1 = ['Y', 'a', 'k', 'i', 'b', 'c', 'h', 'u', 'k', '1', '6', '0', '8', '1', '9', '8', '9']

"""
Print 1st symbol of list
"""
print(list_1[0])

"""
Print last symbol
"""
print(list_1[-1])

"""
Print 3rd from start and 3rd from the end
"""
print(list_1[2],list_1[-3])

"""
Slice first 10 symbols
"""
print(list_1[0:10])

"""
Print only symbols with index, which divides on 2 without remaining
"""
print(list_1[1:len(list_1):2])

"""
Print only integer values from list
"""
symbol_list = ['Y', 'a', 'k', 'i', 'b', 'c', 'h', 'u', 'k', '1',
               '6', '0', '8', '1', '9', '8', '9']
digits = []

for symbol in symbol_list:
    try:
        digits.append(int(symbol))
    except ValueError:
        pass

print(digits)

"""
Reverse list using slice
"""
print(list_1[::-1])

"""
Convert base list into string
"""
print(str(list_1))
```