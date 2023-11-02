let uArray = [5, 4, 3, 2, 1, 0];


function cyclic_sort(arr) {
    let i = 0;

    while (i <= arr.length - 1) {
        let correct = arr[i];
        let currentIndex = i;

        if (arr[i] !== arr[correct] && correct <= arr.length - 1) {
            swap(arr, currentIndex, correct);
        } else {
            i++;
        }
    }
}

const swap = (arr, currentIndex, currentValue) => {
    let temp = arr[currentValue];
    arr[currentValue] = currentValue;
    arr[currentIndex] = temp
}

cyclic_sort(uArray)
console.log(uArray)