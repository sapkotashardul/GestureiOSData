from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
# import json
import ast

with open("Sensor_Data_for_Bite_using_Accelerometer/bite-9.txt") as f:
    x = []
    y = []
    z = []
    for line in f:
        x.append(ast.literal_eval(line)[1][0])
        y.append(ast.literal_eval(line)[1][1])
        z.append(ast.literal_eval(line)[1][2])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #ax.plot_surface(x, y, z)
    ax.plot3D(x, y, z, 'gray')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    ax.scatter3D(x, y, z, c=z, cmap='Greens');

    # plt.plot(x,y)
    plt.show()



