# Calvin Hathcock
# ITCS 3146 

''' 
Uniformed search 
Implemented by Breadth First Search (BFS) and Depth First Search (DFS) algorithms
'''
import typing as T
from helpers import *

#Node object to represent each position in the grid 
class Node: 
    ''' 
    Node object to represent each position in the grid
    value: 2 element list for the coordinate
    parent: reference variable to another Node object
    '''
  
    def __init__(self, value: T.Tuple[int, int], parent = None):
        self.value = value
        self.parent = parent

    def __str__(self) -> str:
        row, col = self.value
        return f"Node({row}, {col})"

    def __repr__(self) -> str:
        return str(self)

def expand_node(node: Node, grid: T.List, closed_list: T.Set, open_list: T.List[Node]):
    '''Given the current node, expand all of its neighbors based on the current queue
    
    Parameters:
        Node: current node
        grid: current grid
        closed_list: list of nodes already visited
        open_list: list of accessible nodes that are yet to be visited
    
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
        open_list.append(Node(value = n, parent = node))

def uninformed_search(open_list: T.List, closed_list: T.List, node: Node, goal: Node, grid: T.List, orientation: bool):
    ''' Performs an *uninformed* search, either breadth first or depth first

        Parameters: 
            open_list: Nodes yet to be visited
            closed_list: Nodes already visited
            node: Starting node
            goal: goal node
            grid: Grid in which the search will be conducted
            orientation: flag for orientation of the search
                            true: breadth (FIFO)
                            false: depth  (LIFO)
        
        Returns:
            A "path" or 2d list or locations in the grid
    '''
    count = 1
    expand_node(node, grid, closed_list, open_list)
    while True:
        #failure when there is no more nodes in the open list
        if not open_list:
            status = "failure"
            break
        #get next node based on orientation of search
        #orientation true: use breadth first
        #orientation false: use depth first
        if orientation:
            node = open_list.pop(len(open_list)-1) 
        else:
            node = open_list.pop(0) 
        #success when goal node is found
        if node.value == goal.value:
            status = "success"
            break
        closed_list.append(node)
        expand_node(node, grid, closed_list, open_list)
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