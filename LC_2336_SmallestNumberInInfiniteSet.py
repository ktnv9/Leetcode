class  SmallestInfiniteSet:

	def __init__(self):

		self._heap = []

	def addBack(self, num):
		
		heap = self._heap

		if num in heap:
			return

		heap.append(num)
		heap_size = len(heap)

		current = heap_size-1
		parent = math.ceil(current/2)-1

		while current > 0 and heap[parent] > heap[current]:
			
			# swap elements		 
			A[current], A[parent] = A[parent], A[current]
			
			current = parent
			parent  = math.ceil(current/2)-1

	def pop_smallest(self):

		heap = self._heap
		heap_size = len(heap)

		smallest_element = heap[0]
		heap[0] = heap[heap_size-1]

		heap.pop()

		def heapify(heap, current):
		
			left, right = 2*current + 1, 2*current + 2
			
			smallest = current
			if heap[left] < heap[smallest]:
				smallest = left
			if heap[right] < heap[smallest]:
				smallest = right
			
			if not smallest == current:
				heap[smallest], heap[current] = heap[current], heap[smallest]
				current = smallest
				heapify(heap, current)

		heapify(heap, 0)
		return smallest_element

		

		