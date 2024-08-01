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
  
  let set = new Set();
  set.add('a').add('e').add('i').add('o').add('u');

  for (let i = 0; i < s.length / 2; i++) {
    if (set.has(a[i].toLowerCase())) {
      vowelsInA++;
    }
    if (set.has(b[i].toLowerCase())) {
      vowelsInB++;
    }

  }
 
  return (vowelsInA === vowelsInB);
};