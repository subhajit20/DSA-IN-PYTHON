# Counting sort algorithm

def Counting_Sort(arr):
    empty_arr = []

    max = arr[0]
    for i in range(0,len(arr)):
        if max < arr[i]:
            max = arr[i]
            empty_arr = [0] * (max+1)

    for n in range(0,len(arr)):
        m = 1
        if empty_arr[arr[n]] == 0:
            empty_arr[arr[n]] = m
        elif empty_arr[arr[n]] > 0:
            m = empty_arr[arr[n]] + 1
            empty_arr[arr[n]] = m
            
    n = 0
    for i in range(0,len(empty_arr)):
        if empty_arr[i] != 0:
            while n <= len(arr)-1 and empty_arr[i] != 0:
                if empty_arr[i] == 0:
                    break
                arr[n] = i
                n = n + 1
                empty_arr[i] = empty_arr[i] - 1

    return arr

arr = [6,2,8,4]
newarr = Counting_Sort(arr) 
print(arr) # sorted array => [2,4,6,8]