def funcname():
    print("Function without parameter")


def funcname1(parameter_list):
    print("Function with parameter")
    print(parameter_list)
    if isinstance(parameter_list, int):
        return
   # parameter_list = str(parameter_list)
    for x in range(0, len(parameter_list)):
        print(parameter_list[x])


'''
Same output but with different approach

def funcname1(parameter_list):
    print("Function with parameter")
    print(parameter_list)
    if isinstance(parameter_list, list):
       # parameter_list = str(parameter_list)
        for x in range(0, len(parameter_list)):
            print(parameter_list[x])
'''

funcname()
# Output: Function without parameter

funcname1(2)
# Output:
# Function with parameter
# 2

n = [1, 2, 3, 4]
funcname1(n)

# Output:
# Function with parameter
# [1, 2, 3, 4]
# 1
# 2
# 3
