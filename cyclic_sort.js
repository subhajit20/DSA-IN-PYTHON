let unsortedArray = [5,4,3,2,1,10,6];

function cyclic_sort(unsortedArray){
  let i = 0;
  while (i <= unsortedArray.length - 1) {
    let currentValue = unsortedArray[i];
    let currentIndex = i + 1;
    if (currentValue !== currentIndex) {
      if (currentValue > unsortedArray.length - 1) {
        i++;
      } else {
        swap(unsortedArray,currentIndex,currentValue)
      }
    } else {
      i++;
    }
  }
}

function swap(arr,currentIndex,currentValue){
  let temp = arr[currentValue-1];
  arr[currentValue-1] = currentValue;
  arr[currentIndex - 1] = temp;
}

cyclic_sort(unsortedArray);

console.log(unsortedArray);
