// https://leetcode.com/problems/valid-palindrome

/**
 * 
 * @param {String} char 
 * @return {boolean}
 */
function isAlphaNum(char) {
  let code = char.charCodeAt(0);
  return (code >= 48 && code <= 57) 
  || (code >= 65 && code <= 90)
  || (code >= 97 && code <= 122);
}

function toLower(char) {
  let code = char.charCodeAt(0);
  
  if ((code >= 97 && code <= 122) || (code >= 48 && code <= 57)) {
    return code;
  } 

  return code + 32;
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
    } else if (toLower(s[left]) === toLower(s[right])) {
      left++;
      right--;
    } else {
      return false;
    }
  }

  return true;
}
