# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def pr(head: Optional[ListNode]) ->None:
    arr=[]
    while head:
        arr.append(head.val)
        head= head.next
    print(arr)


class Solution:    
    def mergeTwo(self,l1: Optional[ListNode], l2:Optional[ListNode])->Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy=ListNode(None)
        curr= dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next= l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr = curr.next

        if l1:
            curr.next=l1
        
        if l2:
            curr.next =l2
        
        return dummy.next
        
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        if len(lists) ==1:
            return lists[0]
        
        if len(lists) ==2:
            return self.mergeTwo(lists[0], lists[1])
        
        mid = len(lists)//2
        left=self.mergeKLists(lists[:mid])
        right=self.mergeKLists(lists[mid:])
        
        return self.mergeTwo(left, right)


            
        