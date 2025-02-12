
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class List:
    
    def __init__(self, list_node_vals):
        self.head = self._create_list(list_node_vals)
    
    def _create_list(self, list_node_vals):
        
        if list_node_vals == []:
            return None
        
        next_node = None
        for indx in range(len(list_node_vals)-1,-1,-1):
            node = ListNode(list_node_vals[indx], next_node)
            next_node = node
        return node

    def display(self):
        L = []
        curr = self.head
        while curr is not None:
            L.append(curr.val)
            curr = curr.next
        print(L)

    def deleteMiddle(self):

        sp, fp, prev = self.head, self.head, None

        if self.head is not None:

            while fp is not None:
                if fp.next is not None:
                    fp = fp.next.next
                    prev = sp
                    sp = sp.next
                else:
                    break
            if prev is not None:
                prev.next = sp.next
            else:
                self.head = None
                
        
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
