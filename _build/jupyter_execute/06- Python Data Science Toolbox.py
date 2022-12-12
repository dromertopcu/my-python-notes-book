#!/usr/bin/env python
# coding: utf-8

# ## Python Data Science Toolbox

# ### Introduction to iterators

# **Iterable**
# * Examples: lists, strings, dictionaries, ,le connections
# * An object with an associated iter() method
# * Applying iter() to an iterable creates an iterator</a>
# 
# **Iterator**
# * Produces next value with next()

# ```python
# word = 'Da'
# it = iter(word) 
# next(it) # iterating over iterables
# ```
# ```
# 'D'
# ```
# ```python
# next(it)
# ```
# ```
# 'a'
# ```
# ```python
# next(it)
# ```
# ```
# StopIteration Traceback (most recent call last)
# <ipython-input-11-2cdb14c0d4d6> in <module>()
# -> 1 next(it)
# StopIteration:
# ```

# ```python
# word = 'Da'
# it = iter(word) 
# print(*it) # iterating at once with *
# ```
# ```
# D a t a
# ```
# ```python
# print(*it) # no more values to go through
# ```
# ```
# ```

# ```python
# file = open('file.txt') # iterating over file connections
# it = iter(file) 
# print(next(it))
# ```
# ```
# This is the first line.
# ```
# ```python
# print(next(it))
# ```
# ```
# This is the second line.
# ```

# ### Playing with iterators

# ```python
# avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
# e = enumerate(avengers) # using enumerate()
# print(type(e))
# ```
# ```
# <class 'enumerate'>
# ```
# ```python
# e_list = list(e)
# print(e_list)
# ```
# ```
# [(0, 'hawkeye'), (1, 'iron man'), (2, 'thor'), (3, 'quicksilver')]
# ```

# ```python
# avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
# for index, value in enumerate(avengers): # enumerate() and unpack
#     print(index, value)
# ```
# ```
# 0 hawkeye
# 1 iron man
# 2 thor
# 3 quicksilver
# ```
# ```python
# for index, value in enumerate(avengers, start=10):
#     print(index, value)
# ```
# ```
# 10 hawkeye
# 11 iron man
# 12 thor
# 13 quicksilver
# ```

# ```python
# avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
# names = ['barton', 'stark', 'odinson', 'maximoff']
# z = zip(avengers, names) # using zip()
# print(type(z))
# ```
# ```
# <class 'zip'>
# ```
# ```python
# z_list = list(z)
# print(z_list)
# ```
# ```
# [('hawkeye', 'barton'), ('iron man', 'stark'),
# ('thor', 'odinson'), ('quicksilver', 'maximoff')]
# ```

# ```python
# avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
# names = ['barton', 'stark', 'odinson', 'maximoff']
# for z1, z2 in zip(avengers, names): # zip() and unpack
#     print(z1, z2)
# ```
# ```
# hawkeye barton
# iron man stark
# thor odinson
# quicksilver maximoff
# ```

# ```python
# avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
# names = ['barton', 'stark', 'odinson', 'maximoff']
# z = zip(avengers, names)
# print(*z) # print zip with *
# ```
# ```
# ('hawkeye', 'barton') ('iron man', 'stark')
# ('thor', 'odinson') ('quicksilver', 'maximoff')
# ```

# ### Using iterators to load large files into memory

# ```python
# import pandas as pd
# result = []
# for chunk in pd.read_csv('data.csv', chunksize=1000): # iterating over data specify the chunksize
#     result.append(sum(chunk['x']))
# total = sum(result)
# print(total)
# ```
# ```
# 4252532
# ```

# ### List comprehensions

# ```python
# nums = [12, 8, 21, 3, 16]
# new_nums = [num + 1 for num in nums] # list comprehension
# print(new_nums)
# ```
# ```
# [13, 9, 22, 4, 17]
# ```

# ```python
# result = [num for num in range(11)] # list comprehension with range()
# print(result)
# ```
# ```
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ```

# ```python
# pairs_2 = [(num1, num2) for num1 in range(0, 2) for num2 in range(6, 8)] # nested loops
# print(pairs_2)
# ```
# ```
# [(0, 6), (0, 7), (1, 6), (1, 7)]
# ```

# ### Advanced comprehensions

# ```python
# [num ** 2 for num in range(10) if num % 2 == 0] # conditionals in comprehensions
# ```
# ```
# [0, 4, 16, 36, 64]
# ```

# ```python
# [num ** 2 if num % 2 == 0 else 0 for num in range(10)] # conditionals in comprehensions
# ```
# ```
# [0, 0, 4, 0, 16, 0, 36, 0, 64, 0]
# ```

# ```python
# pos_neg = {num: -num for num in range(9)} # dict comprehensions
# print(pos_neg) 
# ```
# ```
# {0: 0, 1: -1, 2: -2, 3: -3, 4: -4, 5: -5, 6: -6, 7: -7, 8: -8}
# ```

# ### Introduction to generator expressions

# Recall list comprehension :
# ```python
# [2 * num for num in range(10)]
# ```
# ```
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# ```
# Use ```( )``` instead of ```[ ]``` :
# ```python
# (2 * num for num in range(10))
# ```
# ```
# <generator object <genexpr> at 0x1046bf888>
# ```

# ```python
# result = (num for num in range(6))
# for num in result:
#     print(num)
# ```
# ```
# 0
# 1
# 2
# 3
# 4
# 5
# ```
# ```python
# print(list(result))
# ```
# ```
# [0, 1, 2, 3, 4, 5]
# ```

# ```python
# even_nums = (num for num in range(10) if num % 2 == 0)
# print(list(even_nums))
# ```
# ```
# [0, 2, 4, 6, 8]
# ```

# Generator functions
# * Produces generator objects when called
# * Defined like a regular function  ```def```
# * Yields a sequence of values instead of returning a single value
# * Generates a value with ```yield``` keyword

# ```python
# def num_sequence(n):
#     """Generate values from 0 to n."""
#     i = 0
#     while i < n:
#         yield i
#         i += 1
# ```

# ```python
# result = num_sequence(5)
# print(type(result))
# ```
# ```
# <class 'generator'>
# ```
# ```python
# for item in result:
#     print(item)
# ```
# ```
# 0
# 1
# 2
# 3
# 4
# ```
