# Dynamic vs Static Array

#Creating an array

A = [1,2,3]
print(A)  #PRINTS THE ARRAY

# Append - Insert element at the end of the array - Time is 0 (1) - BCOS OF DYNAMIC ARRAY

A.append(5)
"""
print(A) #this will now add 5 at the end of the array & print it

# Pop - Deleting element at the end of the array - ALWAYS O(1), constant time as never need additional space

A.pop()
print(A) #removed 5


#Insert (not at end of array) - Takes Time O(n)
#all elements at WORST case will have to shift

A.insert(2,5)
#2 is the index & 5 is what will be inserted at index 2

#Modifying an element - Takes time O(1) - just changing
A[0] = 9
print(A)

#Accessing element given index i - O(1)
print(A[2])

if 6 in A:
    print("True")
#This is 0(n) - runs through all the elements
#Space is O(1) as no extra space needed

#finding the length of an array in O(1) time as its a constant counting property inbuilt into python
print(len(A))
#------------------------------------------------------------------------------------

#Strings

#Appending at the end of the string - O(n) take all the characters & make a new string

s = "hello"

b= s + "z"
print(b)

#Check if something in the string - O(n) Time Complexity

if "e" in s:
    print("True")

#Accessing Positions in a string
print(s[2]) # this is O(1)


#finding the length of a string
print(len(s)) #this counts characters in the string
#Its O(1) - it stores length as a property that it can look up - inbuilt into Python
"""