from grid_methods import *

'''
state = (grid, grid_size, cursor)
car_info = (car_id, car_index, car_length, car_orientation)
'''

def func_actions(state):
    """
    This function will go through the list of all cars in the current Map, with the goal of determining whether it's
    possible to move them 1 coordinate up/down (in case they're vertical) or 1 coordinate to the sides
    (in case they're horizontal). The move is only considered possible if these coordinates are currently free.

    Parameters:
        - State: (grid, grid_size, cursor) -> Current state of the map

    Returns:
        A list of all the possible actions. Each action is represented by a tuple containing the info of the car to be
        moved, and the key corresponding to the direction in which the move will be made (car_info, key).
    """
    grid = state[0]
    grid_size = state[1]
    actlist = []

    # Determining the cars present in the Map
    cars = set(grid)
    cars.remove('o')
    cars.discard('x')

    # Checking the possible actions for each car
    for car in cars:
        car_info = get_car_info(state, car)
        car_index = car_info[1]
        car_size = car_info[2]
        car_orientation = car_info[3]

        if car_orientation == 'H':
            if car_index % grid_size != 0 and grid[car_index - 1] == 'o':
                actlist.append((car_info, 'a'))
            if car_index % grid_size + car_size < grid_size and grid[car_index + car_size] == 'o':
                actlist.append((car_info, 'd'))
        else:
            if car_index >= grid_size and grid[car_index - grid_size] == 'o':
                actlist.append((car_info, 'w'))
            if car_index + car_size * grid_size < grid_size * grid_size and grid[car_index + car_size * grid_size] == 'o':
                actlist.append((car_info, 's'))

    return actlist


def func_result(state, action):
    """
    This function receives the current state of the Map, as well as an action to be applied to a car in the map, and
    returns the state of the Map after this action is performed.

    Parameters:
        - State: (grid, grid_size, cursor) -> Current state of the map
        - Action: (car_info, key) -> Car in which the action will be applied, as well as the key describing the direction
        of the movement.

    Returns:
        A string representing the new State of the map after the move.
    """
    grid = state[0]
    grid_size = state[1]
    car_info = action[0]
    movement = action[1]

    car_id = car_info[0]
    car_index = car_info[1]
    car_size = car_info[2]

    grid_after_move = list(grid)

    if movement == 'w':
        grid_after_move[car_index - grid_size] = car_id
        grid_after_move[car_index + car_size * grid_size - grid_size] = 'o'
    elif movement == 'a':
        grid_after_move[car_index - 1] = car_id
        grid_after_move[car_index + car_size - 1] = 'o'
    elif movement == 's':
        grid_after_move[car_index + car_size * grid_size] = car_id
        grid_after_move[car_index] = 'o'
    else:
        grid_after_move[car_index + car_size] = car_id
        grid_after_move[car_index] = 'o'

    car_x = car_index % grid_size
    car_y = car_index // state[1]
    
    return (''.join(grid_after_move), grid_size)
    

def func_cost(state, action, parent_state):
    """

    """



    pass


def func_heuristic(state, movement_vector, limit, depth):
    """

    """
    pass


def func_satisfies(state):
    """
    This function will verify if the current State of the map already satisfies the conditions to move on to the next
    level, that is, if the player car ('A') is at the right edge of the map.

    Parameters:
        - State: (grid, grid_size, cursor) -> Current state of the map

    Returns:
        True if the car is on the edge of the map, False if not.
    """
    grid_size = state[1]

    car_info = get_car_info(state, 'A')
    car_index = car_info[1]

    # Determining the X coordinate of the player car
    car_x = car_index % grid_size + 1

    return car_x == grid_size - 1
