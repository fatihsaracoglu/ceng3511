import math, itertools
from collections import defaultdict
from random import uniform
import matplotlib.pyplot as plt

colors = ['green', 'red', 'blue', 'orange', 'brown', 'olive', 'gray', 'purple', 'cyan', 'pink']

dataset = []
with open('data.txt', 'r') as data:
    lines = data.read().splitlines()
    for line in lines[1:]:
        item = [int(i.strip()) for i in line.split(',')]
        dataset.append(item)

# Pick k centroids
def initialize_centroids(data_set, k):
    centers = []
    dimensions = len(data_set[0])
    min_max = defaultdict(int)
    for point in data_set:
        for i in range(dimensions):
            val = point[i]
            min_key = 'min_%d' % i
            max_key = 'max_%d' % i
            if min_key not in min_max or val < min_max[min_key]:
                min_max[min_key] = val
            if max_key not in min_max or val > min_max[max_key]:
                min_max[max_key] = val
    for i in range(k):
        rand_point = []
        for j in range(dimensions):
            min_val = min_max['min_%d' % j]
            max_val = min_max['max_%d' % j]
            rand_point.append(uniform(min_val, max_val))
        centers.append(rand_point)
    return centers


def point_average(points):
    dimension_number = len(points[0])
    center = []
    for dimension in range(dimension_number):
        dim_sum = 0
        for point in points:
            dim_sum += point[dimension]
        center.append(dim_sum / float(len(points)))
    return center


def euclidean_distance(a, b):
    distance = 0.0
    # Add -1 to ignore the output value
    for i in range(len(a) - 1):
        distance += pow((a[i] - b[i]), 2)
    return math.sqrt(distance)


def update_centers(data_set, assignments):
    new_means = defaultdict(list)
    centers = []
    for assignment, point in zip(assignments, data_set):
        new_means[assignment].append(point)
    for points in new_means.values():
        centers.append(point_average(points))
    return centers


def assign_points(data_points, centers):
    assignments = []
    for point in data_points:
        shortest = math.inf
        shortest_index = 0
        for i in range(len(centers)):
            val = euclidean_distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def k_means(dataset, k):
    centers = initialize_centroids(dataset, k)
    assignments = assign_points(dataset, centers)
    old_assignments = None
    final_centers = []
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        final_centers = new_centers
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    for i, color in zip(final_centers, colors):
        plt.scatter(i[0], i[1],
                    label="centroid-" + str(colors.index(color)),
                    color=color,
                    marker="*", s=100)
    return assignments


def find_coordinate_values(dataset):
    x = []
    y = []
    for i in dataset:
        x.append(i[0][0])
        y.append(i[0][1])
    return [x, y]


if "__main__" == __name__:

    while True:
        k = int(input("Please enter the k-value (1-10): "))
        if (k >= 1 and k <= 10):
            break
        else:
            print("You entered an invalid number... Try again!")

    f = plt.figure()

    assignments = k_means(dataset, k)

    result = []
    for i, j in zip(dataset, assignments):
        result.append((i, j))

    result = sorted(result, key=lambda x: x[1])
    L = [list(v) for k, v in itertools.groupby(result, lambda x: x[1])]


    for i, color in zip(L, colors):
        x = find_coordinate_values(i)[0]
        y = find_coordinate_values(i)[1]
        plt.scatter(x, y, label="Cluster " + str(colors.index(color)), color=color,
                    marker=".", s=30)

    plt.xlabel('Income')
    plt.ylabel('Spend')
    plt.title('Income-Spend Clustering Graph (k = ' + str(k) + ')')
    plt.legend()
    plt.show()
    print("Creating PDF...", end="")
    f.savefig("plot.pdf", bbox_inches='tight')
    print("DONE!")
