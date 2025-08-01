#Hashsets
#
# s = set() #you can add stuff into sets
# print(type(s))
#
# #Sets  is a data structure that has ONLY unique values, its defined with curly {} brackets
# #
# number = [1, 1, 2, 6, 4]
# first = set(number)
# print(first)
# second = {1, 3, 5, 3}
# print(second) #this would remove the 2nd 3 as only unique values
# print(type(second))  #shows its a set -
#
# #Union of 2 sets
# print(first | second) #this prints a new set with only unique values from both sets, ascending order
# #Intersection of 2 sets
# print(first & second) #this prints a set with only the values that appear in both sets
# #Difference between sets
# print(first - second) #this gives 2,4, 6 - its the values that appear in first but not second
# #Symmetric Difference
# print(first ^ second) #this gives values in first or second set but not both

#Note one thing about SETS
#UNLIKE LISTS, THEY ARE UNORDERED
# YOU DONT HAVE ANY INDEXES IN SETS
# IF YOU NEED TO ACCESS BY SETS THEN SHOULD BE NO USE FOR INDEXES

#they are used to check for the existence

#---------------------------------------------------------------------------------------------

#Hashsets

s = set()
print(s) #first shows an empty set

#Add item into Set - T O(1)
s.add(1)
s.add(2)
s.add(3)

print(s) #shows 3 things in the set

#Lookup if something is in the set - T O(1)
if 1 in s:
    print(True) #1 is in the set

#Also
if 4 not in s:
    print("False")
    #This is still O(1) run time

#Remove something from the set - O(1)
#s.remove(4) #WOULD GET AN ERROR BCOS ITS NOT THE SET
s.remove(3)
print(s)


#
string = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbcccccccccccc"
#to see if a character is in here
sett = set(string) #The set construction takes O(s) time where s is the length of the string

print(sett) # this removes the unwanted duplicates so u can just see the unique items

#looping through a set - rarely done
for x in s:
    print(x)
#this gives you the T- O(n) as you looping through each element
# n is number of things in the set

#-------------------------------------------------------------------------

#HASHMAPS
#they are just dictionaries in python

d = {"greg": 1, "steve": 2, "rob":3}
#add all the key value pairs first
# so greg maps over to 1
#steve maps over to 2
#rob maps over to 3

#add key:value pair in dict - T(O(1))
d["arsh"]=9 # note number doesnt reflect its index
print(d)

#Check for the presence in a dictionary : T O(1)
if "greg" not in d:
    print("True")

#Check the value corresponding to a key in a dictionary O(1)
print(d["greg"]) #you assume this key is in the dictionary
#if key not in dict, then you will get a Key Error

#Looping over the key:value pairs of the dictionary
#O(n)

for key, value in d.items():
    print(f"key: {key}, value: {value}")

#DEFAULT DICT

from collections import defaultdict

default = defaultdict(int) #this gives each key without a value, a value of 0
#this assigns a default value to every key so you dont get Key error
print(default[2]) #this will automatically link key 2 to value 0
print(default) #shows its an int default and the key value pair

default_list = defaultdict(list) #this gives each key without a value, a value of 0
print(default_list[2]) #this way makes a list as the value as default for each key
print(default_list)

#Common in lEETCODE

#COUNTER DICTIONARY
from collections import Counter

#string has lots of a, b & c
string = "aaaaaaaaaaaabbbbbbbbbbbbccccccccccc"
counter = Counter(string)
print(counter)
#dont use counters in the interviews
#But the counter will create a dictionary with a count for each character in a string.
