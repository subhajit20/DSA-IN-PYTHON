def Binary_Search(mylist,item):
    low = mylist[0]
    heigh = len(mylist)
    while low <= heigh:
        mid = int((low+heigh)/2)
        if mylist[mid] == item:
            return mid;
        elif item > mylist[mid]:
            low = mid + 1
        elif item < mylist[mid]:
            heigh = mid - 1
            
        
    return -1


mylist = [2,9,17,23,56,67,72,110,230]
result = Binary_Search(mylist,210)

if result == -1:
    print("Element is not found...")
else:
    print("Element is found...")