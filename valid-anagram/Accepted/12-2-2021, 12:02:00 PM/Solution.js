// https://leetcode.com/problems/valid-anagram

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {

    let lettersOfS = s.split('');
    let lettersOfT = t.split('');

    if (s.length !== t.length)
        return false;

    lettersOfS.sort();
    lettersOfT.sort();

    for (let j = 0; j < lettersOfS.length; j++)
    {
        if (lettersOfS[j] !== lettersOfT[j])
            return false;
    }

    return true;
};