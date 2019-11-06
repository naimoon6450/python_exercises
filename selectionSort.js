const selectSort = arr => {
  let minInd = 0,
    slow = 0,
    fast = 1;

  while (slow < arr.length - 1) {
    // if fast is less than current min
    if (arr[fast] < arr[minInd]) {
      minInd = fast;
    }

    // if fast hits the end, swap AND reset
    if (fast === arr.length - 1) {
      // swap
      let temp = arr[slow];
      arr[slow] = arr[minInd];
      arr[minInd] = temp;
      // increment slow
      slow++;
      // change minInd
      minInd = slow;
      // change fast
      fast = slow + 1;
    } else {
      fast++;
    }
  }

  return arr;
};

// m = 3
// 5, 3, 4, 1, 2
// s           f
//          m

// m = 4
// 1, 3, 4, 5, 2
//    s        f
//             m

// m = 4
// 1, 2, 4, 5, 3
//          s  f
//          m

console.log(selectSort([0, 2, 34, 22, 10, 19, 17]));
