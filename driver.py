from helpers import *
from uninformed import *
from informed import *
from local import *

'''
    Perform Breadth First Search
'''
#read grid
grid = readGrid("grid.txt")
#Set the starting positon and goal position 
start_pos = [0, 0]
goal_pos = [len(grid)-1, len(grid[0])-1]
#Set up the  initial closed and open lists 
open_list = []
closed_list = []
#setup uninformed breadth search search
start_node = Node(value=start_pos)
goal_node = Node(value=goal_pos)

print("Perform Breadth First Search")

if (start_node.value != goal_node.value):
    closed_list.append(start_node)
    breadth_path = uninformed_search(open_list, closed_list, start_node, goal_node, grid, True)
#visualizeGrid(grid, breadth_path, True)
outputGrid(grid, start_pos, goal_pos, breadth_path, 'breadth_output.txt')

'''
    Perform Depth First Search
'''
#read grid
grid = readGrid("grid.txt")
#Set the starting positon and goal position 
start_pos = [0, 0]
goal_pos = [len(grid)-1, len(grid[0])-1]
#Set up the  initial closed and open lists 
open_list = []
closed_list = []
#setup uninformed depth search
start_node = Node(value=start_pos)
goal_node = Node(value=goal_pos)

print("Perform Depth First Search")

if (start_node.value != goal_node.value):
    closed_list.append(start_node)
    depth_path = uninformed_search(open_list, closed_list, start_node, goal_node, grid, False)
#visualizeGrid(grid, depth_path, True)
outputGrid(grid, start_pos, goal_pos, depth_path, 'depth_output.txt')

'''
    Perform A* Search
'''
#read grid
grid = readGrid("grid.txt")
#Set the starting positon and goal position 
start_pos = [0, 0]
goal_pos = [len(grid)-1, len(grid[0])-1]
#Set up the  initial closed and open lists 
open_list = []
closed_list = []
#setup informed search
heur = heuristic(start_pos, goal_pos)
start_node = InformedNode(start_pos, g=grid[start_pos[0]][start_pos[1]], h=heur)
goal_node = InformedNode(value=goal_pos)

print("Perform A* First Search")

if (start_node.value != goal_node.value):
    closed_list.append(start_node)
    path = a_star(open_list, closed_list, start_node, goal_node, grid)
outputGrid(grid, start_pos, goal_pos, path, 'a_star_output.txt')
#visualizeGrid(grid, path, True)

'''
    Perform Simulated Annealing (Local Search)
'''
print("Perform Simulated Annealing")
board_sizes = [4, 8, 16]
decay_rates = [.9, .75, .5]
thresholds = [0.000001, 0.0000001, 0.00000001]

#trying different pairs 
for i in range(0, 3):
    print("***************************")
    print(f"Board size: {board_sizes[1]}")
    print("***************************")
    print(f"Decay rate: {decay_rates[i]}")
    print("***************************")
    print(f"Threshold: {thresholds[i]}")
    print("***************************")
    board = Board(board_sizes[1])
    board.rand()
    result = simulated_annealing(board, decay_rates[i], thresholds[i]) 

#10 runs of each board size
for j in board_sizes:
    board = Board(j)
    board.rand()
    print("***************************")
    print(f"Board size: {j}")
    print("***************************")
    print(f"Decay rate: {decay_rates[0]}")
    print("***************************")
    print(f"Threshold: {thresholds[0]}")
    for k in range(0, 10):  
        print("---------------------------")
        print(f"Run: {k+1}")
        print()
        result = simulated_annealing(board, decay_rates[0], thresholds[0])