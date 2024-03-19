# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current_l1 = l1
        current_l2 = l2
        l1_list, l2_list = [], []    

        # Convert both LinkedLists to Python Lists
        while current_l1 is not None or current_l2 is not None:            
            if current_l1 is not None:
                l1_list.append(str(current_l1.val))
                current_l1 = current_l1.next

            if current_l2 is not None:
                l2_list.append(str(current_l2.val))
                current_l2 = current_l2.next

        l1_list.reverse() # Reverse lists e.g. [2, 4, 3] -> [3, 4, 2]
        l2_list.reverse() # Reverse lists e.g. [2, 4, 3] -> [3, 4, 2]

        # Convert the lists to integers. e.g. [3, 4, 2] -> 342
        l1_value = int(''.join(l1_list))
        l2_value = int(''.join(l2_list))      

        sum_values = l1_value + l2_value
        sum_values = str(sum_values)

        # Create the head node
        head = ListNode(sum_values[-1])
        current = head

        # Insert the elements to LinkedList in reverse order
        for digit in sum_values[-2::-1]:
            current.next = ListNode(digit)
            current = current.next
        return head