// https://leetcode.com/problems/determine-if-string-halves-are-alike

/**
 * @param {string} s
 * @return {boolean}
 */
var halvesAreAlike = function(s) {
     let a = s.slice(0, s.length / 2);
  let b = s.slice(s.length / 2, s.length);
  
  let vowelsInA = 0;
  let vowelsInB = 0;

  for (let c of a) {
    if (c === 'a' || c === 'e' || c === 'i' || c === 'o' || c === 'u' || c === 'A' || c === 'E' || c === 'I' || c === 'O' || c === 'U') {
      vowelsInA++;
    }
  }

  for (let c of b) {
    if (c === 'a' || c === 'e' || c === 'i' || c === 'o' || c === 'u' || c === 'A' || c === 'E' || c === 'I' || c === 'O' || c === 'U') {
      vowelsInB++;
    }
  }
  return (vowelsInA === vowelsInB);
};