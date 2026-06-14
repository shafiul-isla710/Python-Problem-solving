nums = [10, 5, 20, 8, 15]

max_num = nums[0]

for item in nums:

    if item > max_num:
        max_num = item
    
print(max_num)



//even number count function 

def eventCount(numbers):
    count = 0

    for item in numbers:
        if item % 2 == 0:
            count +=1
    
    return count

print(f"There are {eventCount(nums)} even Number inside of list")