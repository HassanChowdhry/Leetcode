// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers

/**
 * 
 * @param {TreeNode} root 
 * @param {number} sum 
 * @returns 
 */
function dfs(root, binString, array) {

  if (!root) {
    return root;
  }

  binString += root.val;

  if (!root.left && !root.right) {
    array[0] += parseInt(binString, 2);
  }

  dfs(root.left, binString, array);
  dfs(root.right, binString, array);

  return array;
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
function sumRootToLeaf(root) {
  let array = [0];
  dfs(root, '', array);
  return array[0];
}
