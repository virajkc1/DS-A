# 2 pointers means 2 indexes at the start & end that are squeezing

nums = [-4,-1,0,3,10]    #16,  1,  0   , 9 , 100

#Squares of a sorted array
#we can sort it in nlogn time 0,1,9,16,100
#[100,16,9,1,0]


def two_pointer(arr):
    n = len(nums)
    right = n - 1
    left = 0
    result = []
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left] ** 2)
            left += 1
        else:
            result.append((nums[right] ** 2))
            right -= 1

    return result

#Time 0(n) # have to go thru all elements 1 time
#Space 0(n)

print(two_pointer(nums))





