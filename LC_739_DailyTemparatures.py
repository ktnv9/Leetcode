def DailyTemparatures(temparatures):

    # monotonic stack approach | rc -> O(n) | sc -> O(n)

    stack = []    
    wd_temps = []
    for curr_indx in range(len(temparatures)-1, -1, -1):

        curr_temp = temparatures[curr_indx]
        wd_count = 0
        w_temp_found = False
        while stack:
            
            if curr_temp > stack[-1][0]:
                wd_count += stack.pop()[1]
            else:
                w_temp_found = True
                wd_count += 1
                break 
            # wd_count += popped_element[1]
        if not w_temp_found:
            wd_count = 0
        stack.append((curr_temp, wd_count))
        wd_temps.append(wd_count)

    return wd_temps[::-1]

    

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
warmer_temparatures = DailyTemparatures(temparatures)
print(warmer_temparatures)

temparatures = [30,40,50,60]
warmer_temparatures = DailyTemparatures(temparatures)
print(warmer_temparatures)

temparatures = [30, 60, 90]
warmer_temparatures = DailyTemparatures(temparatures)
print(warmer_temparatures)