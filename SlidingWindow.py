#Variable Length - window has changing size
# Fixed Length - window size is fixed

s = "abcabcbb"

#Time: O(n)
#Space: O(n)

def varLengthWindow(s):
    l = 0
    longest = 0
    sett = set()
    n = len(s)

    for r in range(n): #this is O(n)
        while s[r] in sett: #meaning while set is invalid   - this is what we remove to the set - this is O(n) in same time as the for loop
            sett.remove(s[l])
            l += 1

        w = (r-l) + 1
        longest = max(longest, w) #compares and sees if old or new w is bigger and longest will equal that
        sett.add(s[r]) #s[r] was a duplicate so it was removed

    return longest
print(varLengthWindow(s))







#-----------------------------------------------------------------------------------------------------------------------------------------------
#Fixed Length Window

#Leetcode 646
'''
You have  a list of numbers and given a value K, K is the length of numbers you have contigously, you need to find the maximum value of that
eg:
nums = [1,12,-5,-6,50,3]   k = 4
the 3 options are:
                    1 ,12, -5, -6       -> Average: 12.75
                    12, -5, -6, 50       -> Average: 10.75
                    -5, -6, 50, 3        -> Average: 9.75
Hence Max Average is 12.75
'''

nums = [1,12,-5,-6,50,3]
k =4

def fixedLengthWindow(nums, k):  #nums is an array of integers
    n = len(nums)
    cur_sums = 0

    for i in range(k): #runs through number indexes: 0 to k-1 (3)  hence 4 numbers
        cur_sums += nums[i]

    max_avg = cur_sums / k

    for i in range(k,n):  #starts from index 4 to the length of the array (meaning all the other numbers till the end). eg if 12 elements then goes from index to index 11 inclusive
        cur_sums += nums[i]
        cur_sums -=nums[i-k]

        new_avg = cur_sums / k
        max_avg = max(max_avg, new_avg)

    return max_avg

#Time: O(n) - just moving across all elements once
# Space: O(1)



print(fixedLengthWindow(nums,k))



