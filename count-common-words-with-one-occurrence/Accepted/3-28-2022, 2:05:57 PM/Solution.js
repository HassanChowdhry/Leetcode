// https://leetcode.com/problems/count-common-words-with-one-occurrence

/**
 * @param {string[]} words1
 * @param {string[]} words2
 * @return {number}
 */
var countWords = function(words1, words2) {
     let map = new Map();
  let commonWords = 0;

  for (let word of words1) {
    
    if (map.has(word)) {
      map.set(word, map.get(word) + 1);
      
    } else map.set(word, 1);

  }

  for (let word of words2) {

    if (map.get(word) === 0) {
      map.set(word, map.get(word) - 1);
      commonWords -= 1;
    }

    if (map.get(word) === 1) {
      map.set(word, map.get(word) - 1);
      commonWords += 1;
    }
  }

  return commonWords;
}