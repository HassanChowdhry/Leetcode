// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers

/**
 * 
 * @param {TreeNode} root 
 * @param {number} sum 
 * @returns 
 */
function dfs(root, binString, sum) {

  if (!root) {
    return 0;
  }

  binString += root.val;

  if (!root.left && !root.right) {
    sum +=   parseInt(binString, 2);
  }

   return sum + dfs(root.right, binString, sum) + dfs(root.left, binString, sum);
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
function sumRootToLeaf(root) {
  return dfs(root, '', 0);
}
