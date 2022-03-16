def LetterCount(strParam):
  strParam = strParam.split()
  a,b = 1, -1
  for i in range(len(strParam)):
    for j in strParam[i]:
      if strParam[i].count(j) > a:
        a = strParam[i].count(j)
        b = i
  
  if b != -1:
    return strParam[b]
  else:
    return -1


# keep this function call here 
print(LetterCount(input()))
