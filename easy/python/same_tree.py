#  Link exercício:
#    https://leetcode.com/problems/same-tree/

#  Obj:
#    Verificar se as arvores são iguais

#  Críterios:
#   Estrutura identica;
#   Nós do mesmo valor;

# Definition for a binary tree node.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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
 
#para testar o códifo na IDE 
def criarListaNode(input):
    final = atual = TreeNode
    for x in input:
        atual.next = TreeNode(x)
        atual = atual.next
    lista_node = final.next
    return lista_node 

# Essa função pega uma lista node e devolve uma lista comum em python
def voltaArray(lista_node):
    lista = []
    while lista_node is not None:
        lista.append(lista_node.val)
        lista_node = lista_node.next
        print(lista)
    return lista

p = [1,2,3]
q = [1,2,3]
p_node = criarListaNode(p)
q_node = criarListaNode(q)
resultado_esperado = True
print(Solution().isSameTree(p=p_node, q=q_node), resultado_esperado)