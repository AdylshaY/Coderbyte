def CountingMinutes(strParam):
  times = strParam.split('-')
  time1 = Convert24Hour(times[0])
  time2 = Convert24Hour(times[1])
  min1 = (time1[0] * 60) + time1[1]
  min2 = (time2[0] * 60) + time2[1]
  if min2 > min1:
    return min2 - min1
  elif min1 > min2:
    return min2 - min1 + 1440
  else:
    return 0
  

def Convert24Hour(times):
  if times[-2:] == 'pm':
    hour = times[:-2].split(':')
    if hour[0] != '12':
      hour[0] = int(hour[0]) + 12
      hour[1] = int(hour[1])
    else:
      hour[0] = int(hour[0])
      hour[1] = int(hour[1])
  else:
    hour = times[:-2].split(':')
    if hour[0] == '12':
      hour[0] = int(hour[0]) + 12
      hour[1] = int(hour[1])
    else:
      hour[0] = int(hour[0])
      hour[1] = int(hour[1])
  return hour


# keep this function call here 
print CountingMinutes(raw_input())
