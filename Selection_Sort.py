arr = [26,23,10,2,18]

i = 0

while i <= len(arr)-1:
    min = i
    for t in range(i+1,len(arr)):
        if arr[min] > arr[t]:
            min = t
    temp = arr[i]
    arr[i] = arr[min]
    arr[min] = temp
    i = i + 1
print(arr)