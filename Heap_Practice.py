def heapify(input_array, index, array_size):
	
	# heapify method to rearrange input_array starting from given index in order to make the array maintain heap property.

	# indices of left and right children.
	left, right = 2*index + 1, 2*index + 2

	# check which among the left, right, current index have the maximum value
	next_index = index
	if left < array_size and input_array[left] > input_array[next_index]:
		next_index = left
	if right < array_size and input_array[right] > input_array[next_index]:
		next_index = right
	
	# swap the current element with the max element.
	if not next_index == index:
		input_array[index], input_array[next_index] = input_array[next_index], input_array[index]

		# recursively call heapify from the next index.
		heapify(input_array, next_index, array_size)
 

def build_heap(input_array):

	# given an array, rearrange the elements in the array to maintain heap property.

	# starting from first intermediate heap node to root, heapify each node.
	for index in range((len(input_array)//2)-1, -1, -1):
		heapify(input_array, index, len(input_array))


def heapsort(input_array):
	
	array_size = len(input_array)

	# handle empty and single-element arrays.
	if array_size <= 1:
		return
	
	# build heap
	build_heap(input_array)
	
	for last_index in range(array_size-1, 0, -1):
	
		# extract max (swap the first and last elements and decrease the size of heap)
		input_array[0], input_array[last_index] = input_array[last_index], input_array[0]

		# heapify from root to maintain the heap property.
		heapify(input_array, 0, last_index)


input_array = [6, 4, 8, 1, 9, 2, 3]

print(f'before heapsort {input_array}')

heapsort(input_array)

print(f'after heapsort {input_array}')
