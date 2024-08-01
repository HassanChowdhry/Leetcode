// https://leetcode.com/problems/longest-substring-without-repeating-characters

    /**
     * @param {string} s
     * @return {number}
     */
    var lengthOfLongestSubstring = function(s) {
let len = 0;
  let map = new Map();

  for (let i = 0; i < s.length; i++) {
    if (map.has(s[i])) {
      let prevChar = map.get(s[i]);
      for (let [key, value] of map.entries()) {
        if (value <= prevChar) map.delete(key);
      }

      map.set(s[i], i);
    } else {
      map.set(s[i], i);
    }

    if (map.size > len) len = map.size;
  }

  return len;
    }