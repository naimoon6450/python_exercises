const mergeDivide = arr => {
  // divide some array into equal portions
  let mid = Math.floor((arr.length - 1) / 2);
  let left = arr.slice(0, mid + 1);
  let right = arr.slice(mid + 1);
  return [left, right];
};

const sortedArrReducer = (sa1, sa2) => {
  let combined = [],
    pt1 = 0,
    pt2 = 0;

  // continue looping until the pointers reach the end
  while (pt1 < sa1.length && pt2 < sa2.length) {
    if (sa1[pt1] < sa2[pt2]) {
      combined.push(sa1[pt1]);
      pt1++;
    } else {
      combined.push(sa2[pt2]);
      pt2++;
    }
  }

  return combined.concat(sa1.slice(pt1), sa2.slice(pt2));
};
// [1, ]
// [1, 3, 9]    [4, 10, 11, 12]
//        p1        p2
// console.log(sortedArrReducer([1, 3, 9], [4, 10, 11, 12]));

const mergeSort = arr => {
  if (arr.length < 2) {
    return arr;
  }

  const divArr = mergeDivide(arr);
  let left = divArr[0];
  let right = divArr[1];
  // if arr length isn't 1, then continue to divde
  // if it is 1 then merge them recursively
  return sortedArrReducer(mergeSort(left), mergeSort(right));
};

console.log(mergeSort([6, 1, 9, 2, 10, 0]));

// 6, 1, 9, 2, 10, 0
// left = [6, 1, 9]
// right = [2, 10, 0]
// sAR ( [1,6,9], ms (2,10,0))

// ms (6,1,9)
// left = [6, 1]
// right = [9]
// sAR ( [1, 6], [9])

// ms (6,1)
// left = [6]
// right = [1]
// sAR (ms (6), ms (1)) => sAR (6, 1) => [1, 6]

// ms (6)
// return 6
// ms (1)
// return 1
