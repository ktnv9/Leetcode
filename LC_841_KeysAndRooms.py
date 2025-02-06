def canVisitAllRooms(rooms) -> bool:
    
    # initially none of the rooms are visited.
    visited = {}
    for i in range(len(rooms)):
        visited[i] = False

    # mark the first room as visited.
    stack = [0]
    visited[0] =  True

    while not stack == []:

        # go to the recently visited room
        top = stack[-1]

        # get the keys.
        keys = rooms[top]

        # identify the unvisited room using the available keys.
        unvisited_room = -1
        for key in keys:
            if not visited[key]:
                unvisited_room = key
                break
                    
        # if an unvisited room exists, mark it as visited.
        if unvisited_room > 0:
            stack.append(unvisited_room)
            visited[unvisited_room] = True
        
        # if all rooms for which the keys are available are visited then continue with the next recently visited room.
        else:
            stack.pop()

    # check if all rooms are visited.
    for room in visited:
        if not visited[room]:
            return False
        
    return True