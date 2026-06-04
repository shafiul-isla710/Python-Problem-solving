numbers = [1,2,3,4,6]

start, end = min(numbers), max(numbers)

missing_set = set(range(start,end+1)) - set(numbers)

missintNum = list(missing_set)

print(missintNum)