# 6/10 total points

def HappyNumbers(num):
  result = 0
  for i in str(num):
    result = int(i) ** 2 + result
  if result != 1:
    return False
  else:
    return True

# keep this function call here 
print(HappyNumbers(input()))
