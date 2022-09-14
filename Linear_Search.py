def Liner_Search(mylist,element):
    if len(mylist) == 0:
        return "List is empty..."
    for i in mylist:
        if i == element:
            return i
    return -1

result = Liner_Search([1,2,13],3)

if result == -1:
    print("Element is not present in List")
else:
    print("Element is present in List")