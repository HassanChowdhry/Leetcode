// https://leetcode.com/problems/leaf-similar-trees

const getLeafs = (root) => {
    if (!root) return [];
    
    const stack = [root], result = []
    while(stack.length) {
        const curr = stack.pop()
        if (!curr.left && !curr.right) result.push(curr.val)

        if (curr.left) stack.push(curr.left)
        if (curr.right) stack.push(curr.right)
    }

    return result
};

const leafSimilar = (root1, root2) => {
    if (!root1 || !root2) return false

    const root1Leafs = getLeafs(root1), root2Leafs = getLeafs(root2)

    if (root1Leafs.length !== root2Leafs.length) return false
    
    for(let i = 0; i < root1Leafs.length; i++) {
        if (root1Leafs[i] !== root2Leafs[i]) return false
    }
    
    return true
};