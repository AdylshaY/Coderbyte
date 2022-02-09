def KnightJumps(strParam):

  moves = [[-1,2], [-1,-2], [-2,-1], [-2,1], [1,2], [1,-2], [2,-1], [2,1]]

  current_position = list(map(int, strParam[1:-1].split()))
  # print(current_position)
  counter = 0
  for move in moves:
    new_x = move[0] + current_position[0]
    new_y = move[1] + current_position[1]
    # print(new_x, new_y)
    if 0<new_x<9 and 0<new_y<9:
      counter += 1

  return counter

# keep this function call here 
print(KnightJumps(input()))
