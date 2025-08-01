
# Have a sorted array
A = [-3,-1,0,1,4,7]





#Naive way to search through - O(n)
# if -1 in A:
#     print(True)

#Traditional Binary Search - Looking if a number in the array
#Time O(log n)
#Space is O(1)

def binary_search(arr,target):
    N = len(arr)
    L = 0  # at start of the array
    R = N - 1  # at the end of the array


    while L <= R: # we want to run even when L = R to consider final value but if R is < L then we cross the search space & you will return False
        M = L + ((R-L) // 2) # at the middle of the array - lower middle always chosen
        if arr[M] == target:
            return True
        elif arr[M] < target:  # target is bigger than the middle
            L = M + 1
        else:
            R = M - 1
    return False #IF WE cant find it

print(binary_search(A,-11))

#Conditional Binary Search  -Boolean & arranged  - same T O(log(n)) - Space - O(1)
# [F, F ,F ,F , T, T, T]
#Searching for the first True
#      0      1     2      3      4     5     6
B = [False, False, False, False, True, True, True]
#     L                    M                   R
# M is false
#                                  L     M     R
#M is now true
#                                  L    M,R
# NOW M IS CHANGED POSITION
#                                 L,M    R
#NOW M IS TRUE & SO R = M
# AND NOW R = L TOO
#                                 L,M,R
# SO NOW WE RETURN index = to 4


def binary_search_condition(arr):
    #looking for the first True
    N = len(arr)
    L = 0
    R = N-1

    while L < R: #not = to as we have to force it to escape, as when they are = to each other that case we need
        M = (L+R) //2

        if arr[M]: #if the array at the middle #IF IT IS TRUE
            R = M  #WE DONT KNOW IF L IS TRUE TOO , WE JUST KNOW M IS SO SET R = M

        else: #so M is false then L would be false too
            L = M + 1
    return L

print(binary_search_condition(B))

