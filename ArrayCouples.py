# This code got 6 points !!!

def ArrayCouples(arr):
  pair_list = FindPairs(arr)
  for pair in pair_list:
    pair.reverse()
    pair_list.remove(pair)
    if pair in pair_list:
      continue
    else:
      return ",".join(list(map(str, pair)))
  return 'yes'


def FindPairs(arr):
  pairs = []
  for i in range(0,len(arr),2):
    # print(arr[i], arr[i+1])
    l = [arr[i], arr[i+1]]
    pairs.append(l)
  return pairs

# keep this function call here 
print(ArrayCouples(input()))
