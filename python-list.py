nums = [10, 11, 2, 22, 20, 30]
num = {10, 20,11}

print(nums[-1]) #output: 30 from last
print(nums[-2]); '''output: 20 from last'''
print(nums[0]) #output: 10
print(nums[-2:]) #output: [20, 30] from last, slicing returns a new list
print(num.pop()) #output: 10
print(2**3) #3 is Power of 2
print(nums[2:5]) #output: [2, 22, 20], excluding last index

letters = ['a', 'b', 'c', 'd']
print(len(letters)) #output: 4

''' It is possible to nest lists (create lists containing other lists), for example: '''

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x) #output: [['a', 'b', 'c'], [1, 2, 3]]
print(x[0]) #output: ['a', 'b', 'c']
print(x[0][1]) #output: 'b'
print(x[1]) #output: [1, 2, 3]

a, b = 0, 1
print(a)
print(b)
while a < 1000:
    print(a, end='\t')
    a, b = b, a + b
print("done")