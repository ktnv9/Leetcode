
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self, input_list):
        self.head = None
        self.num_elements = len(input_list)
        self._createLinkedList(input_list)

    def _createLinkedList(self, input_list):

        for index, value in enumerate(input_list):
            current_node = ListNode(value)
            if not index:
                self.head = current_node
            if index:
                prev_node.next = current_node
            
            prev_node = current_node

    def display(self):

        disp_list = []
        current = self.head
        while current:
            disp_list.append(current.val)
            current = current.next
        print(disp_list)

    def reverse_between(self, left, right):

        if left < 1 or left >= right or right > self.num_elements:
            return
        
        current_pos = 1
        previous, current, next = None, self.head, self.head.next
        while current_pos <= right:
            
            if current_pos > left:
                current.next = previous # reverse the link
            
            if current_pos == left:
                previous_left = previous
                current_left = current
            
            previous, current, next = current, next, next.next
            current_pos += 1

        previous_left.next = previous
        current_left.next = current
        

L = [1,2,3,4,5,6]
LL = LinkedList(L)
#LL.display()

L = [1,2,3,4,5]
left = 2
right = 4

L = [5]
left = 1
right = 1
head = LinkedList(L)
head.display()
head.reverse_between(left, right)
head.display()