# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# # Step 1: Create all nodes individually
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)

# # Step 2: Link nodes sequentially
# node1.next = node2
# node2.next = node3
# node3.next = node4

# # Step 3: Create a cycle: node4.next points to node2 (index = 1)
# node4.next = node2

# # node1 is the head of the linked list
# head = node1

# def detect_cycle(head):
#     my_set = set()
#     cur = head
#     while cur:
#         if cur.next is None:
#             return False , my_set
#         if str(cur) + str(cur.next) not in my_set:
#             my_set.add(str(cur) + str(cur.next))
#         else:
#             return True , my_set
#         cur = cur.next
#     return False , my_set

# print(detect_cycle(head))


# ====================================================================

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# from typing import Optional

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         visited = set()
#         current = head

#         while current:
#             if current in visited:
#                 return True
#             visited.add(current)
#             current = current.next

#         return False
