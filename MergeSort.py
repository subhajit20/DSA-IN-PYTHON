arr1 = [1,5,7,99]
arr2 = [3,10,26,66,69,100]
newarr = []
def merge(arr1,arr2,newarr):
    i = 0
    j = 0
    while i <= len(arr1)-1 and j <= len(arr2)-1:
        if arr1[i] < arr2[j]:
            newarr.append(arr1[i])
            i = i + 1
        elif arr1[i] > arr2[j]:
            newarr.append(arr2[j])
            j = j + 1
        
    while i <= len(arr1)-1:
            newarr.append(arr1[i])

            i = i + 1
    while j <= len(arr2)-1:
        newarr.append(arr2[j])
        j = j + 1

    return newarr

newarr1 = merge(arr1,arr2,newarr)
print(newarr1)