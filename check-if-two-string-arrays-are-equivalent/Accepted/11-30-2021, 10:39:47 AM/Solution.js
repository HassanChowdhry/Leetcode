// https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent

/**
 * @param {string[]} word1
 * @param {string[]} word2
 * @return {boolean}
 */
var arrayStringsAreEqual = function(word1, word2)
{
     if (word1.join('') === word2.join('') )
        {
            return true;
        }
        else return false;
};