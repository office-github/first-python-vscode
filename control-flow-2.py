for n in range(2, 10):
    for x in range(2, n):
        if n % 2 == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# output:
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 is a prime number

for n in range(2, 10):
    for x in range(2, n):
        if n % 2 == 0:
            print(n, 'equals', x, '*', n / x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# output:
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2.0
# 5 is a prime number
# 6 equals 2 * 3.0
# 7 is a prime number
# 8 equals 2 * 4.0
# 9 is a prime number

'''
The continue statement, also borrowed from C, continues with the next iteration of the loop:
'''
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

# output:
#     Found an even number 2
#     Found a number 3
#     Found an even number 4
#     Found a number 5
#     Found an even number 6
#     Found a number 7
#     Found an even number 8

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
    continue
    print("Found a number", num)

# output:
    # Found an even number 2
    # Found an even number 4
    # Found an even number 6
    # Found an even number 8

'''
The pass statement does nothing. 
It can be used when a statement is required syntactically but the program requires no action.
For example:
'''

while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)
