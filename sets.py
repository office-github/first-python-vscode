"""
A set is an unordered collection with no duplicate elements.
Basic uses include membership testing and eliminating duplicate entries.
Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
----------------------------
Curly braces or the set() function can be used to create sets. 
Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary, a data structure
"""

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

#output: {'apple', 'pear', 'orange', 'banana'}

print('orange' in basket)                 # fast membership testing
# output: True

"""
# Demonstrate set operations on unique letters from two words
"""
a = set('abracadabra')
b = set('alacazam')
print(a)     # unique letters in a
#output: {'a', 'r', 'c', 'd', 'b'}
print(a - b)
# letters in a but not in b, output: {'b', 'r', 'd'}
print(a | b)
# letters in a or b or both, output: {'m', 'd', 'r', 'z', 'c', 'l', 'b', 'a'}
print(a & b)
# letters in both a and b, output: {'a', 'c'}
print(a ^ b)
# letters in a or b but not both, output: {'m', 'r', 'l', 'd', 'b', 'z'}

"""
Similarly to list comprehensions, set comprehensions are also supported:
"""
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
# output: {'r', 'd'}
