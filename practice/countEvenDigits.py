num = 123456

count = 0 

while num > 0:

    last_digits = num % 10

    if last_digits % 2 == 0:
        count += 1
    
    num = num // 10

print(count)