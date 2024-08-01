// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters

/**
 * @param {string} s
 * @return {number}
 */
var countGoodSubstrings = function(s) {
  let count = 0;
  let set = new Set();
  
  for (let i = 0; i < s.length - 2; i++) {
    let temp = s.slice(i, i + 3);

    for (let j = 0; j < 3; j++) {
      if (set.has(temp[[j]])) {
        break;
      }
      set.add(temp[j]);
    }

    if (set.size === 3) {
      count += 1;
    }

    set.clear();
  }

  return count;
}