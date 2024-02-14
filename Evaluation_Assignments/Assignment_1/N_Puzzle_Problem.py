import copy
class Node():
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        

class QueueFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

print(f"Enter the Initial State(3x3) (-1 for blank space): ")

initial_state = []
for i in range(3):
    initial_state.append(list(map(lambda x: int(x) ,input().split())))



print(f"Enter the Goal State(3x3) (-1 for blank space): ")

goal_state = []
for i in range(3):
    goal_state.append(list(map(lambda x: int(x) ,input().split())))


def result_after_move(current, position, next_move):
    x,y = position
    i,j = next_move
    current_copy = copy.deepcopy(current)
    if i<0 or i>2 or j<0 or j>2 :
        return None
    else:
        temp = current_copy[x][y]
        current_copy[x][y] = current_copy[i][j]
        current_copy[i] [j]=temp
        return current_copy

def possible_moves(current_state):
    curr_X = 0
    curr_Y = 0
    possible_states = []
    for i in range(3):
        for j in range(3):
            if current_state[i][j] == -1:
                curr_X = i
                curr_Y = j
                break
    delta_row = [0, -1, 0, 1]
    delta_col = [-1, 0, 1, 0]
    for i in range(4):
        possible_X = curr_X + delta_row[i]
        possible_Y = curr_Y + delta_col[i]
        result = result_after_move(current_state, (curr_X, curr_Y), (possible_X, possible_Y))
        if result is not None:
            possible_states.append(result)
    return possible_states    
                

def solve(start_state, end_state):
    start = Node(state=start_state, parent=None)
    
    frontier = QueueFrontier()
    frontier.add(start)
    
    explored = set()
    
    while True:
        if frontier.empty():
            return None
        
        node = frontier.remove()
        
        if node.state == end_state:
            solution = []
            while node.parent is not None:
                solution.append(node.state)
                node = node.parent
            solution.reverse()
            return solution
        
        explored.add(tuple(map(tuple, node.state)))
        
        for state in possible_moves(node.state):
            state_tuple = tuple(map(tuple, state))
            if not frontier.contains_state(state) and state_tuple not in explored:
                child = Node(state=state, parent=node)
                frontier.add(child)


solutions = solve(initial_state, goal_state)
if solutions is None:
    print("No solution exists for this start state: \n", initial_state, "\nand end state: \n", goal_state, "\n")
else:
    print("Starting State: \n")
    for k in initial_state:
        print(k)
    print()
    for i in solutions:
        for j in i:
            print(j)
        print()
    print("Goal State Reached!!!!\n")