// productOfArray([1,2,3]) // 6
// productOfArray([1,2,3,10]) // 60

// base case is when there's 1 element in array

const prod = arr => {
  if (arr.length === 0) {
    return 1;
  }
  return arr[0] * prod(arr.slice(1));
};

console.log(prod([1, 2, 3, 10]));
