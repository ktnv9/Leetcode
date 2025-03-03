def largest_almost_missing_integer_simulation(nums, k):

    if not nums:
        return -1
    
    nums_size = len(nums)

    if k > nums_size:
        return -1
    
    if k == nums_size:
        return max(nums)
    
    sub_array_counts = {}

    for sub_array_num in range(nums_size-k+1):
        
        for index in range(sub_array_num, sub_array_num+k):

            if nums[index] not in sub_array_counts:
                sub_array_counts[nums[index]] = [sub_array_num]
            else:
                if sub_array_num not in sub_array_counts[nums[index]]:
                    sub_array_counts[nums[index]].append(sub_array_num)

    max_element  = -1
    for element in sub_array_counts:
        
        if len(sub_array_counts[element]) == 1:
            
            if element > max_element:
                max_element = element

    return max_element
                
def largest_almost_missing_integer_optimized(nums, k):

    max_element = -1
    if nums and 0 < k <= len(nums):
        
        nums_count = len(nums)

        # one subsequence - maximum of all elements.
        if k == nums_count:
            return max(nums)

        # subsequence of size 1 - maximum of all unique elements.
        if k == 1:
            D = {}
            for num in nums:
                if num not in D:
                    D[num] = 1
                else:
                    D[num] += 1
            for num in nums:
                if D[num] == 1:
                    if num > max_element:
                        max_element = num
        
        # 1 < size of subsequence < n - Find the largest between first and last element.
        else:
            first, last = nums[0], nums[nums_count-1]

            first_unique, last_unique = True, True
            for index in range(1, nums_count):
                if nums[index] == first:
                    first_unique = False
            for index in range(0,nums_count-1):
                if nums[index] == last:
                    last_unique = False

            if first_unique:
                max_element = max(max_element, first)
            if last_unique:
                max_element = max(max_element, last)

    return max_element







nums = [3,9,2,1,7]
k = 3

nums = [3,9,7,2,1,7]
k = 4

nums = [0,0]
k = 2

nums = [2,2]
k = 1

nums = [7,5,9,10,0,12,3,12,10]
k = 1

am_element = largest_almost_missing_integer_optimized(nums, k)
print(am_element)            
