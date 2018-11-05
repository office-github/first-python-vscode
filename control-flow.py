'''if Statements'''

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
print("done.")

''' Output: 
Please enter an integer: 24
More
done.
'''
# for loop

words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w)

''' Output:
cat
window
defenestrate
'''

for w in words[:]:  # Loop over a slice copy of the entire list.
    print(w)

''' Output:
cat
window
defenestrate
'''

# len of words
print("len of words: ", len(words))
