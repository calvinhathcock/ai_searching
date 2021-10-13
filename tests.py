from helpers import *
from uninformed import *
from informed import *

def runTests(displayGrids=False):
    """ Runs a series of planning queries on randomly generated maps, map sizes, and start and goal pairs
        
        Parameters:
                displayGrid (bool): True will use matplotlib to visualize the grids
                
        Returns:
                None
    """
    numExpanded = []
    totalGridSize = 200
    gridSizes = [i for i in range(10,totalGridSize,5)]
    
    numTests = 500
 
    # For each grid size
    for gs in gridSizes:    
        numEx = []
        # Do X tests where X=numTests
        for i in range(0,numTests):
    
            # Get random grid, start, and goal
            grid = genGrid(gs)
            start, goal = genStartGoal(grid)
            start_node = Node(start)
            goal_node = Node(goal)
    
            # Call algorithm
            open_list = []
            closed_list = []

            [p, numExp] = uninformed_search(open_list, closed_list, start_node, goal_node, grid, True)
    
            # Display grids if desired
            if i < 2 and gs <= 50 and displayGrids:
                visualizeGrid(grid, p)
                # Store data for single run
            numEx.append(numExp)
   
        # Store data for grid size
        numExpanded.append(numEx)
        
    print(numEx)
    # Get average of expanded nodes for each grid size
    neAvg = []
    for i,n in enumerate(numExpanded):
        print("Grid size: %s" % gridSizes[i])
        avg = 0
        for e in n:
            avg += e
        avg = avg / len(n)
        neAvg.append(avg)
        print("Average number of expanded nodes: %s" % avg)
    
    # Display bar graph for expanded node data      
    pyplot.clf()
    pyplot.bar(gridSizes, neAvg)
    pyplot.show()

runTests()