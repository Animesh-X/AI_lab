import tsplib95 as tsp
import random
import math
import copy


data = tsp.load("tsmdataset.tsp")    # Load the data from the file pr107.tsp
cities = list(data.get_nodes())     # Retrieve the cities information


def get_neighbors(state):
    
    state_copy = copy.deepcopy(state)
    size = len(state)
    pos1 = random.choice(range(size))
    pos2 = random.choice(range(size))
    state_copy[pos1], state_copy[pos2] = state_copy[pos2], state_copy[pos1]
    return state_copy


def get_cost(state):
    
    distance = 0
    
    for i in range(len(state)):
        from_city = state[i]
        to_city = None
        if i+1 < len(state):
            to_city = state[i+1]
        else:
            to_city = state[0]
        distance += data.get_weight(from_city, to_city)
    
    fitness = 1/float(distance)
    return fitness
        

def annealing(initial_state, temp, alpha):
    
    solution = initial_state
    curr_temp = temp
    curr_alpha = alpha
    
    same_solution = 0
    same_cost_diff = 0
    
    while same_solution < 15000 and same_cost_diff < 150000 and curr_temp > 0:
        neighbor = get_neighbors(solution)
        cost_diff = get_cost(neighbor) - get_cost(solution)
        
        if cost_diff > 0:
            solution = neighbor
            same_solution = 0
            same_cost_diff = 0
        else :
            if random.uniform(0, 1) <= math.exp(float(cost_diff) / float(curr_temp)):
                solution = neighbor
                same_solution = 0
                same_cost_diff = 0
            else:
                same_solution +=1
                same_cost_diff+=1
        curr_temp = curr_temp * curr_alpha
        
    return solution, 1/get_cost(solution)


def main():
    
    temperature  = int(input(f"Enter the temperature: "))
    alpha = float(input(f"Enter the cooling rate: "))
    no_of_iterations = int(input(f"Enter the number of iterations: "))
    
    best_routes = []
    best_route_distance = []
    for i in range(no_of_iterations):
        route, route_distance = annealing(cities, temperature, alpha)
        best_routes.append(route)
        best_route_distance.append(route_distance)
        
    for i in range(len(best_routes)):
        print(best_routes[i], "\t", best_route_distance[i])

main()