import geometry
from vrp import CVRP, CVRP_Solution

def create_cvrp_by_instance(instance_filename, tsp95_standard=False):
    try:
        file = open(instance_filename)
        lines =  file.readlines()
        file.close()
    except IOError:
        print("[ERROR]: Could not open the {} file.".format(instance_filename))
        exit(1)

    number_of_vehicles, bks, number_of_clients, vehicle_capacity = (int(x) for x in lines[0].split())
    cvrp = CVRP(number_of_vehicles, bks, number_of_clients, vehicle_capacity)

    # Clients
    for i in range(1, number_of_clients+1):
        line = lines[i]
        splited_line = line.split()
        client_id, x, y  = int(splited_line[0]), float(splited_line[1]), float(splited_line[2])
        cvrp.coordinates[client_id] = x,y

    #Demands
    lines = lines[number_of_clients+1:] #+1 so index 0 is now "DEMAND_SECTION" string
    for i in range(1, number_of_clients+1):
        line = lines[i]
        client_id, demand = (int(x) for x in lines[i].split())
        cvrp.demands[client_id] = demand 

    cvrp.distances = geometry.distances.calculate_distance_matrix(cvrp.coordinates, tsp95_standard)
    return cvrp


def create_cvrp_solution_by_file(solution_filename, add_one=False):
    try:
        file = open(solution_filename)
        lines =  file.readlines()
        file.close()
    except IOError:
        print("[ERROR]: Could not open the {} file.".format(solution_filename))
        exit(1)

    solution = CVRP_Solution()

    i = 0
    while True:
        line = lines[i]
        if line[-1] == '\n' or line[-1] == ' ': line = line[:len(line)-1]

        splited_line = line.split()

        if splited_line[0] != 'Cost':
            route = []
            for ci in splited_line[2:]:
                if add_one: ci = int(ci) +1
                route.append(int(ci))
            solution.routes.append(route)

        else:
            solution.cost = int(splited_line[1])
            break

        i+=1

    return solution