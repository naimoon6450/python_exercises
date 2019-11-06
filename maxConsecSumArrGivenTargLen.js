function maxSubarraySum(arr, numLen) {
  // add whatever parameters you deem necessary - good luck!
  // find sum of first numLen elems
  if (numLen > arr.length) {
    return null;
  }

  let maxSum = 0;
  for (let i = 0; i < numLen; i++) {
    maxSum += arr[i];
  }
  //   problem now is the maxSum should be same as tempSum not the maxSum
  // now start the sliding
  let tempSum = maxSum;
  for (let j = numLen; j < arr.length; j++) {
    tempSum += arr[j] - arr[j - numLen];
    maxSum = Math.max(tempSum, maxSum);
  }
  console.log(maxSum);
  return maxSum;
}

maxSubarraySum([-3, 4, 0, -2, 6, -1], 2);
