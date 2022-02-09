def SimpleEvens(num):
  for char in str(num):
    if int(char) % 2 != 0:
      return 'false'
  return 'true'

# keep this function call here 
print SimpleEvens(raw_input())
