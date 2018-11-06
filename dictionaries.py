"""
Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type;
strings and numbers can always be keys.
Tuples can be used as keys if they contain only strings, numbers, or tuples;
if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.
You can’t use lists as keys, since lists can be modified in place using index assignments,
slice assignments, or methods like append() and extend().
----------------------
It is best to think of a dictionary as a set of key: value pairs,
A pair of braces creates an empty dictionary: {}
# 1. delete a key:value pair with del
# 2. Performing list(d) on a dictionary returns a list of all the keys used in the dictionary,
# 3. in insertion order (if you want it sorted, just use sorted(d) instead).
"""

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

# output: {'jack': 4098, 'sape': 4139, 'guido': 4127}

print(tel['jack'])
# output: 4098

del tel['sape']  # deleting the item from dictionary
print(tel)
# output: {'jack': 4098, 'guido': 4127}

list(tel)
print(tel)
# output: {'jack': 4098, 'guido': 4127}, note: dictionary not converted to the list
print(list(tel))
# output: ['jack', 'guido'], returns the keys list

print(sorted(tel))  # output: ['guido', 'jack']

print('guido' in tel)  # output: True
print('jack' not in tel)  # output: False

"""
The dict() constructor builds dictionaries directly from sequences of key-value pairs:
"""

dictionary = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dictionary)
#output: {'sape': 4139, 'guido': 4127, 'jack': 4098}

"""
In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
"""

x = {x: x**2 for x in (2, 4, 6)}

print(x)
#output: {2: 4, 4: 16, 6: 36}

"""
When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
"""
dd = dict(sape=4139, guido=4127, jack=4098)
print(dd)
#output: {'sape': 4139, 'guido': 4127, 'jack': 4098}
