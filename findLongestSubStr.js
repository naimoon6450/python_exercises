/**
 * Outputs length of longest distinct substr
 *
 * 'ashui iuelpoj op'
 */

function findLongestSubstring(str) {
  // add whatever parameters you deem necessary - good luck!
  let max = 0;
  let fast = 0;
  let slow = 0;
  let dict = {};

  while (fast < str.length) {
    let currChar = str[fast];
    // if the currChar is in the dictionary, then stop and reset, set max length
    if (dict[currChar]) {
      max = fast - slow;
      slow = fast;
      dict = {};
    } else {
      dict[currChar] = 1;
    }
    // else move fast and continue the checks
    fast++;
  }
  console.log(max);
}

findLongestSubstring('ashuiiuelpojop');
