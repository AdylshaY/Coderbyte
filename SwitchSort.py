def SwitchSort(arr):
  steps = 0
  i = 0

  while i < len(arr):
    if(i+1 == arr[i]):  # n. eleman n+1 sayisina esit ise olmasi gereken yerdedir.
      i += 1
    elif(arr[i] == len(arr)):  # listenin elemen sayisina esit olan sayiyi oynatmak tekrar ayni yere geri gelmesini saglar.
      i += 1
    elif(arr[i]-1 == ((i+arr[i]) % len(arr))):  # listedeki n sayisini saga(ileri) hareket ettirince n-1. indexe gelip gelmedigini kontrol eder.
      change(i, ((i+arr[i]) % len(arr)), arr)
      # print(arr)    # listenin her degisim sonrasi yeni durumunu gormek icin
      steps += 1
      i = 0
    elif(arr[i]-1 == ((i-arr[i]) % len(arr))):  # listedeki n sayisini sola(geri) hareket ettirince n-1. indexe gelip gelmedigini kontrol eder.
      change(i, ((i-arr[i]) % len(arr)), arr)
      # print(arr)    # listenin her degisim sonrasi yeni durumunu gormek icin
      steps += 1
      i = 0
    else:
      i += 1
  return steps

def change(first, second, arr):
  arr[first], arr[second] = arr[second], arr[first]
  return arr

# keep this function call here 
print(SwitchSort(input()))
