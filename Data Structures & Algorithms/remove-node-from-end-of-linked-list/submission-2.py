# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        if n>count:
            return None

        count=count-n
        if count==0:
            return head.next
        
        i=0
        prev=None
        temp=head
        while i<count:
            i+=1
            prev=temp
            temp=temp.next
        prev.next=temp.next
        return head

        