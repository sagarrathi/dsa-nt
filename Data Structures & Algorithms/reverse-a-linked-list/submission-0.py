# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
# #         self.next = next
def prit(x:Optional[ListNode]):

    cursor=x
    arr=[]
    while cursor:
        arr.append(cursor.val)
        cursor=cursor.next
    print(arr)



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        tail= None

        while head:
            backup=head.next
            head.next=tail
            tail=head
            head=backup
        
        return tail
        