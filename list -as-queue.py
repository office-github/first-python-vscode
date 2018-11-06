from collections import deque

queue = deque(['bijay', 'rajesh', 'ranjeet'])
queue.append('hwllo')

print(queue)

print(queue.popleft())

print(queue)

# output:
# deque(['bijay', 'rajesh', 'ranjeet', 'hwllo'])
# bijay
# deque(['rajesh', 'ranjeet', 'hwllo'])
