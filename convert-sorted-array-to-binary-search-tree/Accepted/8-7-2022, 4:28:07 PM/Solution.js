// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree


function treeMaker(nums, left, right) {
  if (left > right) return null;

  let middle = Math.floor((left + right) / 2); 
  let root = new TreeNode(nums[middle]);
  root.left = treeMaker(nums, left, middle - 1);
  root.right = treeMaker(nums, middle + 1, right);

  return root;
}
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
function sortedArrayToBST(nums) {
  let left = 0;
  let right = nums.length - 1;

  return treeMaker(nums, left, right);
}
