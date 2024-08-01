// https://leetcode.com/problems/finding-the-users-active-minutes

/**
 * @param {number[][]} logs
 * @param {number} k
 * @return {number[]}
 */
var findingUsersActiveMinutes = function(logs, k) {
   let map = new Map();

  for (let [id, minute] of logs) {
    if (map.has(id)) {
      map.set(id, map.get(id).add(minute));

    } else {
      map.set(id, new Set());
      map.set(id, map.get(id).add(minute));
    }
  }

  let answer = new Array(k).fill(0);

  for (let value of map.values()) {
    answer[value.size - 1] += 1; 
  }     

  return answer;
}