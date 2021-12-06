import matplotlib.pyplot as plt

def plot_cvrp_solution(cvrp, cvrp_solution, show_numbers=True):
	colors = ['blue', 'red', 'darkorange', 'green', 'darkviolet', 'gray', 'maroon', 'cyan', 'darkgreen', 'deeppink', 'lime']

	index = 0
	for route in cvrp_solution.routes:
		color = colors[index]

		#x,y = cvrp.coordinates[1] #depot
		c0 = route[0]

		xplot = (cvrp.coordinates[1][0], cvrp.coordinates[c0][0])
		yplot = (cvrp.coordinates[1][1], cvrp.coordinates[c0][1])
		plt.plot(xplot, yplot, color=color, marker="o", markersize=4);

		for i in range(len(route) -1):
			ci = route[i] 
			x1,y1 = cvrp.coordinates[ci]

			cj = route[i+1]
			x2,y2 = cvrp.coordinates[cj]

			xplot = (x1, x2)
			yplot = (y1, y2)
			plt.plot(xplot, yplot, color=color, marker="o", markersize=4);


		cn = route[-1]

		xplot = (cvrp.coordinates[cn][0], cvrp.coordinates[1][0])
		yplot = (cvrp.coordinates[cn][1], cvrp.coordinates[1][1])
		plt.plot(xplot, yplot, color=color, marker="o", markersize=4);

		index = (index+1)%len(colors)

	#Depot
	plt.plot(*cvrp.coordinates[1], color='darkcyan', marker="s", markersize=10);

	#Clients ID
	if show_numbers:
		for i in range(1, cvrp.number_of_clients +1): #0 does not exist on cvrp
			x,y = cvrp.coordinates[i]
			plt.text(x,y , str(i), color='black', fontsize=12);


	plt.show()