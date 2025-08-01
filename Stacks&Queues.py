#Stacks  -LIFO , FILO

#Uses dynamic arrays

stk = []
print(stk)  #nothing appears


#Append to the top of the stack O(1), LIFO (from right is at top)  JUST ADDING TO THE TOP
stk.append(5)

#print(stk)

stk.append(4)
stk.append(3)

print(stk)  #this is now [5,4,3] 3 is at the bottom & 5 is at the top

#Pop from the top of the stack  - O(1)
#tracking what you popped

x=stk.pop()
print(x)  # so we popped 3 from the stack so now [5,4]
print(stk) #this should be [5,4] as we removed the final element



#Ask whats on the top of the stack - O(1)
print(stk[-1])  #so the last element is what is on top of the stack

#Ask if stack is empty or not
if stk:
    print("True")

# stk.pop()
# print(stk)
# stk.pop()
# print(stk)
#stk.pop() you will get an error if you pop from an empty stack

#Note its best to pop from a stack only when in an if stack: circumstance


#Queues - First in First Out (FIFO)
# to solve problems import a class called Deque

from collections import deque

q = deque() #deque is the double ended queue, it has 2 ends, you can add to the right & pop & you can do the same to both left right

print(q)

#Enqueue - Add elements to the right - O(1)
q.append(5)
q.append(6)

print(q)

#Dequeue (pop left) - Remove elements from the left - O(1)
q.popleft() #this will pop from the left
#if you just did q.pop() this will pop from the right NOT A QUEUE
#note that queues will pop from the left & append to the right

print(q)

#Note that the queue will NOT be a dynamic array as if you popped something, that element would need replacing with a 0
#instead its a doubly linked list so we dont have to do that & the time complexity is O(1)

#Peek from the left (can be right too) / seeing what will come out of the queue first
q.append(7)
print(q)
print(q[0]) #this shows you whats the most left element - O(1)

print(q[-1]) #shows element on the right - O(1)



