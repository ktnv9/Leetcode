
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

    def deleteMiddle(self):

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
                
        
'''
list_node_vals = [1,2,3,4]
head = List(list_node_vals)
print("Before")
head.display()
head.deleteMiddle()
print('After')
head.display()

list_node_vals = [1,3,4,7,1,2,6]
head = List(list_node_vals)
print("Before")
head.display()
head.deleteMiddle()
print('After')
head.display()
'''
list_node_vals = [1,2,3,4]
head = List(list_node_vals)
print("Before")
head.display()
head.deleteMiddle()
print('After')
head.display()
