// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters

/**
 * @param {string} s
 * @return {number}
 */
var countGoodSubstrings = function(s) {
  let map = new Map();
  let count = 0;

  for (let i = 0; i <= s.length; i++) {
    if (i >= 3) {
      
      if (map.size === 3) {
        count++;
      }

      if (map.get(s[i - 3]) > 1) {
        map.set(s[i - 3], map.get(s[i - 3]) - 1);
    
      } else {
        map.delete(s[i - 3]);
      }

    } 

    if (map.has(s[i])) {
      map.set(s[i], map.get(s[i]) + 1);

    } else {
      map.set(s[i], 1);
    }

  }

  return count;
}