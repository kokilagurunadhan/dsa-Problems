# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        curr=s
        prev=None

        while curr:
            
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        p1=head
        p2=prev

        while p2:
            if p1.val!=p2.val:
                return False
            p1=p1.next
            p2=p2.next
        return True
        