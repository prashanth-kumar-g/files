# importing the required module 
import matplotlib.pyplot as plt
import random
x = []
y = []
while True:
    # x axis values
    a = random.randrange(20,40)
    b = random.randrange(30,50)
    x.append(a)
    # corresponding y axis values
    y.append(b)
    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    # giving a title to my graph
    plt.title('My first graph!')
    # function to show the plot
    plt.show()
    plt.close()
