'''

'''

# input = number
# print the pattern

# 0 -> dont print
# 1 -> 1
# 2 -> 1, 1,2, 1


def print_row(number):
    output_list = [str(element) for element in range(1, number+1)]
    print(", ".join(output_list))

def print_pattern(number):

    for num in range(1, number+1):
        print_row(num)

    for num in range(number-1, 0, -1):
        print_row(num)

number = 4
print_pattern(number)


    



        
