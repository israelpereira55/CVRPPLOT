import numpy as np

import geometry

class CVRP:
    #coordinates   [x,y]   
    #distances      dij     distance matrix
    #demands       [?] 

    number_of_vehicles : int
    number_of_clients : int
    vehicle_capacity : int
    bks : int

    def __init__(self, number_of_vehicles, bks, number_of_clients, vehicle_capacity):
        self.number_of_vehicles = number_of_vehicles
        self.bks = bks
        self.number_of_clients = number_of_clients
        self.vehicle_capacity = vehicle_capacity

        self.coordinates = np.zeros((self.number_of_clients +1 ,2))
        self.demands = np.zeros((self.number_of_clients +1))


    def print_instance(self, debug=False):
        print("=================================== CVRP INSTANCE ========================================")
        print(f"\n  BKS: {self.bks}"
              f"\n  Number of clients: {self.number_of_clients}"
              f"\n  Number of vehicles: {self.number_of_vehicles}"
              f"\n  Vehicle capacity: {self.vehicle_capacity}")

        print("\n\nClients\n")
        print("ID\tX\tY\tDEMAND")
        for i in range(self.number_of_clients +1):
            client_id, x, y, demand = i, *self.coordinates[i], self.demands[i]
            print("{}\t{}\t{}\t{}".format(client_id, x, y, demand))
        
        print("==========================================================================================")


        if debug:
            print("\n  DISTANCE MATRIX ({}x{})". format(len(self.distances), len(self.distances[0])) )
            for i in range(self.number_of_clients):
                print(self.distances[i])
