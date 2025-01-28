def Sort(arr):
  n = len(arr)
  for i in range(n):
   for j in range(n-i-1):
    if arr[j] > arr[j+1]:
     temp = arr[j]
     arr[j] = arr[j+1]
     arr[j+1] = temp
  return arr


arr = ['a', 'c', 'b', 'd', 'e', 'f']
# arr = [5, 2, 6, 4, 7, 4]
print(Sort(arr))

