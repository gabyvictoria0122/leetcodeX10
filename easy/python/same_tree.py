#  Link exercício:
#    https://leetcode.com/problems/same-tree/

#  Obj:
#    Verificar se as arvores são iguais

#  Críterios:
#   Estrutura identica;
#   Nós do mesmo valor;

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None : # Same Tree
            return True
        if p == None or q == None : # Different Size
            return False
        if p.val != q.val : # Different Nodes 
            return False
        # Recursividade, função vai ficar repetindo mas com os valores de left e right para sabermos se são iguais. 
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)     
