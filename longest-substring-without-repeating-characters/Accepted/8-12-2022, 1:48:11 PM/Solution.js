// https://leetcode.com/problems/longest-substring-without-repeating-characters

/**
 ** Time O(n), Space(1)
 * @param {number{}} map 
 * @param {number} prevDupCharIndex 
 */
function removePrevValues(map, prevDupCharIndex) {
  for (let [key, value] of map.entries()) {
    if (value <= prevDupCharIndex) map.delete(key);
  }
}

/**
 * * Time O(n ^ 2), Space O(n)
 * @param {string} s
 * @return {number}
 */
function lengthOfLongestSubstring(s) {
  let len = 0;
  let map = new Map();

  for (let i = 0; i < s.length; i++) {
    if (map.has(s[i])) {
      let prevDupCharIndex = map.get(s[i]);
      removePrevValues(map, prevDupCharIndex);
      map.set(s[i], i);
    } else {
      map.set(s[i], i);
    }

    if (map.size > len) len = map.size;
  }

  return len;
}