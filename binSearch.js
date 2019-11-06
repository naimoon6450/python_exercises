function binarySearch(sortedArr, target) {
  // add whatever parameters you deem necessary - good luck!
  let low = 0,
    high = sortedArr.length - 1,
    mid = Math.floor((high - low) / 2);

  while (low <= high && sortedArr[mid] !== target) {
    if (sortedArr[mid] > target) {
      // too high so bring high to mid - 1
      high = mid - 1;
    } else {
      // too low so bring low to mid + 1
      low = mid + 1;
    }
    // recalculate
    mid = Math.floor((high - low) / 2);
  }

  if (sortedArr[mid] === target) {
    return mid;
  }

  return -1;
}

// 1, 5, 8, 10, 12, 15 => 8
// m    lh

console.log(binarySearch([1, 5, 8, 10, 12, 15], 8));
