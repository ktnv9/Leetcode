def daily_temperatures(temparatures):

    """
    Finds the number of days until a warmer temperature for each day.
    Uses monotonic decreasing stack to efficiently find the next greater element.

    Args:
        temperatures: A list of temperatures
    Returns:
        A list of the number of days until a warmer temperature for each day.
    """

    # Handling the edge case of empty input.
    if not temparatures:
        return []

    num_elements = len(temparatures)
    wait_days = [0] * num_elements
    stack = []  # stores (temperature, index) pairs  
    
    for curr_indx in range(num_elements-1, -1, -1):

        curr_temp = temparatures[curr_indx]
        
        days = 0

        while stack and curr_temp >= stack[-1][0]:
            
            popped_temp, popped_index = stack.pop()
            days += popped_index + 1
        
        if stack:
            wait_days[curr_indx] = stack[-1][1] - curr_indx

        stack.append((curr_temp, curr_indx))

    return wait_days

    '''
    # brute force approach | rc -> O(n^2) | sc -> O(n)

    warmer_temparatures = []
    
    num_elements = len(temparatures)
    
    for curr_indx in range(num_elements):
        
        warmer_day_found = False
        count = 0
        for next_indx in range(curr_indx+1, num_elements):
            if next_indx < num_elements:
                if temparatures[next_indx] > temparatures[curr_indx]:
                    count += 1
                    warmer_day_found = True
                    break
                else:
                    count += 1
        if warmer_day_found:
            warmer_temparatures.append(count)
        else:
            warmer_temparatures.append(0)
            
    return warmer_temparatures
    '''
temparatures = [73,74,75,71,69,72,76,73]
warmer_temparatures = daily_temperatures(temparatures)
print(warmer_temparatures)

temparatures = [30,40,50,60]
warmer_temparatures = daily_temperatures(temparatures)
print(warmer_temparatures)

temparatures = [30, 60, 90]
warmer_temparatures = daily_temperatures(temparatures)
print(warmer_temparatures)

temparatures = [30, 40, 50, 60]
warmer_temparatures = daily_temperatures(temparatures)
print(warmer_temparatures)

temparatures = [60, 50, 40, 30]
warmer_temparatures = daily_temperatures(temparatures)
print(warmer_temparatures)


temparatures = [30, 60, 90, 40, 20, 50, 80]
warmer_temparatures = daily_temperatures(temparatures)
print(warmer_temparatures)