
def read_binary_watch(turned_on):

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
    for x in range(5):
        y = turned_on-x
        if y >= 0:
            # get subsets of size x --> sum elements in the set.
            # get subsets of size y --> sum elements in the set.
            # possible combinations = {sum_x:sum_y in the format "0:00" if sum_x < 10 or "00:00" format if sum_x >= 10}
    # return the possible combinations
            

