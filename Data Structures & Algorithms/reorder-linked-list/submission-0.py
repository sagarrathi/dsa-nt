# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def pr(head: Optional[ListNode])-> None:
    
    arr=[]
    while head:
        arr.append(head.val)
        head= head.next
    print(arr)

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next
        while fast and fast.next:
            slow=slow.next
            fast= fast.next.next

        right = slow.next
        slow.next = None #truncate
        left = None

        while right :
            temp= right.next
            right.next=left
            left=right
            right= temp

        first, second = head, left

        while second:
            tmp1 = first.next
            first.next= second
            tmp2=second.next
            second.next=tmp1
            second=tmp2
            first = tmp1
        
        # pr(first)
        # pr(second)
        


        