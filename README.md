***************** Linear Search and Binary Search *******************

If the array is sorted then we will go with binary search because it consumes less time than linear search.

Rule ------
1. we need to take out the low index, height index, and mid-index of the array 
2.  Taking out the mid index simply we need to do that we need to add the two indexes like mid = (low+height)/2, which gives the mid-range.
3.  we need to make a while loop and inside the while loop we will make the main login
4.  if the item is greater than the middle element of the list then, we need to store the middle range into the low variable like this low = mid + 1
5. And the same thing will happen if the item is less than the middle element of the list or array, then we need to store the middle index into the heigh variable like this heigh = mid - 1
6.  And the last thing is that when the element will is the same as the middle item then it will return  +1 otherwise come out from the while loop and return -1