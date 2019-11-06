// 3, 5, 4, 1, 2
//    c  f
//    i

// 3, 5, 4, 1, 2
//    c  f
//    i

const insertSort = arr => {
  for (let i = 0; i < arr.length; i++) {
    let currVal = arr[i]; // or arr[ j + 1 ]
    let j;
    for (j = i - 1; j >= 0 && arr[j] > currVal; j--) {
      arr[j + 1] = arr[j]; // arr[j] equivalent to arr[i - 1]
    }
    arr[j + 1] = currVal;
  }
  return arr;
};

const insertSortWhile = arr => {
  let curr = 0,
    fast = 1;

  while (curr < arr.length - 1) {
    // if there's a number < curr bring it up
    for (let j = fast; j >= 0 && arr[j] < arr[j - 1]; j--) {
      // initialize the current value, which will change upon loop
      let currVal = arr[curr];
      // the swapping
      arr[j - 1] = arr[j];
      arr[j] = currVal;
      // decrement curr to grab next value to update
      curr--;
    }

    // update curr to fast
    curr = fast;
    fast++;
  }
  return arr;
};

// currVal = 2
// 2, 1, 5, 22, 10, 19, 17
// c
//    f
//    j

// currVal = 17
// 1, 2, 5, 10, 17, 19, 22
//               c
//                      f
//                  j
console.log(insertSortWhile([2, 1, 5, 22, 10, 19, 17]));
// console.log(insertSort([0, 2, 34, 22, 10, 19, 17]));

// currVal = 0
//   0, 2, 34, 22, 10, 19, 17
//   i
// j

// currVal = 2
//   0, 2, 22, 34, 10, 19, 17
//              i
//      j
