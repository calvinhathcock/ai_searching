import random
import math
from helpers import *

class Board():
 
    def __init__(self, numRowsCols):
        self.cells = [[0] * numRowsCols for i in range(numRowsCols)]
        self.numRows = numRowsCols
        self.numCols = numRowsCols

		# negative value for initial h...easy to check if it's been set or not
        self.h = -1

    # Print board
    def printBoard(self):
        for row in self.cells:
            print (row)

    # Randomize the board
    def rand(self):
        self.cells = [[0] * self.numRows for i in range(self.numRows)]
        for row in self.cells:
            i = random.randint(0, self.numCols-1)
            row[i] = 1

    # Swap two locations on the board
    def swapLocs(self, a, b):
        temp = self.cells[a[0]][a[1]]
        self.cells[a[0]][a[1]] = self.cells[b[0]][b[1]]
        self.cells[b[0]][b[1]] = temp

# Cost function for a board
def numAttackingQueens(board):

    # Collect locations of all queens
    locs = [] 
    for r in range( len(board.cells) ):
        for c in range( len(board.cells[r]) ):
            if board.cells[r][c] == 1:
                locs.append([r, c])
    #print 'Queen locations: %s' % locs

    result = 0

    # For each queen (use the location for ease)
    for q in locs:

        # Get the list of the other queen locations
        others = [x for x in locs if x != q]
        #print 'q: %s others: %s' % (q, others)
    
        count = 0
        # For each other queen
        for o in others:
            #print 'o: %s' % o
            diff = [o[0] - q[0], o[1] - q[1]]

            # Check if queens are attacking
            if o[0] == q[0] or o[1] == q[1] or abs(diff[0]) == abs(diff[1]):
                count = count + 1

        # Add the amount for this queen
        result = result + count

    return result

# Move any queen to another square in the same column
# successors all the same                                                                                    
def getSuccessorStates(board):
    result = []

    for i_row, row in enumerate(board.cells):
        # Get the column the queen is on in this row
        # [0] because list comprehension returns a list, even if only one element
        # This line will crash if the board has not been initialized with rand() or some other method
        i_queen = [i for i,x in enumerate(row) if x == 1][0]

        # For each column in the row
        for i_col in range(board.numCols):

            # If the queen is not there
            if row[i_col] != 1:
                # Make a copy of the board
                bTemp = Board(board.numRows)
                bTemp.cells[:] = [r[:] for r in board.cells]

                # Now swap queen to i_col from i_queen
                bTemp.swapLocs([i_row, i_col], [i_row, i_queen])
                #bTemp.printBoard()
                result.append(bTemp)

    return result
    
def schedule_function(T, decay_rate):
    return T * decay_rate
  
def simulated_annealing(initial_board, decay_rate, T_threshold):
    ''' Performs local search, simulated annealing algorithm
        
        Parameters:
            initial_board: initial randomized nqueens board
            decay_rate: rate at which the temperature decays (per iteration)
            T_threshold: Minimum threshold for the temperature T
            
        Returns:
            Final heuristic value
    '''
    T = 100
    current = initial_board
    cost = numAttackingQueens(current)
    print("Initial board:")
    current.printBoard()
    print(f"h-value: {cost}")
    while T > T_threshold and cost > 0:
        # call schedule function
        T = schedule_function(T, decay_rate)
		# get list of successor states and their costs
        successors = getSuccessorStates(current)
		# select next node
        successor = random.choice(successors)
        successor_cost = numAttackingQueens(successor)
		# maybe go to next
        delta_e = cost - successor_cost
        if delta_e > 0 or random.random() < math.exp(delta_e / T):
            # definitely choose better one
            # maybe choose a worse one
            current = successor
            cost = successor_cost 
    print()
    print("Final board:")
    current.printBoard()
    print(f"h-value: {cost}")
    return cost


