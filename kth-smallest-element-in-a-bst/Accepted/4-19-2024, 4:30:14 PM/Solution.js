// https://leetcode.com/problems/kth-smallest-element-in-a-bst

/**
 * 
 * @param {TreeNode} root 
 * @param {number} k 
 * @param {number[]} nums 
 */
function dfs2(root, k, nums) {
  if (nums.length !== k) {
    if (root.left) dfs2(root.left, k, nums);

    if (nums.length < k) nums.push(root.val);
    
    if (root.right) dfs2(root.right, k, nums);
  }
}

/**
 * * Time O(n), Space O(n)
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
function kthSmallest(root, k) {
  let nums = [];

  dfs2(root, k, nums);

  return nums[nums.length - 1];
}