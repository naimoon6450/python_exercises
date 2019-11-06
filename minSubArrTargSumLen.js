/**
 *
 * Given array and a targ sum, find the length of the min contig subarray that is greater than or equal to the targSum
 *
 * still sliding WINDOW
 *
 * len = 1
 * sum = 10
 * [10,  3,  1,  2,  4,  3], 7 => 2 bc [4,3]
 *      l            r
 * [4,3,3,8,1,2,3], 11 => 2 bc [3,8]
 * [3,1,7,21,62,19], 52 => 1 bc [62] is greater
 * [0,0,0,0,0,0]
 *
 * len = 5
 * sum = 9
 * [1, 2, 3, 4, 5], 11 => 3 [3,4,5]
 *           l  r
 *
 * Need to keep track of current MIN length
 */

function minSubArrayLen(arr, targSum) {
  let minLen = Infinity,
    left = 0,
    right = 0,
    // intialize sum to first val in arr
    sum = arr[left];

  while (right < arr.length || left < arr.length) {
    // if we havne't reached targSum, keep moving right and add
    if (sum >= targSum) {
      // get the min length now
      minLen = Math.min(minLen, right - left + 1);
      // remove sum from the left
      sum -= arr[left];
      // move left
      left++;
    }
    // as long as right is less then arr length continue moving it
    // arr len - 1 because it will enter here on 3 and become 4
    // if it was arr len then it will enter here on 4 and become 5 which will lead to non-indexable ish
    if (right < arr.length - 1 && sum < targSum) {
      right++;
      sum += arr[right];
    }
    // what happens when it's less than targ sum though, you have to break
    // must do arr len - 1 bc right will be length of arr - 1 at most
    if (right === arr.length - 1 && sum < targSum) {
      break;
    }

    // console.log(`Right ${right} and Left ${left} sum ${sum}`);
  }
  return minLen;
}

// console.log(minSubArrayLen([1, 2, 3, 4, 5], 110)); // should be 3
// console.log(minSubArrayLen([4, 3, 3, 8, 1, 2, 3], 11));
// console.log(minSubArrayLen([10, 3, 1, 2, 4, 3], 7));
// console.log(minSubArrayLen([1, 4, 16, 22, 5, 7, 8, 9, 10], 55));

/**
 * Lesson learned here was that I didn't account for breaking out of the loop once the sum was < targetSum
 *
 * Also right would go past index
 *
 * And we only want to increment right WHEN sum is smaller than targ
 * And we only want to increment left WHEN sum is larger than targ
 */

const minSubClean = (arr, targ) => {
  let left = 0,
    minLen = Infinity,
    sum = 0;

  for (let right = 0; right < arr.length; right++) {
    sum += arr[right];

    while (sum >= targ) {
      // get min length
      minLen = Math.min(minLen, right - left + 1);
      // reduce sum
      sum -= arr[left];
      // inc left
      left++;
    }
  }

  return minLen === Infinity ? 0 : minLen;
};

console.log(minSubClean([1, 2, 3, 4, 5], 7));
