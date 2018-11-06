"""
# 1 A tuple consists of a number of values separated by commas, for instance:
"""
t = 111, 34234, 3242, 'ewrwer'

print(t)

# output: (111, 34234, 3242, 'ewrwer')

"""
# 2 Tuples may be nested:
"""
u = t, (1, 2, 3, 4, 5)
print(u)
# output: ((111, 34234, 3242, 'ewrwer'), (1, 2, 3, 4, 5))

"""
# 3 Tuples are immutable:
"""

# t[0] = 88888, this gives compile time error as tuples are immutable
# TypeError: 'tuple' object does not support item assignment

# but they can contain mutable objects:

v = ([1, 2, 3], [3, 2, 1])
print(v)

# output: ([1, 2, 3], [3, 2, 1])

"""
Note: 
Tuples are immutable, and usually contain a heterogeneous sequence of elements that
 are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples).
"""
''' ***************************************** '''

'''
Empty tuples are constructed by an empty pair of parentheses;
a tuple with one item is constructed by following a value with a comma
'''

empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))  # output: 0
print(len(singleton))  # output: 1
print(singleton)  # output: ('hello',)

# The statement t = 111, 34234, 3242, 'ewrwer' is an example of tuple packing:
# the values 111, 34234, 3242 and 'ewrwer'' are packed together in a tuple. The reverse operation is also possible:
x, y, z, k = t
print(x)  # output: 111
