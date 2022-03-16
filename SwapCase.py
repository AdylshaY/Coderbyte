def SwapCase(strParam):
  newString = ""
  for char in strParam:
    if char.islower():
      upper = char.upper()
      newString += upper
    else:
      lower = char.lower()
      newString += lower
  return newString

# keep this function call here 
print SwapCase(raw_input())
