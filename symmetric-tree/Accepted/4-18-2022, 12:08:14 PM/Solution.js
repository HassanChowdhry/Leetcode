// https://leetcode.com/problems/symmetric-tree

function symmetricTree(leftRoot, rightRoot) {
  if (!leftRoot || !rightRoot) {
    return (leftRoot === rightRoot);
  } 
  
  if (leftRoot.val !== rightRoot.val) {
    return false;
  }

    return (symmetricTree(leftRoot.left, rightRoot.right) && symmetricTree(leftRoot.right, rightRoot.left));

}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
function isSymmetric(root) {
  if (!root) {
    return true;
  } 
 
  return symmetricTree(root.left, root.right);
}
