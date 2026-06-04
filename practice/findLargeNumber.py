def largeNum(x):
 
  if not x:
    print('The list is Empty')
  
  largeNumber = x[0]
  
  for i in x:
    if largeNumber < i:
      largeNumber = i
  
  
  print(largeNumber)

  

numbers = [3,5,6,32,9]
largeNum(numbers)