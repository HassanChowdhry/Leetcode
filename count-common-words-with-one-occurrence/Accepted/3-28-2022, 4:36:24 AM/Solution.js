// https://leetcode.com/problems/count-common-words-with-one-occurrence

/**
 * @param {string[]} words1
 * @param {string[]} words2
 * @return {number}
 */
var countWords = function(words1, words2) {
     
  let map1 = new Map();
  let map2 = new Map();
  let commonWords = 0;

  for (let word of words1) {
    
    if (map1.has(word)) {
      map1.set(word, map1.get(word) + 1);
      
    } else map1.set(word, 1);

  }

  for (let word of words2) {
    
    if (map2.has(word)) {
      map2.set(word, map2.get(word) + 1);
      
    } else map2.set(word, 1);

  }
    
  for (let [key, value] of map1.entries()) {
    if (value === 1) {
    
      if (map2.has(key)) {
    
        if (map2.get(key) === value) {
          commonWords += 1;
        }
      }
    }
  }

  return commonWords;
}