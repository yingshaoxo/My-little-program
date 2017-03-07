import matplotlib.pyplot as plt
import math


class formula():
    def point_distance(self, xy1, xy2):
        x1, y1 = xy1
        x2, y2 = xy2
        return int(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))

class geometry(formula):
    def __init__(self, x_center, y_center):
        self.x_center = x_center
        self.y_center = y_center
        #plt.figure(figsize=(7, 7))
        plt.axis([0, length*2, 0, length*2])

    def cube(self, side_length):
        x_from = self.x_center - side_length//2
        y_from = self.y_center - side_length//2
        point_x = []
        point_y = []
        for x in range(x_from, x_from+side_length+1):
            for y in range(y_from, y_from+side_length+1):
                point_x.append(x)
                point_y.append(y)
        return point_x, point_y

    def circular(self, radius):
        side_length = radius * 2 
        cube_x, cube_y = self.cube(side_length)
        point_x = []
        point_y = []
        for i in range(0, len(cube_x)):
            x, y = cube_x[i], cube_y[i]
            if int(self.point_distance([x, y], [self.x_center, self.y_center])) <= radius:
                point_x.append(x)
                point_y.append(y)
        return point_x, point_y

    def oval(self, a, b):
        c = math.sqrt(a**2 - b**2)

        circular_x, circular_y = self.circular(a)
        point_x = []
        point_y = []
        for i in range(0, len(circular_x)):
            x, y = circular_x[i], circular_y[i]
            if (((x-self.x_center)**2)/(a**2) + ((y-self.y_center)**2)/(b**2)) == 1:
                point_x.append(x)
                point_y.append(y)
        return point_x, point_y

    def hyperbola(self, a, b):
        c = math.sqrt(a**2 + b**2)

        circular_x, circular_y = self.circular(a)
        point_x = []
        point_y = []
        for i in range(0, len(circular_x)):
            x, y = circular_x[i], circular_y[i]
            if (((x-self.x_center)**2)/(a**2) - ((y-self.y_center)**2)/(b**2)) == 1:
                point_x.append(x)
                point_y.append(y)
        return point_x, point_y


length = 500
g = geometry(length, length)

x, y = g.hyperbola(150, 100)
plt.scatter(x,y)

plt.show()