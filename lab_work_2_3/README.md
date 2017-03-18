##Laboratory Work 2.3

####Description

Write the code to do following:

* Generate string with lowercase and uppercase alphabet plus numbers 
* Print 1st symbol of string 
* Print last symbol 
* Print 3rd from start and 3rd from the end 
* Slice first 8 symbols 
* Print only symbols with index, which divides on 3 without remaining 
* Print the symbol of the middle of the string text 
* Reverse text using slice

####Here is its solution code:

*solution_2_2.py
```python
"""
 Generate string with lowercase and uppercase alphabet plus numbers
"""
s = 'Galina16081'

"""
Print 1st symbol of string
"""
print(s[0])

"""
Print last symbol
"""
print(s[-1])

"""
Print 3rd from start and 3rd from the end
"""
print(s[2], s[-3])

"""
Slice first 8 symbols
"""
print(s[0:8])

"""
Print only symbols with index, which divides on 3 without remaining
"""
print(s[2:len(s):3])

"""
Print the symbol of the middle of the string text
"""
print(s[len(s)//2])

"""
Reverse text using slice
"""
print(s[::-1])

```

