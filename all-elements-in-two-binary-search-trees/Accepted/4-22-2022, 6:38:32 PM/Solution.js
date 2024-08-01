// https://leetcode.com/problems/all-elements-in-two-binary-search-trees

/**
 * 
 * @param {*} root1 
 * @param {*} array 
 */
function dfs1(root1, array) {
  if (!root1) {
    return root1;
  } 

  dfs1(root1.left, array);
  array.push(root1.val);
  dfs1(root1.right, array);

  return array;
}

/**
 * 
 * @param {*} root1 
 * @param {*} array 
 */
function dfs2(root2, array) {
  if (!root2) {
    return root2;
  } 

  dfs2(root2.left, array);
  array.push(root2.val);
  dfs2(root2.right, array);

  return array;
}

/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {number[]}
 */
function getAllElements(root1, root2) {
  let array = [];
  dfs1(root1, array);
  dfs2(root2, array);
  return array.sort((a, b) => a - b);
}
