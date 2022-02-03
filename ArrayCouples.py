def ArrayCouples(arr):
  pair_list = FindPairs(arr)
  l = []
  for pair in pair_list:
    reversed_pair = list(reversed(pair))
    if reversed_pair in pair_list:
      continue
    else:
      l.append(pair)
  if len(l) == 0:
    return 'yes'
  else:
    flatten_list = [item for subl in l for item in subl]
    return ",".join(list(map(str, flatten_list)))

def FindPairs(arr):
  pairs = []
  for i in range(0,len(arr),2):
    # print(arr[i], arr[i+1])
    l = [arr[i], arr[i+1]]
    pairs.append(l)
  return pairs

# keep this function call here 
print(ArrayCouples(input()))
