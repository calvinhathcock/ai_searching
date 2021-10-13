from helpers import *
from uninformed import *
from informed import *

open_list = []
closed_list = []

#read in grid 
grid = readGrid("grid.txt")

#get starting location
start = input("Enter coordinates of starting position, separated by spaces: ")
start = start.split()
for i in range(len(start)):
    start[i] = int(start[i])

#get goal location
goal = input("Enter coordinates of the goal position, separated by spaces: ")
goal = goal.split()
for i in range(len(goal)):
    goal[i] = int(goal[i])

heur = heuristic(start, goal)
#create starting node
start_node = InformedNode(value=start, g=grid[start[0]][start[1]], h = heur)
#start_node = Node(start)
#create goal node
goal_node = InformedNode(value=goal)
#goal_node = Node(goal)

if (start_node.value != goal_node.value):
    closed_list.append(start_node)
    path = a_star(open_list, closed_list, start_node, goal_node, grid)
#outputGrid(grid, start, goal, path)
#visualizeGrid(grid, path, True)
# if (start_node.value != goal_node.value):
    # closed_list.append(start_node)
    # path = uninformed_search(open_list, closed_list, start_node, goal_node, grid, True)
# visualizeGrid(grid, path, True)
# #todo:
#   structure driver better



'''A* driver'''
# #read grid
# grid = readGrid("grid.txt")
# #Set the starting positon and goal position 
# start_pos = [0, 0]
# goal_pos = [len(grid)-1, len(grid[0])-1]
# #Set up the  initial closed and open lists 
# open_list = []
# closed_list = []
# #setup informed search
# heur = heuristic(start_pos, goal_pos)
# start_node = InformedNode(start_pos, g=grid[start_pos[0]][start_pos[1]], h=heur)
# goal_node = InformedNode(value=goal_pos)

# if (start_node.value != goal_node.value):
#     closed_list.append(start_node)
#     path = a_star(open_list, closed_list, start_node, goal_node, grid)
# #outputGrid(grid, start, goal, path)
# #visualizeGrid(grid, path, True)
