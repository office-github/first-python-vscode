print((1, 2, 3) < (1, 2, 4))  # output: True

print([1, 2, 3] < [1, 2, 4])  # output: True

print('ABC' < 'C' < 'Pascal' < 'Python')  # output: True

print((1, 2, 3, 4) < (1, 2, 4))  # output: True

print((1, 2) < (1, 2, -1))  # output: True

print((1, 2, 3) == (1.0, 2.0, 3.0))  # output: True

print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))  # output: True

'''
Other languages may return the mutated object, 
which allows method chaining, such as d->insert("a")->remove("b")->sort();.
'''
