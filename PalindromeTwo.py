def PalindromeTwo(strParam):
  chars = []
  for char in strParam:
    if char.isalpha():
      chars.append(char.lower())
  
  if chars == chars[::-1]:
    return 'true'
  else:
    return 'false'


# keep this function call here 
print PalindromeTwo(raw_input())
