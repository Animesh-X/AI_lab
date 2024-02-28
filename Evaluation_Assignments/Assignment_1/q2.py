from collections import deque

class PuzzleNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent


def next_move(node):
    state = node.get_state()
    orow = 0
    ocol = 0
    for i, row in enumerate(state):
        for j, tile in enumerate(row):
            if tile == 0:
                orow = i
                ocol = j
    neighbors = []
    mover = [0, -1, 0, 1]
    movec = [-1, 0, 1, 0]
    for i in range(4):
        nrow = orow + mover[i]
        ncol = ocol + movec[i]
        if 0 <= nrow < len(state) and 0 <= ncol < len(state[0]):
            new_state = [list(row) for row in state]
            temp = new_state[nrow][ncol]
            new_state[nrow][ncol] = new_state[orow][ocol]
            new_state[orow][ocol] = temp
            neighbors.append(new_state)
    possible_moves = []
    for neighbor in neighbors:
        possible_moves.append(PuzzleNode(neighbor, node))
    return possible_moves


def bfs(initial_state, goal_state):
    queue = deque([PuzzleNode(initial_state)])
    visited = set()

    while queue:
        current_node = queue.popleft()
        current_state = tuple(map(tuple, current_node.get_state())) 
        if current_state == tuple(map(tuple, goal_state)):
            print("Solution found!")
            solution_node = current_node
            moves = []
            while solution_node:
                moves.insert(0, solution_node.get_state())
                solution_node = solution_node.get_parent()
            for i, state in enumerate(moves):
                print("Move #{}:".format(i))
                for row in state:
                    print(row)
                print()
            return current_node

        if current_state not in visited:
            visited.add(current_state)
            moves = next_move(current_node)
            for move in moves:
                queue.append(move)
                
    print("No solution found.")
    return None

initial_state = [
    [3, 8, 1],
    [6, 2, 5],
    [4, 7, 0]
]

goal_state = [
    [1,2,3],
    [8,4,0],
    [7,6,5]
]

bfs(initial_state, goal_state)