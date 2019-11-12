/**
 * This pivotHelper does 2 things:
 * 1. Returns the index of the element that's set perfectly or its sorted position
 * 2. Places the element in the sorted position or where it would be if it was sorted
 */

const pivotHelper = (arr, start = 0, end = arr.length - 1) => {
  let piv = start; // will be used to jump the pivot
  let pivVal = arr[start];
  for (let i = start + 1; i < arr.length; i++) {
    // if the curr num is less than piv move it back
    if (arr[i] < pivVal) {
      // increment piv as there's another num to jump over
      piv++;
      // the swapping
      let temp = arr[piv];
      arr[piv] = arr[i];
      arr[i] = temp;
    }
  }
  // make the final swap
  arr[start] = arr[piv];
  arr[piv] = pivVal;
  return piv;
};

// console.log(pivotHelper([2, 1]));
// console.log(pivotHelper([9, 4, 8, 2, 1], 3));

// 5, 2, 1, 4, 8, 7, 6, 3
//         piv
//             i
// pV

const quickSort = (arr, left = 0, right = arr.length - 1) => {
  debugger;
  if (left < right) {
    // initially gets the pivot using the first number as pivot
    let piv = pivotHelper(arr, left, right); // 9
    // left side
    quickSort(arr, left, piv - 1);
    // right side
    quickSort(arr, piv + 1, right);
  }

  return arr;
};

console.log(quickSort([9, 4, 8, 8, 2, 1, 5, 7, 6, 3]));

// 9, 4, 8, 8, 2, 1, 5, 7, 6, 3
// l                          r
// pivHelper => 9
// quickSort([3, 4, 8, 8, 2, 1, 5, 7, 6, 9], 0, 8)
