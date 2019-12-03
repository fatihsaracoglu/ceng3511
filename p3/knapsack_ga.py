import random

fc = open('./c.txt', 'r')
fw = open('./w.txt', 'r')
fv = open('./v.txt', 'r')
fout = open('./out.txt', 'w')


c = int(fc.readline())
w = []
v = []
for line in fw:
    w.append(int(line))
for line in fv:
    v.append(int(line))
totalItem = len(w)

print('Capacity :', c)
print('Weight :', w)
print('Value : ', v)

populationSize = int(input('Size of population : '))
generationNumber = int(input('Max number of generation : '))
print('\nParent Selection\n---------------------------')
print('(1) Roulette-wheel Selection')
print('(2) K-Tournament Selection')
parentSelection = int(input('Which one? '))
k = 0
if parentSelection == 2:
    k = int(input('k=? (between 1 and ' + str(populationSize) + ') '))

print('\nN-point Crossover\n---------------------------')
n = int(input('n=? (between 1 and ' + str(len(w) - 1) + ') '))

print('\nMutation Probability\n---------------------------')
mutationProbability = float(input('prob=? (between 0 and 1) '))

print('\nSurvival Selection\n---------------------------')
print('(1) Age-based Selection')
print('(2) Fitness-based Selection')
survivalSelection = int(input('Which one? '))
elitismInput = input('Elitism? (Y or N) ')
if (elitismInput.lower() == "y"):
    elitism = True
else:
    elitism = False


def calculateFitness(chromosome):
    value = 0
    for i, gene in enumerate(chromosome):
        if gene == 1:
            value += v[i]
    return value

def calculateWeight(chromosome):
    weight = 0
    for i, gene in enumerate(chromosome):
        if gene == 1:
            weight += w[i]
    return weight


def formatChromosomeList(chromosomes):
    formatedChromosomeList = []
    for chromosome in chromosomes:
        pair = (chromosome, calculateFitness(chromosome))
        formatedChromosomeList.append(pair)
    return formatedChromosomeList


print('\n----------------------------------------------------------')
print('initalizing population')
initalPopulation = []
for i in range(populationSize):
    tempChromosome = []
    for j in range(len(w)):
        tempChromosome.append(random.randint(0, 1))
    initalPopulation.append(tempChromosome)

initalPopulation = formatChromosomeList(initalPopulation)
for i, individual in enumerate(initalPopulation):
    print(i + 1, ":", individual)


def eliminationOverWeight(population):
    eliminatedPopulation = []
    for individual in population:
        if (calculateWeight(individual[0]) <= c):
            eliminatedPopulation.append(individual)
    return eliminatedPopulation


####### PARENT SELECTION #######

def rouletteWheelParentSelection(population):
    parents = []
    population = eliminationOverWeight(population)
    sumOfFitnessValues = sum(individual[1] for individual in population)
    probabilities = []
    sumOfProbabilities = 0
    for individual in population:
        probability = sumOfProbabilities + (individual[1] / sumOfFitnessValues)
        probabilities.append(probability)
        sumOfProbabilities += probability
    while (len(parents) < populationSize):
        pointer = random.uniform(0, 1)
        for i, individual in enumerate(population):
            if (pointer <= probabilities[i]):
                parents.append(individual)
                break
    return parents

def kTournamentParentSelection(population):
    parents = []
    temp = []
    population = eliminationOverWeight(population)
    for i in range(populationSize):
        for i in range(k):
            chosen = random.choice(population)
            temp.append(chosen)
        individualWithHighestFtValue = max(temp, key=lambda item: item[1])
        parents.append(individualWithHighestFtValue)
    return parents

####### CROSSOVER #######

def nPointCrossover(parents):
    childList = []
    while (len(childList) < populationSize):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        if (parent1 == parent2):
            parent2 = random.choice(parents)
        chunkSize =  int(totalItem / n)
        splitedParent1 = [parent1[0][i:i + chunkSize] for i in range(0, len(parent1[0]), chunkSize)]
        totalParts = len(splitedParent1)
        splitedParent2 = [parent2[0][i:i + chunkSize] for i in range(0, len(parent2[0]), chunkSize)]
        child1 = []
        child2 = []
        turn = True
        for i in range(totalParts):
            if (turn):
                child1 += splitedParent1[i]
                child2 += splitedParent2[i]
                turn = False
            else:
                child1 += splitedParent2[i]
                child2 += splitedParent1[i]
                turn = True

        childList.append(child1)
        childList.append(child2)
    return formatChromosomeList(childList)


###### MUTATION #######

def mutate(chromosome):
    randomProbability = random.uniform(0, 1)
    if randomProbability <= mutationProbability:
        randomGeneIndex = random.randint(0, totalItem - 1)
        if (chromosome[randomGeneIndex] == 0):
            chromosome[randomGeneIndex] = 1
        else:
            chromosome[randomGeneIndex] = 0

    return chromosome


def mutation(childs):
    for i, chromosome in enumerate(childs):
        chromosomeAfterMutation = mutate(chromosome[0])
        if (chromosomeAfterMutation != chromosome[0]):
            childs[i][0] = chromosomeAfterMutation
            childs[i][1] = calculateFitness(chromosomeAfterMutation)

    return childs


###### SURVIVAL SELECTION ######

def fitnessBasedSelection(population, childs):
    newPopulation = []

    if (elitism):
        individualWithMaxFtValue = max(population, key=lambda item: item[1])
        newPopulation.append(individualWithMaxFtValue)
        population.remove(individualWithMaxFtValue)

    totalPopulation = population + childs
    sortedPopulation = sorted(totalPopulation, key=lambda x: x[1], reverse=True)

    while (len(newPopulation) < populationSize):
        for individual in sortedPopulation:
            newPopulation.append(individual)

    return newPopulation


def ageBasedSelection(population, childs):
    newPopulation = []

    chromosomeWithMaxFtValue = max(population, key=lambda item: item[1])

    if (elitism):
        newPopulation.append(chromosomeWithMaxFtValue)

    while (len(newPopulation) < populationSize):
        for individual in childs:
            newPopulation.append(individual)

    return newPopulation


def selectFittest(population):
    return max(population, key=lambda item: item[1])


def result(chromosome):
    return [chromosome[0], calculateWeight(chromosome[0]), chromosome[1]]


###### GENERATING PART ######

population = initalPopulation
generationCounter = 1
fitnessValues = []
generationList = []
while (generationCounter <= generationNumber):
        parents = []

        if (parentSelection == 1):
            parents = rouletteWheelParentSelection(population)
        elif (parentSelection == 2):
            parents = kTournamentParentSelection(population)

        childs = nPointCrossover(parents)

        newChilds = mutation(childs)

        if (survivalSelection == 1):
            population = ageBasedSelection(population, newChilds)
        elif (survivalSelection == 2):
            population = fitnessBasedSelection(population, newChilds)


        if (generationCounter == generationNumber):
            population = eliminationOverWeight(population)
            fittest = selectFittest(population)
            output = result(fittest)
            print('\n----------------------------------------------------------')
            print("After", generationCounter, "generations, the fittest chromosome and its weight and value:")
            print('chromosome: ' + str(output[0]))
            print('weight: ' + str(output[1]))
            print('value: ' + str(output[2]))
            
            fout.write('chromosome: ' + ''.join(str(i) for i in output[0]) + '\n')
            fout.write('weight: ' + str(output[1]) + '\n')
            fout.write('value: ' + str(output[2]))
            fout.close()

        generationCounter += 1
