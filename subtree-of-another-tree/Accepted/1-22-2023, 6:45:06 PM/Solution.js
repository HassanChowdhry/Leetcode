// https://leetcode.com/problems/subtree-of-another-tree

// https://leetcode.com/problems/subtree-of-another-tree/

function isEqual(root, subRoot) {
  if (root === null || subRoot === null) {
    return root === null && subRoot === null;
  }

  return root.val === subRoot.val && isEqual(root.left, subRoot.left) && isEqual(root.right, subRoot.right);
}

function dfs(root, subRoot) {
  if (!root) return false;

  if (isEqual(root, subRoot)) {
    return true;
  }
  
  let left = dfs(root.left, subRoot);
  let right = dfs(root.right, subRoot);

  return left || right;
}

/**
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
function isSubtree(root, subRoot) {
  return dfs(root, subRoot);
}

