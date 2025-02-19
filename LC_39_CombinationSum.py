
def combination_sum(candidates, target):

    # list to store all the combinations that sum to target.
    combinations = []

    # recursive call to get all possible non-repetitive combinations.
    def get_combinations(combination, start_index, current_sum):

        # base case : store the combination if its sum is equal to target.
        if current_sum == target:
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
            get_combinations(combination, index, current_sum+candidates[index]) # sum is calculated here to avoid recalculation at every recursive call.
            combination.pop() # back track

    
    candidates.sort() # sort to terminate early in the recursion.

    # intially combination is empty list, start index is 0, sum is also 0.
    get_combinations([], 0, 0)

    return combinations



candidates = [2,3,5]
target = 8
candidates = [2]
target = 1
candidates = [2,3,6,7]
target = 7
candidates = [7,3,2]
target = 18

combinations = combination_sum(candidates, target)

print(combinations)









'''
def combination_sum(candidates, target):

    def similar_lists(list1, list2):

        if len(list1) == len(list2):
            dict_counter = {}
            for element in list1:
                if element in dict_counter:
                    dict_counter[element] += 1
                else:
                    dict_counter[element] = 1
            for element in list2:
                if element in dict_counter:
                    dict_counter[element] -= 1
                else:
                    return False
            for element in dict_counter:
                if dict_counter[element]:
                    return False
            return True
        return False


    def get_combinations(combination, sum_value):

        # base case: if combination sums to target, then collect the combination
        if sum_value == target:
            
            similar_list_found = False
            for existing_combo in combinations:
                if similar_lists(existing_combo, combination):
                    similar_list_found = True
                    break
            if not similar_list_found:
                combinations.append(combination[:])
            return
        
        if sum_value > target:
            return
        
        for candidate in candidates:
            combination.append(candidate)
            get_combinations(combination, sum_value+candidate)
            combination.pop() # backtrack

    combinations = []
    get_combinations([],0)
    return combinations
'''




