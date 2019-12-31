import math
import matplotlib.pyplot as plt
from multiprocessing.pool import ThreadPool

train_set = []
with open('train.txt', 'r') as train:
    lines = train.read().splitlines()
    for line in lines[1:]:
        values = [float(value.strip()) for value in line.split(',')]
        train_set.append(values)

test_set = []
with open('test.txt', 'r') as test:
    lines = test.read().splitlines()
    for line in lines[1:]:
        values = [float(value.strip()) for value in line.split(',')]
        test_set.append(values)
number_of_instance = len(test_set)


# Calculate euclidean distance between two instances
def euclidean_distance(instance1, instance2):
    distance = float(0)
    # Add -1 to ignore the output value
    number_of_features = len(instance1) - 1
    for i in range(number_of_features):
        distance += pow((instance1[i] - instance2[i]), 2)
    return math.sqrt(distance)


# Calculate distances to each instance of train set from an instance in test set
# and choose k neighbors
def choose_neighbors(instance, k):
    neighbor_list = []
    distance_list = []
    for train_instance in train_set:
        distance = euclidean_distance(instance, train_instance)
        distance_list.append((train_instance, distance))
    desc_sorted_distance_list = sorted(distance_list, key=lambda x: x[1])
    for i in range(k):
        neighbor_list.append(desc_sorted_distance_list[i][0])
    return neighbor_list


# Classify the instance according to its neighbors
def classify(neighbor_list):
    labels = []
    for instance in neighbor_list:
        labels.append(instance[-1])
    label_of_instance = max(set(labels), key=labels.count)
    return label_of_instance


# Calculate accuracy rate by comparing labels
def calculate_accuracy(estimation_labels_of_instances):
    true_estimation_number = 0
    for i, instance in enumerate(test_set):
        if (estimation_labels_of_instances[i] == instance[-1]):
            true_estimation_number += 1
    accuracy_rate = float((true_estimation_number / len(test_set))) * 100
    return accuracy_rate


# Evaluate neighbors beforehand to decrease running time
def evaluate_neighbors(k):
    neighbors_list = []
    for instance in test_set:
        neighbors = choose_neighbors(instance, k)
        neighbors_list.append(neighbors)
    return neighbors_list


if __name__ == "__main__":

    while True:
        k = int(input("Please enter the k-value: "))
        if ((k > 1 and k < number_of_instance)):
            break
        else:
            print("You entered an invalid number... Try again!")

    # Apply threading to evaluate neighbors
    pool = ThreadPool(processes=2)
    async_result = pool.apply_async(evaluate_neighbors, (k,))
    neighbors_list = async_result.get()

    print("Evaluating the accuracies... ", end="")
    accuracies = []
    for i in range(k):
        labels = []
        for j in range(number_of_instance):
            label_of_instance = classify(neighbors_list[j][:i + 1])
            labels.append(label_of_instance)
        accuracy = calculate_accuracy(labels)
        accuracies.append(accuracy)
    print("DONE!")

    print("Plotting graph... ", end="")
    f = plt.figure()
    plt.plot([(i + 1) for i in range(k)], accuracies)
    plt.xlabel('k')
    plt.ylabel('Accuracy')
    plt.title('Accuracy Rate Graph (max. k = ' + str(k) + ')')
    plt.show()
    print("DONE!")

    print("Creating PDF... ", end="")
    f.savefig("plot.pdf", bbox_inches='tight')
    print("DONE!")
