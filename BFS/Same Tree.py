'''Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.'''

'''Logic behind the code:
So, we need to find if two tree are identical or not.
* First, check if p and q are none or null, then in this case both trees are same
* Second, check if any one tree is null but other one is not, then in this case both trees are different. Hence, return False
* Third, Check if current (parent node is same) and in the same tree check if the left child of both tree is same and check if the right child of both tree is same. If yes then return True.'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        return(p.val==q.val
            and self.isSameTree(p.left,q.left)
            and self.isSameTree(p.right,q.right))