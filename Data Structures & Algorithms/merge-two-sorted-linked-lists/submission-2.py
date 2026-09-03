# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        c1= list1
        c2= list2
        
        node=start =ListNode(None)

        while c1 and c2:
            if(c1.val<c2.val):
                node.next=c1
                c1=c1.next
            else:
                node.next=ListNode(c2.val)
                c2=c2.next
            node=node.next
        
        if c1:
            node.next= c1

        if c2:
            node.next= c2
            
        return start.next
        
        