// https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences

/**
 * @param {string} s
 * @return {boolean}
 */
var areOccurrencesEqual = function(s) {
    let occurMap = new Map();

    for(let c of s) {
        if (occurMap.has(c))
            occurMap.set(c, occurMap.get(c) + 1);
        else
            occurMap.set(c, 1);
    }

    let occ = occurMap.values().next().value;

    for (let n of occurMap.values()) {
        if (n !== occ)
            return false;
    }

    return true;
};