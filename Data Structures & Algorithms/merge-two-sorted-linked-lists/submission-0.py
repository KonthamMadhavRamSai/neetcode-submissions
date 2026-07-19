# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=list1
        temp2=list2
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        newlist=ListNode()
        newhead=newlist
        while temp1 is not None and temp2 is not None:
            if temp1.val<temp2.val:
                newnode=ListNode(temp1.val)
                temp1=temp1.next
            else:
                newnode=ListNode(temp2.val)
                temp2=temp2.next
            newlist.next=newnode
            newlist=newlist.next
        if temp2:
            while temp2:
                newnode=ListNode(temp2.val)
                temp2=temp2.next
                newlist.next=newnode
                newlist=newlist.next
        if temp1:
            while temp1:
                newnode=ListNode(temp1.val)
                temp1=temp1.next
                newlist.next=newnode
                newlist=newlist.next
        return newhead.next
        

                
        