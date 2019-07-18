import matplotlib.pyplot as plt 

from mole_motion import RandomWalk

#Generate random walk and capture points

rw = RandomWalk()
rw.fill_walk()

#plt.plot(rw.x_values, rw.y_values, color='g',linewidth=1.0)

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
			cmap=plt.cm.Reds, edgecolor='none', s=10)

plt.scatter(0,0, c='green',edgecolors='none', s=60)
plt.scatter(rw.x_values[-1],rw.y_values[-1], c='blue', 
			edgecolor='none', s=60)


plt.show()