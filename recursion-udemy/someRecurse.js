// SAMPLE INPUT / OUTPUT
const isOdd = val => val % 2 !== 0;

// base case if array is empty
// return odd or true

function someRecursive(arr, func) {
  // add whatever parameters you deem necessary - good luck!
  // if reaches the end return false
  if (arr.length === 0) {
    return false;
  }
  // if there's anything true return immediately
  if (func(arr[0])) {
    return true;
  }

  // continue recrusing
  return someRecursive(arr.slice(1), func);
}

// console.log(someRecursive([1, 2, 3, 4], isOdd)); // true
// someRecursive([4, 6, 8, 9], isOdd); // true
console.log(someRecursive([4, 6, 8], isOdd)); // false
// someRecursive([4,6,8], val => val > 10); // false
