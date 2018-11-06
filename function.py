def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result


print(fib2(100))  # call it

# output:
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


print(ask_ok('Do you really want to quit?'))

# output: #1

# Do you really want to quit?sdf
# Please try again!
# Do you really want to quit?- 1
# Please try again!
# Do you really want to quit?- 1
# Please try again!
# Do you really want to quit?- 1
# Please try again!
# Do you really want to quit?- 1
# Traceback(most recent call last):
#   File "d:\Practice\PythonDS\first-python-vscode\function.py", line 30, in < module >
#   print(ask_ok('Do you really want to quit?'))
#   File "d:\Practice\PythonDS\first-python-vscode\function.py", line 26, in ask_ok
#   raise ValueError('invalid user response')
# ValueError: invalid user response

# output:  # 2

# Do you really want to quit?ok
# Please try again!
# Do you really want to quit?cls
# Please try again!
# Do you really want to quit?
# Please try again!
# Do you really want to quit?
# Please try again!
# Do you really want to quit?
# Traceback(most recent call last):
#   File "d:\Practice\PythonDS\first-python-vscode\function.py", line 30, in < module >
#   print(ask_ok('Do you really want to quit?'))
#   File "d:\Practice\PythonDS\first-python-vscode\function.py", line 26, in ask_ok
#   raise ValueError('invalid user response')
# ValueError: invalid user response


i = 5


def f(arg=i):
    print(arg)


i = 6
f()

# output:
# 5

'''
Important warning: The default value is evaluated only once.
This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.
For example, the following function accumulates the arguments passed to it on subsequent calls:
'''


def f1(a, L=[]):
    L.append(a)
    return L


print(f1(1))
print(f1(2))
print(f1(3))

# output:
# [1]
# [1, 2]
# [1, 2, 3]

'''
If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
'''


def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f2(1))
print(f2(2))
print(f2(3))

# output:
# [1]
# [2]
# [3]

'''
Small anonymous functions can be created with the lambda keyword.
Lambda functions can be used wherever function objects are required.
'''


def make_incrementor(n):
    return lambda x: x + n


print(make_incrementor(42))
# output: <function make_incrementor.<locals>.<lambda> at 0x01009660>
f = make_incrementor(42)
print(f(0))  # output: 42
print(f(2))  # output: 44
print(f(4))  # output: 46


def my_function():
    """
    Do nothing, but document it.
    No, really, it doesn't do anything.
    """
    '''
    blank
    '''
    pass


print(my_function())  # output: None
print(my_function.__doc__)
# output:
# Do nothing, but document it.
# No, really, it doesn't do anything.


def f3(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f3.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


f3('spam')

# output:
# Annotations: {'ham': < class 'str' > , 'return': < class 'str' > , 'eggs': < class 'str' > }
# Arguments: spam eggs
# 'spam and eggs'
