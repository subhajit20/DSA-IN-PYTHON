# mylist = [10,20,30]

# m = iter(mylist)
# print(next(m))
# print(next(m))
# print(next(m))

# Custom iterator
class ListIterator:
  def __init__(self,*initiallist):
    self.mylistlist = initiallist

  def __iter__(self):
    self.index = 0
    return self

  def __next__(self):
    if self.index <= len(self.mylistlist)-1:
      result = self.mylistlist[self.index]
      self.index += 1
      return result
    else:
          raise StopIteration

lists = ListIterator(12,32,43,54,75)
m = iter(lists)
print(m.__next__())
print(m.__next__())
print(m.__next__())
