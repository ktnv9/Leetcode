def combination_sum(candidates, target):

    # list to store all the combinations that sum to target.
    combinations = []

    # recursive call to get all possible non-repetitive combinations.
    def get_combinations(combination, start_index, current_sum):

        # base case : store the combination if its sum is equal to target.
        if current_sum == target:
            if combination not in combinations:
                combinations.append(combination[:])
            return
        
        # no need to proceed further in the recursion tree if the sum crosses the target.
        if current_sum > target:
            return
        
        # Append each candidate to the combination and recursively check if the sum is equal to target.
        for index in range(start_index, len(candidates)):

            if current_sum + candidates[index] > target: # early termination since the candiates are sorted.
                break

            combination.append(candidates[index])
            get_combinations(combination, index+1, current_sum+candidates[index]) # sum is calculated here to avoid recalculation at every recursive call.
            combination.pop() # back track

    
    candidates.sort() # sort to terminate early in the recursion.

    # intially combination is empty list, start index is 0, sum is also 0.
    get_combinations([], 0, 0)

    return combinations


candidates = [10,1,2,7,6,1,5]
target = 8
candidates = [2,5,2,1,2]
target = 5
combinations = combination_sum(candidates, target)
print(combinations)