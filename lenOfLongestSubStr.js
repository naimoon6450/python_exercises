// SLIDING WINDOW
// longestsubstring => ubstring 8
// thisishowwedoit => wedoit 6
// thecatinthehat => hecatin 7

/**
 *
 * t  h  e  c  a  t  i  n  t  h  e  h  a  t
 *    l              r
 * map = { h:1, e: 1, c: 1, a: 1, t: 1, }
 *
 * l  o  n  g  e  s  t  s  u  b  s  t  r  i  n  g
 *                        p1                    p2
 * Pointer manipulation, max difference of index, hashmap to store if already visited?
 */

function findLongestSubstring(str) {
  // initialize array of chars, pointers, maxLen, and dictionary of seen chars
  let strToArr = str.split('');
  let pt1 = 0;
  let pt2 = 0;
  let dictOfSeenChars = {};
  let maxLen = 0;
  if (strToArr.length === 1) {
    return 1;
  }
  //
  while (pt1 < strToArr.length - 1 && pt2 < strToArr.length) {
    let pt1Char = strToArr[pt1];
    let pt2Char = strToArr[pt2];

    // if char is in dict, decrement the seen char in dict, increment pt1
    if (dictOfSeenChars[pt2Char] >= 0) {
      // decrement the pointer bc it's probably 1 too far and r
      pt2Char = strToArr[pt2];
      // capture new max here
      maxLen = Math.max(maxLen, pt2 - pt1);
      // set pt1 to the position of the seen char + 1 to be in front of the dupe
      pt1 = dictOfSeenChars[pt2Char] + 1;
      // put pt2 in after pt1
      pt2 = pt1;
      // reset dict
      dictOfSeenChars = {};
    } else {
      if (dictOfSeenChars[pt2Char] === undefined) {
        // add into the dict with the index of the char
        dictOfSeenChars[pt2Char] = pt2;
        // increment pt2
        pt2++;
      }
    }
    maxLen = Math.max(maxLen, pt2 - pt1);
  }
  return maxLen;
}

const findLongestSubStrOpt = str => {
  let right = 0,
    left = 0,
    maxLen = 0;
  let map = {};
  /* the map will contain all the elements already visited, so when a dupe enters, you delete the element from the map and move left pointer to the next char. For a situation like t w w o p l, when the left is at w and right is at w the map contains { w: 1 }, and when the loop enters again it sees that w is in the map and it removes it, shifts left to the w and now both r/l are on w. This will store w in the map again and continue moving forward

  IN this situation, right is still at s and sees that it's still in the map so it will move left until it deletes s from the map.

  losubstring
     l  r    
  {u:1, b:1}
  */
  const strToArr = str.split('');

  while (right < strToArr.length && left < strToArr.length) {
    let leftChar = strToArr[left];
    let rightChar = strToArr[right];
    // if the right is in the map
    if (map[rightChar]) {
      // note max
      maxLen = Math.max(maxLen, right - left);
      // remove from map increment left
      delete map[leftChar];
      left++;
    } else {
      // right is not in map, lets add it
      map[rightChar] = 1;
      right++;
    }
    maxLen = Math.max(maxLen, right - left);
  }
  return maxLen;
};

// console.log(findLongestSubStrOpt(''));
/**
 * p  w  w  k  e
 * s     i
 * map = {t: 0, h:1, e:2, c:3, ...}
 *            s     i
 *  t h e c a t i n t h e h a t
 * 0 or
 *
 *                   s         i
 * t h i s i s h o w w e d o i t
 * s=9
 *
 * Ensuring that when you're changing startsubstring can't go backwards
 * Ideally you'd want to go mapped index of dupe char + 1, but if you're already passed it, then take max between moving up 1 vs the mapped index of dupe char + 1
 *
 * {t:0, h:6, i:4, s:3, o:7, w:9}
 */

const findLongestSubStrForLoop = str => {
  let maxLen = 0;
  let startSub = 0;
  let map = {};

  const strArr = str.split('');
  for (let i = 0; i < str.length + 1; i++) {
    let char = strArr[i];
    if (map[char]) {
      startSub = Math.max(startSub, map[char] + 1);
    }
    // update map
    map[char] = i;
    maxLen = Math.max(maxLen, i - startSub);
  }
  return maxLen;
};

console.log(findLongestSubStrForLoop('longestsubstring'));
