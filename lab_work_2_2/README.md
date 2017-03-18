##Laboratory Work 2.1

####Description:

Write the code to perform following task:

* Generate sequence 5 integers long from range(0, 100) 
* Generate random float 
* Print variables above 
* Find max element from generated sequence 
* Make a floor division between max element and generated float 
* Find factorial of the result above 
* Shorten the code as much as possible

####Here is its solution code:

*solution_2_2.py
```python
import random
import math

"""
Generate sequence 5 integers long from range(0, 100)
"""
integers_sequence=random.sample(range (100),5)
print("5 integers long from range(0, 100): {}".format(integers_sequence))

"""
Generate random float
"""
generated_float=random.random()

"""
Print variables above
"""
print ("Generated float: {}".format(generated_float))

"""
Find max element from generated sequence
"""
max_int = max(integers_sequence)

"""
Make a floor division between max element and generated float
"""
division = max_int // generated_float

"""
Find factorial of the result above
"""

factorial_int_seq = math.factorial(integers_sequence)
factorial_gen_float = math.factorial(generated_float)
factorial_max = math.factorial(max_int)
factorial_division = math.factorial(division)

"""
Shorten the code as much as possible
"""

```