def canVisitAllRooms(rooms) -> bool:
    
    # mark the first room visited.
    visited = {0}

    # stack to traverse the graph of rooms.
    stack = [0]

    while stack:

        # recently visited room.
        room = stack[-1]
        
        # get keys and search for the unvisited room.
        unv_room_found = False
        for key in rooms[room]:
            if key not in visited:

                # if unvisited room is found, mark it visited.
                stack.append(key)
                visited.add(key)
                unv_room_found = True
                break

        # if all keys from recent room are all visited, proceed with the next recent room.
        if not unv_room_found:
            stack.pop()
    
    # check if all rooms are visited.
    return len(visited) == len(rooms)