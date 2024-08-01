// https://leetcode.com/problems/valid-anagram

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    
  if (s.length !== t.length)
        return false;

    let map = new Map();

    for (let c of s){
        if (map.has(c))
            map.set(c, map.get(c) + 1);
        else map.set(c, 1);    
    }
    for (let c of t) {
        if (!map.has(c)) 
            return false;
        else {
         map.set(c, map.get(c) -1);
        }   
    }
    for (let num of map.values()) {
        if (num !== 0)
            return false;
    }
    return true;
};