def hightDigit(num):
    if num <= 0:
        return 0
    
    hight_d = 0

    while num > 0:
        digit = num % 10

        if digit > hight_d:
            hight_d = digit
        
        if hight_d == 9:
            return hight_d
        
        num = num // 10
    return hight_d

print(hightDigit(493))