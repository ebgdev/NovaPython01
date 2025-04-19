class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    fast = slow = head
    stack = []

    # Push first half into stack
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    # Skip middle for odd-length lists
    if fast:
        slow = slow.next

    # Compare second half with stack
    while slow:
        if stack.pop() != slow.val:
            return False
        slow = slow.next

    return True

# --------------------------
# Test Case 1: Palindrome (1 -> 2 -> 2 -> 1)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4

print("Test Case 1:", isPalindrome(node1))  # True

# --------------------------
# Test Case 2: Not a Palindrome (1 -> 2 -> 3)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)

n1.next = n2
n2.next = n3

print("Test Case 2:", isPalindrome(n1))  # False

# --------------------------
# Test Case 3: Odd-Length Palindrome (1 -> 2 -> 1)
m1 = ListNode(1)
m2 = ListNode(2)
m3 = ListNode(1)

m1.next = m2
m2.next = m3

print("Test Case 3:", isPalindrome(m1))  # True
