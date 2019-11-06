function isPalindrome(str) {
  // add whatever parameters you deem necessary - good luck!
  function helper(strToRev) {
    if (strToRev.length === 0) {
      return '';
    }
    return strToRev[strToRev.length - 1].concat(
      helper(strToRev.slice(0, strToRev.length - 1))
    );
  }

  return helper(str) === str ? true : false;
}

function isPalindromeOther(str) {
  if (str.length === 1) return true;
  if (str.length === 2) return str[0] === str[1];
  // bubbles inwards to check if last letter is same as first letter until it reaches the end
  /**
   * camac
   * c === c
   * ama
   * a === a
   * m
   * true
   */
  // bubbles up the true return value to the top
  if (str[0] === str.slice(-1)) return isPalindromeOther(str.slice(1, -1));
  return false;
}
// isPalindrome('awesome') // false
// isPalindrome('foobar') // false
// isPalindrome('tacocat') // true
isPalindromeOther('amanaplanacanalpanama'); // true

// console.log(isPalindrome('amanaplanacanalpandemonium')); // false
