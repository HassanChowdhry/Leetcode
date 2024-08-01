// https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences

/**
 * @param {string} s
 * @return {boolean}
 */
var areOccurrencesEqual = function(s) {
       let occurences = [];
    let occurMap = new Map();

    for(let c of s) {
        if (occurMap.has(c))
 occurMap.set(c, occurMap.get(c) + 1);       
        else
            occurMap.set(c, 1);
    }

    for (let n of occurMap.values()) {
        occurences.push(n);
    }

    for (let i = 0; i < occurences.length - 1; i++) {
        if (occurences[i] !== occurences[i+1])
            return false;
    }
    return true
};