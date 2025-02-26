
def province_count(is_connected):

    num_cities = len(is_connected)
    remaining_cities = set([i for i in range(num_cities)])
    province_count = 0

    while not len(remaining_cities) == 0:

        start_city = remaining_cities.pop()
        province_count += 1
        stack = [start_city]
        
        while stack:

            top = stack[-1]

            unvisited_nbr_exists = False
            for neighbour_city, connection_chk in enumerate(is_connected[top]):
                if not neighbour_city == top and connection_chk and neighbour_city in remaining_cities:
                    stack.append(neighbour_city)
                    remaining_cities.remove(neighbour_city)
                    unvisited_nbr_exists = True
                    break
            if not unvisited_nbr_exists:
                stack.pop()
    return province_count

is_connected = [[1,1,0],[1,1,0],[0,0,1]]
is_connected = [[1,0,0],[0,1,0],[0,0,1]]
count = province_count(is_connected)
print(count)




