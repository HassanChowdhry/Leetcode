// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters

var countGoodSubstrings = function(s) {
    const lookup = new Map();
    const windowSize = 3;
    
    let answer = 0;
    let left = 0;
    let right = 0;
    
    while(right < s.length) {
        const rightChar = s[right];
        const val = lookup.get(rightChar) || 0;
        
        lookup.set(rightChar, val + 1);
        
        if (right - left + 1 < windowSize) {
            right += 1;
            
            continue;
        }
        
        if (lookup.size === windowSize) answer += 1;
        
        // update map
        const leftChar = s[left];
        lookup.set(leftChar, lookup.get(leftChar) - 1);
        if (lookup.get(leftChar) === 0) {
            lookup.delete(leftChar);
        }
        
        // move window
        left += 1;
        right += 1;
    }
    
    return answer;
};