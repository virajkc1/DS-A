#Bubble Sort
#Time - O(n^2)
#Space - O(1)



A = [-5, 3, 2, 1, -3, 7, 2, 2]
#produced an array

def bubble_sort(arr):
    n = len(arr) #length of the array
    flag = True #this means that we are not done yet
    while flag: #while true
        flag = False #we change to false as we assume that we are done
        # if we need to make a change then we should change the flag back to true so the while loop can be passed through again
        for i in range(1,n): #this goes and runs thru all the elements in the array
            #this goes from position 0 to n-1
            if arr[i -1] > arr[i]:  # position 0 bigger than 1 so we need to swap
                flag = True # we should run the loop again as we are about to do a swap
                arr[i-1], arr[i] = arr[i], arr[i-1]  # we are swapping them around
    return arr
#if you changed the while loop condition inside the loop , then it will still continue all the lines of code

# print(bubble_sort(A))

#---------------------------INSERTION SORT-----------------------------------
#it will be 2 for loops
#T - O(n^2) as nested loops but in place so its Space O(1)

B = [-5,3,2,1,-3,-3,7,2,2]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n): #starts at index i to index n which is exclusive so is not included so you go from starting at 1 to n-1
         for j in range(i,0,-1): #starting at i & 0 is the end exclusive, and -1 decrements by 1, note that 0 is not included so you wont go out of bounds
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:  #if comparison not true then its in the same spot so you should break out of the loop
                break  #breaks out of the if statement AND THE INNER FOR LOOP
         #print(arr)
    return arr
insertion_sort(B)

#------------------------SELECTION SORT-----------------------------
#Nested loop - Time O(n^2), Space O(1)

C = [-3,3,2,1,-5,-3,7,2,2]
def selection_sort(arr):
    n = len(arr)
    for i in range(n): #means 0 to n-1, so loops thru the whole array
        min_index = i # this sets the first minimum value to the value at index 0.
        for j in range(i+1,n):  #we go from the i+1 at the start so 1 if i=0 & loop thru to n-1 as n is exclusive
            if arr[j] < arr[min_index]:  #if the value we land on with index j is smaller than the current min_index value
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  #after j loops through all the items after i, it finds the index with the minimum value and stores it outside the inner loop
        # now we have to SWAP the index i we were on with that minimum index
        #so we go inside the inner for loop and do that
        #print(arr)
    return arr

selection_sort(C)



#-----------------------------MERGE SORT------------------------
#Time - O(nlogn)
#Space - O(n) can be log n but very hard to write

D = [-5,3,2,1,-3,-3,7,2,2]

def merge_sort(arr):
    n = len(arr)
    if n == 1: #if we have an array of just 1 then we want to return the array, we never get an array of size n (empty array due to the way its split)
        return arr
    #if didnt return the array then its bigger than a single element

    m = len(arr) // 2
    L = arr[:m] #everything upto the middle is 1 array (middle not included)
    R = arr[m:] #everything including the middle is another array   #this is why its 0(n) space

    #if you have 2 arrays you want to sort it before

    #BY RECURSION (LOOK BELOW)
    L = merge_sort(L)
    R= merge_sort(R)
    #keep calling the function until we get all elements as single elements (above)

    #switching the arrays
    l, r = 0, 0  #setting the pointers at the start
    L_len = len(L)  #due to all the recursion, the first time it will be used is when we have single elements in the array
    R_len = len(R)

    #now have 2 arrays and need to sort them so you can merge them in linear time
    sorted_arr = [0] * n #this will make an empty array that has n 0s inside it
    i = 0 #this is a count

    while l < L_len and r < R_len: #this means while bother sliders are in the bounds of the array
        if L[l] < R[r]:  #if the index at l of array L is less than index r at array R
            sorted_arr[i] = L[l] # then add the value at index l at L in the sorted array
            l += 1 #this will increment the l index from 0 to the next value
        else:  #if R[r] is less than or equal to L[l]
            sorted_arr[i] = R[r] #this will add the R[r] value in the sorted array
            r += 1  #this will increment r

        i+=1 #this increments the sorted array to be the next position

    #this below while loop will start if r is out of range but l isnt
    while l < L_len:  #while the index l is in the the array
        sorted_arr[i] = L[l]
        i += 1
        l += 1
    #if anything else left in r instead and l is out of range
    while r < R_len:
        sorted_arr[i] = R[r]
        i += 1
        r += 1

    return sorted_arr

#print(merge_sort(D))

#-------------------------------------QUICK SORT-------------------------------------
#Time - O(n logn) (Average is this but can be worse O(n^2)
#Space - O(n)

E = [-5,3,2,1,-3,-3,7,2,2]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr # if you have an array of size 1 or 0

    #if not a base case
    p = arr[-1] #this is the pivot & its at the last element of the array

    L = [x for x in arr[:-1] if x<= p]  #list comprehension  - means every time in array not including the last item
    #if the item is less than or equal to the pivot
    R = [x for x in arr[:-1] if x>p]  #this is every item greater than the pivot in another list

    #now using recursion, you can sort them
    L = quick_sort(L)  # so after we made our list we break it down to a smaller array until you reach base cases
    R = quick_sort(R)

    return L + [p] + R  #this will join up the lists

# print(quick_sort(E))

#-------------------------------------COUNT SORT-------------------------------------

#Time is O(n+k) where k is the range of the data
#Can be written with negative arrays but the range will be bigger so we doing positive numbers as its easier
#k is the max of the array
#Space O(k)

F = [5,3,2,1,3,3,7,2,2]

def counting_sort(arr):
    n = len(arr)
    maxx = max(arr) #this will give you the maximum of the array
    counts = [0] * (maxx + 1) # so it goes from 0 to the maximum value eg if maxx was 6 then you have 0 to 5 but we want 0 to 6 hence the +1

    for x in arr:  #for each number in the array
        counts[x] += 1 #the count at that number will increase
        #eg in our array we have a 3 so the value at counts[3] will increase by 1 as the indexes represent the values in the counts array

    i = 0  #set an index of 0 - going through the array
    for c in range(maxx+1):  #goes over all the valid counts from 0 to maxx (we miss out maxx+1)
        while counts[c] > 0:  #while the counts value at the first position (index 0) is bigger than - 0
            arr[i] = c  #the corresponding array index so at the start will be arr[0] = the index c
            i += 1 #then we will move to next position in our array by incrementing index
            counts[c] -= 1 #so the value at counts[0] at the start will decrease by 1
    return arr

#print(counting_sort(F))

#----------------------------------------WHAT WE DO IN PRACTICE-----------------------------------------

#Time complexity - O(n logn) using TIM SORT

G = [-5,3,2,1,-3,-3,7,2,2]

#In Place (constant space)
G.sort()
print(G)

#if you dont want it in space  - O(n) Space  - if you want a new array
H = [-5,3,2,1,-3,-3,7,2,2]

sorted_H = sorted(H) #this returns us a new array that is sorted
# print(H, sorted_H)

#Sorting arrays of tuples

I = [(-5,3),(2,1),(-3,-3),(7,2),(2,2)]
#for the intervals problems

sorted_I = sorted(I, key = lambda t: t[0])
#lambda is a function to tell you what you want to sort by - so we are sorting by the tuples first position to do the second position then t[1] instead
# print(sorted_I)
#to sort it decending by second element then change to -t[1]

