import numpy as np

import geometry

class CVRP_Solution:
    #routes    

    def __init__(self):
        self.routes = []
        self.cost = 0

    def print_solution(self):
        for index, route in enumerate(self.routes):
            print(f"Route #{index}:", route)

    def calculate_cost(self, cvrp):
        sum_route_distances = 0
        for route in self.routes:
            route_distance = 0
            ci = 1 #depot
            for j in range(len(route)):
                cj = route[j]
                route_distance += cvrp.distances[ci][cj]
                ci = cj

            sum_route_distances += cvrp.distances[route[-1]][1] #depot
            sum_route_distances += route_distance

        return sum_route_distances