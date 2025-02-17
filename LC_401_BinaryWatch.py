
def read_binary_watch(turned_on):

    # back tracking approach to get the subsets of given size.
    def get_subsets(input_list, size):

        subsets = []

        def get_subset(subset, start):

            # base case: when subset is of desired size, collect the subset.
            if len(subset) == size:
                subsets.append(subset[:])
                return
            
            # append each element in the set to the subset obtained so far and recursively call the method.
            for i in range(start, len(input_list)):
                subset.append(input_list[i])
                get_subset(subset, i+1)
                subset.pop() # backtrack
        
        # get the subsets using backtracking methodology.
        get_subset([], 0)

        return subsets

    time_combinations = []
    hours_set = [8,4,2,1]
    minutes_set = [32,16,8,4,2,1]
    for hour_leds_on in range(5):
        minute_leds_on = turned_on - hour_leds_on
        if minute_leds_on >= 0:
            
            subsets_x = get_subsets(hours_set, hour_leds_on)
            subsets_y = get_subsets(minutes_set, minute_leds_on)

            for subset_x in subsets_x:
                for subset_y in subsets_y:
                    hours = sum(subset_x)
                    minutes = sum(subset_y)
                    if hours <= 11 and minutes <= 59:
                        time = f"{hours}:{minutes:02d}"
                        time_combinations.append(time)
    
    return time_combinations

turned_on = 2
time_combinations = read_binary_watch(turned_on)
print(time_combinations)

    # 4 leds on top (8, 4, 2, 1)
    # 6 leds at bottom (32, 16, 8, 4, 2, 1)

    # turned on --> how many leds are turned on in total.

        # eg:   0 --> 0 h-leds, 0 m-leds
        #       1 --> 1 h-leds, 0 m-leds or 0 h-leds 1 m-leds

        # turned on can be only between 0 to 10.
    
    # turned on --> n --> x + y (x = #.of leds from h, y = #.of leds from m)
    #       0 <= x <= 4, 0 <= y <= 6

    # {8, 4, 2, 1} --> given x --> # .of subsets of length x.
    # {32, 16, 8, 4, 2, 1} --> given y --> #. of subsets of length y.

    # time --> sum of elements in h set : sum of elements in m set.
        # sum of elements in h set [0, 11]
        # sum of elements in m set [0, 59]

    # eg: n = 5 --> (0+5, 1+4, 2+3, 3+2, 4+1) similar is the case with other numbers 
    #     n = 3 --> (0+3, 1+2, 2+1, 3+0)
    # for x in range(5):
    #     y = turned_on-x
    #    if y >= 0:
            # get subsets of size x using backtracking --> sum the subsets.
            # get subsets of size y using backtracking --> sum the subsets.
            # possible combinations = {"sum_x:sum_y" in the format "0:00" if sum_x < 10 or "00:00" format if sum_x >= 10}
    # return the possible combinations

