def EvenPairs(strParam):
  count = 0
  for char in strParam:
    if char.isdigit():
      if int(char) % 2 == 0:
        count += 1
        if count == 2:
          return 'true'
      else:
        continue
    else:
      count = 0
  return 'false'
  
# keep this function call here 
print(EvenPairs(input()))
