from collections import deque

def pour(jug1, jug2, jug1_capacity, jug2_capacity):
    space_left = jug2_capacity - jug2
    if jug1 <= space_left:
        jug2 += jug1
        jug1 = 0
    else:
        jug1 -= space_left
        jug2 = jug2_capacity
    return jug1, jug2

def bfs(jug1_capacity, jug2_capacity, target_amount):
    visited = set() 
    queue = deque([(0, 0)])  
    actions = []  
    
    while queue:
        jug1, jug2 = queue.popleft()
        
        if jug1 == target_amount or jug2 == target_amount:
            return actions
        

        next_states = set()
        

        next_states.add((jug1_capacity, jug2))
        
        
        next_states.add((jug1, jug2_capacity))
        
        
        next_states.add((0, jug2))
        
        
        next_states.add((jug1, 0))
        
        
        next_jug1, next_jug2 = pour(jug1, jug2, jug1_capacity, jug2_capacity)
        next_states.add((next_jug1, next_jug2))
        
        
        next_jug2, next_jug1 = pour(jug2, jug1, jug2_capacity, jug1_capacity)
        next_states.add((next_jug1, next_jug2))
        
        
        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
                actions.append(state)
    
    return None  


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
