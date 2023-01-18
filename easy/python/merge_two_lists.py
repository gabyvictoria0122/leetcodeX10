#  Link exercício:
#    https://leetcode.com/problems/merge-two-sorted-lists/

#  Obj:
#    Mesclar duas listas de números

#  Críterios:
#    Mesclar em ordem crescente.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1:ListNode, list2:ListNode) -> ListNode:
        final = atual = ListNode()
        print(final)
        
        while list1 and list2:
            if list1.val <= list2.val:
                atual.next = list1
                list1 = list1.next
            else:
                atual.next = list2
                list2 = list2.next

            atual = atual.next

        if list1 != None:
            atual.next = list1
        else:
            atual.next = list2
            
        return final.next

# para testar o código na IDE 
def criarListaNode(input):
    final = atual = ListNode
    for x in input:
        atual.next = ListNode(x)
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


list1 = [1,2,4]
list2 = [1,3,4]
lista_1 = criarListaNode(list1)
lista_2 = criarListaNode(list2)
lista_node = Solution().mergeTwoLists(lista_1, lista_2)
resposta = voltaArray(lista_node)
assert resposta == [1,1,2,3,4,4]


