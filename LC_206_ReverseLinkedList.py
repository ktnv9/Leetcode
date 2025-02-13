
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class List:
    
    def __init__(self, list_node_vals):
        self.head = self._create_list(list_node_vals)
    
    def _create_list(self, list_node_vals):
        
        if not list_node_vals:
            return None
        
        head = None
        for indx in range(len(list_node_vals)-1, -1, -1):
            head = ListNode(list_node_vals[indx], head)
        return head

    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.val)
            current = current.next
        print(nodes)

    def delete_middle(self):

        if not self.head:
            return
        
        if not self.head.next:
            self.head = None
            return

        slow, fast, prev = self.head, self.head, None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        prev.next = slow.next
                
    def odd_even_list(self):

        if not self.head:
            return

        if not self.head.next:
            return

        if not self.head.next.next:
            return

        odd = self.head
        even = self.head.next
        start_even = self.head.next

        while even and even.next:

            odd.next = even.next
            odd = odd.next

            even.next = even.next.next
            even = even.next
        
        odd.next = start_even

    def reverse(self):

        """
        # if empty list or single element list, return
        if not self.head or not self.head.next:
            return
        
        # two pointers current & next to do flip direction op & move forward.
        current = self.head
        next = self.head.next

        # move until the end of the linked list (next becomes None)
        while next:

            # flip direction operation
            temp = next.next
            next.next = current

            # move current & next
            current = next # nove current
            next = temp # move next

        # make the head point to end of the list
        self.head.next = None

        # mark the current as the new head.
        self.head = current
        """

        if not self.head or not self.head.next:
            return

        prev = None
        current = self.head
        next = self.head.next

        while next:
            
            current.next = prev
            prev = current
            current = next
            next = next.next
        
        current.next = prev
        self.head = current


        
'''
list_node_vals = [1,2,3,4]
head = List(list_node_vals)
print("Before")
head.display()
head.delete_middle()
print('After')
head.display()

list_node_vals = [1,3,4,7,1,2,6]
head = List(list_node_vals)
print("Before")
head.display()
head.delete_middle()
print('After')
head.display()
'''
list_node_vals = []
head = List(list_node_vals)
print("Before")
head.display()

# head.delete_middle()
# head.odd_even_list()

head.reverse()

print('After')
head.display()