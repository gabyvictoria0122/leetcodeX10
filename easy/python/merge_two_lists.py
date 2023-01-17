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


list1 = [1,2,4]
list2 = [1,3,4]

