class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        
        """
        if not list1:
            return list2
        if not list2:
            return list1

        result_list = ListNode(0)
        head_list = result_list

        while list1 and list2:
            if list1.val >= list2.val:
                result_list.next = list2
                list2 = list2.next
            else:
                result_list.next = list1
                list1 = list1.next 
            result_list= result_list.next

        if not list1 and list2:
            result_list.next = list2
        elif not list2 and list1:
            result_list.next = list1
        return head_list.next     