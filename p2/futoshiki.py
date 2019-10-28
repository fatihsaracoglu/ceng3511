import sys
from ortools.sat.python import cp_model


def futoshikiSolver(unaryConstraints, binaryConstraints):
    model = cp_model.CpModel()

    minValue = 1
    maxValue = 4
    A1 = model.NewIntVar(minValue, maxValue, 'A1')
    A2 = model.NewIntVar(minValue, maxValue, 'A2')
    A3 = model.NewIntVar(minValue, maxValue, 'A3')
    A4 = model.NewIntVar(minValue, maxValue, 'A4')
    B1 = model.NewIntVar(minValue, maxValue, 'B1')
    B2 = model.NewIntVar(minValue, maxValue, 'B2')
    B3 = model.NewIntVar(minValue, maxValue, 'B3')
    B4 = model.NewIntVar(minValue, maxValue, 'B4')
    C1 = model.NewIntVar(minValue, maxValue, 'C1')
    C2 = model.NewIntVar(minValue, maxValue, 'C2')
    C3 = model.NewIntVar(minValue, maxValue, 'C3')
    C4 = model.NewIntVar(minValue, maxValue, 'C4')
    D1 = model.NewIntVar(minValue, maxValue, 'D1')
    D2 = model.NewIntVar(minValue, maxValue, 'D2')
    D3 = model.NewIntVar(minValue, maxValue, 'D3')
    D4 = model.NewIntVar(minValue, maxValue, 'D4')

    variablesDict = {}

    variablesDict.update({'A1': A1})
    variablesDict.update({'A2': A2})
    variablesDict.update({'A3': A3})
    variablesDict.update({'A4': A4})
    variablesDict.update({'B1': B1})
    variablesDict.update({'B2': B2})
    variablesDict.update({'B3': B3})
    variablesDict.update({'B4': B4})
    variablesDict.update({'C1': C1})
    variablesDict.update({'C2': C2})
    variablesDict.update({'C3': C3})
    variablesDict.update({'C4': C4})
    variablesDict.update({'D1': D1})
    variablesDict.update({'D2': D2})
    variablesDict.update({'D3': D3})
    variablesDict.update({'D4': D4})

    row1 = [A1, A2, A3, A4]
    row2 = [B1, B2, B3, B4]
    row3 = [C1, C2, C3, C4]
    row4 = [D1, D2, D3, D4]

    column1 = [A1, B1, C1, D1]
    column2 = [A2, B2, C2, D2]
    column3 = [A3, B3, C3, D3]
    column4 = [A4, B4, C4, D4]

    model.AddAllDifferent(row1)
    model.AddAllDifferent(row2)
    model.AddAllDifferent(row3)
    model.AddAllDifferent(row4)
    model.AddAllDifferent(column1)
    model.AddAllDifferent(column2)
    model.AddAllDifferent(column3)
    model.AddAllDifferent(column4)

    for k, v in unaryConstraints.items():
        model.Add(variablesDict.get(k) == v)

    for constraint in binaryConstraints:
        model.Add(variablesDict.get(constraint[0]) > variablesDict.get(constraint[1]))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:
        result = [str(solver.Value(i)) for i in list(variablesDict.values())]
        return result


def split_list(alist, parts=1):
    length = len(alist)
    return [alist[i * length // parts: (i + 1) * length // parts] for i in range(parts)]


def isInteger(v):
    try:
        int(v)
        return True
    except ValueError:
        return False


if __name__ == "__main__":

    unaryConstraintDictionary = {}
    binaryConstraintList = []

    try:
        file_name = str(sys.argv[1])
        with open(file_name) as f:
            content = f.readlines()
        content = [x.strip() for x in content]

        for line in content:
            if not len(line.strip()) == 0:
                constraint = [i.strip() for i in line.split(',')]
                if (isInteger(constraint[1])):
                    value = int(constraint[1])
                    unaryConstraintDictionary.update({constraint[0]: value})
                else:
                    binaryConstraintList.append(constraint)                   
    except Exception as e:
        print("An unexpected error occurred while reading and parsing the file!")
        print("The problem may be missing command line argument...")

    splitedList = []

    try:
        resultList = futoshikiSolver(unaryConstraintDictionary, binaryConstraintList)
        splitedList = split_list(resultList, parts=4)
    except Exception as e:
        print("An unexpected error occurred while solving the CSP!")

    solution = '\n'.join([', '.join([str(value) for value in row]) for row in splitedList])

    try:
        output = open('futoshiki_output.txt', 'w')
        output.write(solution)
        output.close()
    except Exception as e:
        print("An unexpected error occurred while writing the output to the file!")
