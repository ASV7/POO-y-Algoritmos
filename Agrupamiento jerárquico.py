import random
import sys
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def create_points(number_of_points):
    points = []

    for _ in range(number_of_points):
        new_point = Point(random.randint(0,21), random.randint(0,21))
        points.append(new_point)

    return points


def distance(point1, point2, metric_distance = 1):

    if  metric_distance == 1:
        return (((point1.x - point2.x) ** 2) + ((point1.y - point2.y) ** 2)) ** 0.5
    elif metric_distance == 2:
        return abs(point1.x - point2.x) + abs(point1.y - point2.y)
    else:
        print('Introduce a metric')


def closer(point1, points):
    
    distances = []

    for point2 in points:

        if (point2.x == point1.x) and (point2.y == point1.y):

            continue

        else:

            distances.append(distance(point1, point2))

        if len(distances) == 1:
                closer_point = point2
                


        if len(distances) >= 2:

            if distances[-1] == min(distances):
                
                closer_point = point2

    return closer_point


def Hierarchical_clustering(points):
    point = points[0]
    x_points = [point.x for point in points]
    y_points = [point.y for point in points]
    plt.scatter(x_points, y_points, c = ['black'], s = size_choice(sizes), alpha = 0.05)


    if len(points) > 1:
        closer_point_to_original = closer(point, points)
        closer_point_to_closer = closer(closer_point_to_original, points)

        if point == closer_point_to_closer:
            new_point = Point((point.x + closer_point_to_original.x) / 2, (point.y + closer_point_to_original.y) / 2)
            points.remove(point)
            points.remove(closer_point_to_original)
            points.insert(0, new_point)
            plt.text(new_point.x, new_point.y,set_cluster(clusters), fontsize = 10, fontweight = 'bold')
            set_area = plt.Circle((new_point.x, new_point.y), distance(point, closer_point_to_original)/2, alpha = 0.15, color = color_choice(colors))

            
            ax = plt.gca()
            ax.set_aspect(1)
            ax.add_artist(set_area)

            
            
            points = Hierarchical_clustering(points)
        else:
            points.remove(closer_point_to_original)
            points.insert(0, closer_point_to_original)

            points = Hierarchical_clustering(points)
    
    return points

def color_choice(colors):
    
    color_selec = random.choice(colors)
    colors.remove(color_selec)
    
    return color_selec

def size_choice(sizes):
    size_selec = sizes[0]
    sizes.remove(size_selec)
    
    return size_selec

def set_cluster(clusters):
    cluster = clusters[0]
    clusters.remove(cluster)
    
    return cluster

if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    figg=plt.figure(figsize=(10,10), dpi = 72)
    number_of_points = int(input('Introduce the number of points to cluster: '))
    colors = ['brown', 'red', 'tomato', 'sienna', 'orange', 'gold', 'yellow', 'lime', 'green', 'blue', 'turquoise', 'aqua', 'fuchsia', 'deeppink', 'blueviolet']
    sizes = [i*12 + 10 for i in range(30)]
    clusters = ['Cluster ' + str(i) for i in range(1,number_of_points)]
    points = create_points(number_of_points)
    original_points = points[:]
    x_points = [point.x for point in original_points]
    y_points = [point.y for point in original_points]
    for point in points:
        print('(' + str(point.x) + ',' + str(point.y) + ')')

    plt.scatter(x_points, y_points, c = ['black'],s=15)
    Hierarchical_clustering(points)
    plt.grid(True)


    plt.plot(x_points, y_points, 'kx',markersize=15)
    plt.show()