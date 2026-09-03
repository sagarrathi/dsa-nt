# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        c1= list1
        c2= list2
        
        merge=ListNode(None)
        start= merge

        while c1 and c2:
            if(c1.val<c2.val):
                merge.next=ListNode(c1.val)
                merge = merge.next
                c1=c1.next
            else:
                merge.next=ListNode(c2.val)
                merge= merge.next
                c2=c2.next
        
        if c1:
            merge.next= c1

        if c2:
            merge.next= c2
            
        return start.next
        
        