function quickSort(arr, low, hi) {
  if (low >= hi) {
    return;
  }

  let start = low;
  let end = hi;
  let pVot = arr[parseInt((start + end) / 2)]

  // left

  while (start <= end) {
    while (arr[start] < pVot) {
      start++;
    }
    while (arr[end] > pVot) {
      end--;
    }

    if (start <= end) {
      let temp = arr[start];
      arr[start] = arr[end];
      arr[end] = temp;
      start++;
      end--;
    }
  }

  // left array sorting
  quickSort(arr, low, end);

  // right array sorting
  quickSort(arr, start, hi);


  return arr
}

let arr = [11, 10, 8, 2, 5, 1];
const sortedArray = quickSort(arr, 0, arr.length - 1);

console.log(sortedArray)
