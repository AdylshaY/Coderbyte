def StepWalking(num):
  if num == 1:
    return 1
  if num == 2:
    return 2
  return StepWalking(num-1) + StepWalking(num-2)


# keep this function call here 
print StepWalking(raw_input())
