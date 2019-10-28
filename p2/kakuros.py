import sys
from ortools.sat.python import cp_model


def kakuroSolver(column_input, row_input):
    model = cp_model.CpModel()

    minValue = 1
    maxValue = 9
    A1 = model.NewIntVar(minValue, maxValue, 'A1')
    A2 = model.NewIntVar(minValue, maxValue, 'A2')
    A3 = model.NewIntVar(minValue, maxValue, 'A3')
    B1 = model.NewIntVar(minValue, maxValue, 'B1')
    B2 = model.NewIntVar(minValue, maxValue, 'B2')
    B3 = model.NewIntVar(minValue, maxValue, 'B3')
    C1 = model.NewIntVar(minValue, maxValue, 'C1')
    C2 = model.NewIntVar(minValue, maxValue, 'C2')
    C3 = model.NewIntVar(minValue, maxValue, 'C3')

    variablesDict = {}

    variablesDict.update({'A1': A1})
    variablesDict.update({'A2': A2})
    variablesDict.update({'A3': A3})
    variablesDict.update({'B1': B1})
    variablesDict.update({'B2': B2})
    variablesDict.update({'B3': B3})
    variablesDict.update({'C1': C1})
    variablesDict.update({'C2': C2})
    variablesDict.update({'C3': C3})

    row1 = [A1, A2, A3]
    row2 = [B1, B2, B3]
    row3 = [C1, C2, C3]
    column1 = [A1, B1, C1]
    column2 = [A2, B2, C2]
    column3 = [A3, B3, C3]

    model.AddAllDifferent(row1)
    model.AddAllDifferent(row2)
    model.AddAllDifferent(row3)
    model.AddAllDifferent(column1)
    model.AddAllDifferent(column2)
    model.AddAllDifferent(column3)

    model.Add(A1 + B1 + C1 == int(column_input[0]))
    model.Add(A2 + B2 + C2 == int(column_input[1]))
    model.Add(A3 + B3 + C3 == int(column_input[2]))
    model.Add(A1 + A2 + A3 == int(row_input[0]))
    model.Add(B1 + B2 + B3 == int(row_input[1]))
    model.Add(C1 + C2 + C3 == int(row_input[2]))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:
        solution = [str(solver.Value(i)) for i in list(variablesDict.values())]
        return solution


def split_list(alist, parts=1):
    length = len(alist)
    return [alist[i * length // parts: (i + 1) * length // parts] for i in range(parts)]


if __name__ == "__main__":

    column = []
    row = []

    try:
        file_name = str(sys.argv[1])
        with open(file_name) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        column_and_row = []
        for line in content:
            if not len(line.strip()) == 0:
                column_and_row.append(line)

        column = [x.strip() for x in column_and_row[0].split(',')]
        row = [x.strip() for x in column_and_row[1].split(',')]
    except Exception as e:
        print("An unexpected error occurred while reading and parsing the file!")
        print("The problem may be missing command line argument...")

    splitedList = []

    try:
        resultList = kakuroSolver(column, row)
        splitedList = split_list(resultList, parts=3)
    except Exception as e:
        print("An unexpected error occurred while solving the CSP!")

    firstRow = "x, "
    columnValues = ', '.join(value for value in column)
    firstRow += columnValues + "\n"

    rows = ""
    for i, j in zip(splitedList, row):
        rows += j + ", "
        if j != row[-1]:
            rows += ', '.join(value for value in i) + "\n"
        else:
            rows += ', '.join(value for value in i)

    try:
        output = open('kakuro_output.txt', 'w')
        result = firstRow + rows
        output.write(result)
        output.close()
    except Exception as e:
        print("An unexpected error occurred while writing the output to the file!")
