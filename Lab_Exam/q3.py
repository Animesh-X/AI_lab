from collections import deque

def pour(jug1, jug2, jug1_capacity, jug2_capacity):
    # Pour water from jug1 to jug2
    space_left = jug2_capacity - jug2
    if jug1 <= space_left:
        jug2 += jug1
        jug1 = 0
    else:
        jug1 -= space_left
        jug2 = jug2_capacity
    return jug1, jug2

def bfs(jug1_capacity, jug2_capacity, target_amount):
    visited = set()  # To keep track of visited states
    queue = deque([(0, 0)])  # Initial state: both jugs empty
    actions = []  # To store the sequence of actions
    
    while queue:
        jug1, jug2 = queue.popleft()
        
        # Check if target_amount is achieved
        if jug1 == target_amount or jug2 == target_amount:
            return actions
        
        # Generate all possible next states
        next_states = set()
        
        # Fill jug1
        next_states.add((jug1_capacity, jug2))
        
        # Fill jug2
        next_states.add((jug1, jug2_capacity))
        
        # Empty jug1
        next_states.add((0, jug2))
        
        # Empty jug2
        next_states.add((jug1, 0))
        
        # Pour from jug1 to jug2
        next_jug1, next_jug2 = pour(jug1, jug2, jug1_capacity, jug2_capacity)
        next_states.add((next_jug1, next_jug2))
        
        # Pour from jug2 to jug1
        next_jug2, next_jug1 = pour(jug2, jug1, jug2_capacity, jug1_capacity)
        next_states.add((next_jug1, next_jug2))
        
        # Apply actions to the next states
        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
                actions.append(state)
    
    return None  # Target amount not reachable

# Example usage
jug1_capacity = 5
jug2_capacity = 3
target_amount = 4

sequence_of_actions = bfs(jug1_capacity, jug2_capacity, target_amount)
if sequence_of_actions:
    print("Sequence of actions to measure {} litres:".format(target_amount))
    for action in sequence_of_actions:
        print(action)
else:
    print("Target amount of water is not reachable.")
