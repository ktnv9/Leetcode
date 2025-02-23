def combination_sum(candidates, target):

    # list to store all the combinations that sum to target.
    combinations = []

    # recursive call to get all possible non-repetitive combinations.
    def get_combinations(combination, current_sum, start_index):

        # base case : store the combination if its sum is equal to target.
        if current_sum == target:
            combinations.append(combination[:])
            return
        
        # no need to proceed further in the recursion tree if the sum crosses the target.
        if current_sum > target:
            return
        
        # Append each candidate to the combination and recursively check if the sum is equal to target.
        for index in range(start_index, len(candidates)):

            # early termination since the candiates are sorted.
            if current_sum + candidates[index] > target: 
                    break
            
            # eliminate duplicates by checking the current candinate is not equal to the previous element at the same recursion level.
            # and only first occurrence is allowed to be collected into the active combin
            if not ((candidates[index] == candidates[index-1]) and ((index - start_index) > 0)):
                combination.append(candidates[index])
                get_combinations(combination, current_sum+candidates[index], index+1) # sum is calculated here to avoid recalculation at every recursive call.
                combination.pop() # back track

    
    candidates.sort() # sort to terminate early in the recursion & to assist in avoiding duplicate combinations.
    # intially combination is empty list, start index is 0, sum is also 0.
    get_combinations([], 0, 0)

    return combinations

candidates = [2,5,2,1,2]
target = 5
candidates = [10,1,2,7,6,1,5]
target = 8
candidates = [3,1,3,5,1,1]
target = 8
combinations = combination_sum(candidates, target)
print(combinations)