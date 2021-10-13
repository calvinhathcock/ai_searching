# Calvin Hathcock
# ITCS 3153 

''' 
Informed search 
Implemented by the A* algorithm
'''

import typing as T
import heapq
from helpers import *
from uninformed import Node

class InformedNode(Node):
    '''
    Informed Node object to represent each position in the grid
    value: location in grid
    g: step cost of value
    h: heuristic of value
    parent: parent node
    '''
    def __init__(self, value: T.Tuple[int, int], g: float = 0.0, h: float = 0.0, parent = None):
        super().__init__(value, parent) 
        self.g = g
        self.h = h
        self.f = g + h
        
    def __str__(self) -> str:
        row, col = self.value
        return f"Node(({row}, {col}), g(n): {self.g}, h(n): {self.h}, f(n): {self.f})"
    
    def __repr__(self) -> str:
        return str(self)
    
    # override '<' operator so adding to heap can order them by f(n)
    def __lt__(self, other):
        return self.f < other.f

# compute "Manhattan Distance" as heuristic
def heuristic(value: T.Tuple[int, int], goal_value: T.Tuple[int, int]):
    return abs(goal_value[0] - value[0]) + abs(goal_value[1] - value[1])

def expand_informed_node(node: InformedNode, grid: T.List, closed_list: T.Set, open_list: T.List[Node], goal: InformedNode):
    '''Given the current node, expand all of its neighbors based on the current queue
    
    Parameters:
        Node: current node
        grid: current grid
        closed_list: list of nodes already visited
        open_list: list of accessible nodes that are yet to be visited
        goal: the goal location
    
    Return:
        Void
    '''
    neighbors = get_neighbors(node.value, grid)
    for n in neighbors:
        # skip over nodes in the closed list
        if any(n == x.value for x in closed_list):
            continue
        # skip over nodes in the open list
        if any(n == x.value for x in open_list):
            continue
        heur = heuristic(n, goal.value)
        heapq.heappush(open_list, InformedNode(value = n, g = grid[n[0]][n[1]], h = heur, parent = node))

def a_star(open_list: T.List, closed_list: T.List, node: Node, goal: Node, grid: T.List):
    ''' Performs an *informed* search, A* algorithm 

        Parameters: 
            open_list: Nodes yet to be visited
            closed_list: Nodes already visited
            node: Starting node
            goal: goal node
            grid: Grid in which the search will be conducted
        
        Returns:
            A "path" aka 2d list aka locations in the grid
    '''
    count = 1
    heapq.heappush(open_list, node)
    while True:
        #failure when there is no more nodes in the open list
        if not open_list:
            status = "failure"
            break
        #heap always returns the lowest cost (f(n))
        node = heapq.heappop(open_list)  
        if node.value == goal.value:
            status = "success"
            break
        closed_list.append(node)
        expand_informed_node(node, grid, closed_list, open_list, goal)
        count += 1
    path = []
    cost = 0
    #traverse nodes nodes to get the path and its cost
    while node is not None:
        cost = cost + grid[node.value[0]][node.value[1]]
        path.insert(0, node.value)
        node = node.parent
    print(status)
    print(f"Total expanded nodes: {count}")
    print(f"Path cost: {cost}")
    return path