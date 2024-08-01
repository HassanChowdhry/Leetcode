// https://leetcode.com/problems/valid-palindrome

/**
 * 
 * @param {*} char 
 * @returns 
 */
function isAlphaNum(char) {
  let code = char.charCodeAt(0);
  return (code >= 48 && code <= 57) 
  || (code >= 65 && code <= 90)
  || (code >= 97 && code <= 122);
}

/**
 * Time O(n), Space O(1)
 * @param {string} s
 * @return {boolean}
 */
function isPalindrome(s) {
  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    if (!isAlphaNum(s[left])) {
      left++;
    } else if (!isAlphaNum(s[right])) {
      right--;
    } else if (s[left].toLowerCase() === s[right].toLowerCase()){
      left++;
      right--;
    } else {
      return false;
    }
  }

  return true;
}