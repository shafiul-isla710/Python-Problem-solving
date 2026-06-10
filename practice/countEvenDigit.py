def countEven(num):
    if num <= 0:
        return "The Number is Zero"

    count = 0
    while num > 0:
        lastD = num % 10
        if lastD % 2 == 0:
            count += 1
        
        num //= 10
    
    return count


print(countEven(9344))