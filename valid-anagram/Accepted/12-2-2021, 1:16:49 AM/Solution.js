// https://leetcode.com/problems/valid-anagram

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    
      let lettersOfS = [];
    let lettersOfT = [];
    if (s.length !== t.length)
    {
        return false;
    }
    for (let i = 0; i < s.length; i++)
    {
        let letterT = t.substring(i,i+1);
        let letterS = s.substring(i,i+1);
        lettersOfS.push(letterS);
        lettersOfT.push(letterT);
    }
    lettersOfS.sort();
    lettersOfT.sort();
    for (let j = 0; j < lettersOfS.length; j++)
    {
        if (lettersOfS[j] !== lettersOfT[j])
        {
            return false;
        }
    }
    return true;
};