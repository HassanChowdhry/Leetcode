// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers

/**
 * 
 * @param {TreeNode} root 
 * @param {String} binString 
 * @param {Number[]} array 
 * @returns 
 */
function dfs(root, binString, sum) {

  if (!root) {
    return 0;
  }

  binString += root.val.toString();

  if (!root.left && !root.right) {
    sum += parseInt(binString, 2);
  }

  return sum + dfs(root.left, binString, sum) + dfs(root.right, binString, sum);

}

/**
 * *Time O(n), Space O(1)? 
 * @param {TreeNode} root
 * @return {number}
 */
function sumRootToLeaf(root) {
  return dfs(root, '', 0);
}
