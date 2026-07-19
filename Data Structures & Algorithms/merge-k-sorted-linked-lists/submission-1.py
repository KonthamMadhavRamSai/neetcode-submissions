class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        newlist = lists[0]

        for i in range(1, len(lists)):
            newlist = self.mergeTwoLists(newlist, lists[i])

        return newlist

    def mergeTwoLists(self, list1, list2):
        temp1 = list1
        temp2 = list2

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        dummy = ListNode()
        curr = dummy

        while temp1 and temp2:
            if temp1.val < temp2.val:
                curr.next = ListNode(temp1.val)
                temp1 = temp1.next
            else:
                curr.next = ListNode(temp2.val)
                temp2 = temp2.next

            curr = curr.next

        while temp1:
            curr.next = ListNode(temp1.val)
            curr = curr.next
            temp1 = temp1.next

        while temp2:
            curr.next = ListNode(temp2.val)
            curr = curr.next
            temp2 = temp2.next

        return dummy.next