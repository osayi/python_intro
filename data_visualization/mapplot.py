import matplotlib.pyplot as plt



x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values,y_values,c=y_values, cmap = plt.cm.Purples, s=25)

#set chart title and Label axes

plt.title("View of Cubic Numbers", fontsize =24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Cubic Value", fontsize = 14)

plt.show()

