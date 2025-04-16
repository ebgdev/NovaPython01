# from llist import sllist 

# lst1 = sllist([1, 2, 4])
# lst2 = sllist([1, 3, 4])  # Removed extra brackets

# def merge_ll(lst1, lst2):
#     cur1 = lst1.first
#     cur2 = lst2.first
#     merged = sllist()
    
#     # Merge the two lists while both have nodes
#     while cur1 is not None and cur2 is not None:
#         if cur1.value <= cur2.value:
#             merged.append(cur1.value)
#             cur1 = cur1.next
#         else:
#             merged.append(cur2.value)
#             cur2 = cur2.next
    
#     # Append remaining nodes from lst1
#     while cur1 is not None:
#         merged.append(cur1.value)
#         cur1 = cur1.next
    
#     # Append remaining nodes from lst2
#     while cur2 is not None:
#         merged.append(cur2.value)
#         cur2 = cur2.next
    
#     return merged

# print(merge_ll(lst1, lst2))


# ============================================================


# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the starting point
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach the remaining elements from either list
        # current.next = list1 if list1 else list2
        if list1:
            current.next = list1
        else:
            current.next = list2

        
        # Return the merged list (skip the dummy node)
        return dummy.next
    

# Example usage:
# list1 = 1 -> 2 -> 4
# list2 = 1 -> 3 -> 4
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

solution = Solution()
merged = solution.mergeTwoLists(list1, list2)

# Print the merged list
while merged:
    print(merged.val, end=" -> ")
    merged = merged.next
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 ->