// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

class Dup {

  constructor(char, occur) {
    this.char = char;
    this.occur = occur;
  }

  getChar() {
    let s = '';
    let n = this.occur;

    while (n > 0) {
      s += this.char;
      n--;
    }

    return s;
  }
}
/**
 ** Using class - Time O(n), Space O(n)
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
function removeDuplicates(s, k) {
  let stack = [];
  stack.push(new Dup(s[0], 1));

  for (let c = 1; c < s.length; c++) {
    let prevChar = stack.pop();

    if (prevChar && prevChar.char === s[c]) {
      prevChar.occur += 1;
    }

    if (prevChar && prevChar.occur !== k) {
      stack.push(prevChar);
    }

    if (!prevChar || prevChar.char !== s[c]) {
      stack.push(new Dup(s[c], 1));
    } 
  }
  let res = '';

  for (let obj of stack) {
    res += obj.getChar();
  }

  return res;
}