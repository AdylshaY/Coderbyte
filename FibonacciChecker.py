# 10/10 points
# Big-O notation is O(n)

def FibonacciChecker(num):

  fib_num = [0,1]
  if num in fib_num:
    return 'yes'
  while True:
    new_fib = fib_num[-1] + fib_num[-2]
    if num > new_fib:
      fib_num.append(new_fib)
    elif num == new_fib:
      return 'yes'
    else:
      return 'no'



# keep this function call here 
print(FibonacciChecker(input()))
