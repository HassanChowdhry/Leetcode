// https://leetcode.com/problems/leaf-similar-trees

/**
 * 
 * @param {TreeNode} root 
 * @return {Number[]}
 */
function dfsPost(root, leafs) {
  if (!root) {
    return root;
  }

  dfsPost(root.left, leafs);
  dfsPost(root.right, leafs);
  if (!root.left && !root.right) {
    leafs.push(root.val);
  }

}

/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
function leafSimilar(root1, root2) {
  let leafs1 = [];
  let leafs2 = [];

  dfsPost(root1, leafs1);
  dfsPost(root2, leafs2);

  if (leafs1.length !== leafs2.length) return false;

  for (let i = 0; i < leafs1.length; i++) {
    if (leafs1[i] !== leafs2[i]) return false;
  }

  return true;
}