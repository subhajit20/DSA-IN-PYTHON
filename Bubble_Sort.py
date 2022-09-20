arr = [68, 88, 13, 51, 26, 67, 20, 99, 29, 30]

def Bubble_Sort(arr):
    for i in range(0,len(arr)):
        t = 0
        for t in range(t,len(arr)):
            m = t + 1
            key = arr[t]
            if m < len(arr):
                if arr[t] > arr[m]:
                    arr[t] = arr[m]
                    arr[m] = key
            else:
                break
    
    return "Sorted Array ---->",arr
    
new_array = Bubble_Sort(arr)

print(new_array)