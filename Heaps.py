#Build Min Heaps (Heapify)
# Time O(n) , Space O(1) as we just rearrange the elements

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
# this is an array that represents a Binary Tree

import heapq
# you can build a queue with this library

# heapq.heapify(A)
# # remember each children for a parent n is 2n & 2n+1 index
# print(A)
#
# # Heap Push (Insert Element)
# # Time : O(log n)
# # remember A is now the heap not the array
#
# heapq.heappush(A, 4)
# # A is a heap, & 4 shows up in the end
# # may think it is wrong for 4 to be at the end but not an error
#
#         #         -4
#         #     0        1
#         #  3     2    5  10
#         # 8 12  9 4
# # looks like this hence its correct
#
# print(A)
#
#
# # Heap pop (Extract min)
# # Time 0(log n) - time to fix the heap tree after popping it
#
# minn = heapq.heappop(A)
# print(minn)
# # # this shows the top element which is the minimum
# print(A)
# # this shows the heap after the pop
#



# Heap sort
# works by popping from the heap repeatedly
# Time O(nlog n) Space(O(n)) but there is a complex way to make it O(1)

# def heapsort(arr):
#     #Takes an array
#     print(arr)
#     heapq.heapify(arr)   #rearranges the array so it follows the heap property
#     print(arr)
#     n = len(arr) #takes the num elements in the array
#     print(n) # prints the num elements
#     new_list = [0] * n #this makes a list of n items from 0 to n-1
#
#     for i in range(n):
#         minn = heapq.heappop(arr) #this gives you the minimum from the heap by popping the heap
#         # num elements n & processing them in log n time so its nlog n time complexity
#         new_list[i] = minn  # adds at position 0 the minimum it just popped
#         #basically you are popping from the heap to have a list of ascending numbers
#     # print(arr)
#     return new_list

def heapsort(arr):
    n = len(arr)
    heapq.heapify(arr)
    new_list = [0] * n
    for i in (arr):






print(heapsort([1,3,5,7,9,2,4,6,8,0]))
#you make a new array, so space is O(n)

#Heap Pop Push: Time O(log n) , Space O(n)

# print(A)
# heapq.heappushpop(A,99)  #this will pop off the min element of the heap & then push the new element, 99, into the correct space
# print(A)

#heapq is ONLY for minimum heap

#To peak at the minimum heap, position is the first in the heap T-O(1)

# minn = A[0]
# print(minn)

#Max Heap
# B = [-4,3,1,0,2,5,10,8,12,9]
# n = len(B)
#
# for i in range(n):
#     B[i] = -B[i] #make all the elements in the array B negative or if its already negative then positive
# heapq.heapify(B)
# print(B) #now 12 is -12 so its the smallest
# largest = -heapq.heappop(B)
#
# print(largest) #this will pop the largest element (12) as 12 is -12 then its popped from the heap & turned into positive 12
# #the biggest value 12 becomes the most negative value
#
# #to push into the heap
#
# heapq.heappush(B, -7) #this will insert - 7 into the heap but then is converted to positive 7 when popped
# print(B)


#Building the heap yourself
#Time 0(nlogn)  as you push n things over time
#This is slower than heapify as heapify is T-O(n)

#
# C = [-5, 4, 2, 1, 7, 0, 3]
# heap = []
#
# for x in C:
#     heapq.heappush(heap, x) #we are pushing x into the heap
#     print(heap)
#
#     #to check the number of things in the heap
# print(len(heap)) #note that len is constant
#
#
# #Putting tuples of items on the heap
# D = [5,4,3,5,4,3,5,5,4] # create an array
# #Common to count the occurrences of an item in an array
#
# from collections import Counter
#
# counter = Counter(D)
# #made a counter object that takes the array D
# print(counter)
# #this will make a dictionary
# #each key is the unique item & the value is the number of occurrences
#
# heap = [] #make an empty heap to push to
# for key,value in counter.items():
#     #print(key, value)
#     heapq.heappush(heap,(value,key))
#     # each time we will push onto the heap, the tuple , where each tuple has the value then the frequency
#
#     #smallest frequency at the top
#     #if two keys have the same frequency then the heap pushes the smallest number ( key)
#     #remember that the number is the key & the frequency is the value
#     #so it does by value first then by key
#
# print(heap)
#
#
#
#
#
#
#
