def CheckNums(num1,num2):

  if num1 > num2:
    return 'false'
  elif num2 > num1:
    return 'true'
  else:
    return '-1'

# keep this function call here 
print CheckNums(raw_input())
