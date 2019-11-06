const bubble = arr => {
  for (let i = 0; i < arr.length - 1; i++) {
    // realize that the inner loop is going to bubble the value to the end
    // can add a boolean here to stop if already sorted by checking to see if there are any swaps being made
    let swapped = false;
    for (let j = 0; j < arr.length - 1 - i; j++) {
      if (arr[j] > arr[j + 1]) {
        let temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        swapped = true;
      }
    }
    if (!swapped) {
      break;
    }
  }
  return arr;
};

console.log(bubble([7, 1, 5, 2, 0, 10]));
