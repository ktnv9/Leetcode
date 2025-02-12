def DailyTemparatures(temparatures):

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

temparatures = [73,74,75,71,69,72,76,73]
warmer_temparatures = DailyTemparatures(temparatures)
print(warmer_temparatures)