# Project 2: Solving CSPs

## Project Team Members

Merve Çağlarer - 160709049  
Fatih Saraçoğlu - 160709001  

## Task

Solving following puzzles using a CSP (Constraint Satisfaction Problem) solver tool like Google OR-Tools: 
  
- Kakuro puzzle (4 x 4)
- Futoshiki puzzle (4 x 4)

**Kakuro puzzle** is similar to crosswords, but instead of letters the board is filled with digits (from 1 to 9). The board's squares need to be filled in with these digits in order to sum up to the specified numbers. You are not allowed to use the same digit more than once to obtain a given sum. Each Kakuro puzzle has one and only solution.

**Futoshiki puzzle** is a board-based puzzle game, also known under the name Unequal. The purpose of the game is to discover the digits hidden inside the board's cells; each cell is filled with a digit between 1 and the board's size. On each row and column each digit appears exactly once. At the beginning of the game some digits might be revealed. The board might also contain some inequalities between the board cells; these inequalities must be respected and can be used as clues in order to discover the remaining hidden digits. Each puzzle is guaranteed to have a solution and only one.


## Input  

**Kakuro Puzzle**
  
<img src="https://drive.google.com/uc?export=view&id=1nWf8pU4Oxqmih80PUDhMjvrG3R5sPhV-" alt="graph" width="30%"/>  
  
Above figure illustrates a sample Kakuro Puzzle and the corresponding input file is:
```
22, 18, 7
20, 19, 8
```

**Futoshiki Puzzle**

<img src="https://drive.google.com/uc?export=view&id=1gF64jmk76b4p7H_EOwiOdgMIwZzSsECp" alt="graph" width="30%"/>  

Above figure illustrates a sample Futoshiki Puzzle and the corresponding input file is:

```
B2, 1
D4, 2
A1, A2
A4, B4
C2, C1
D2, C2
```


## Usage  

In this project, Google's CP Solver is used as a CSP solver tool. So, you need to install it before running the programs:

```
$ python3 -m pip install --upgrade --user ortools
```

In order to run the programs, you should give the text files as a command line argument:

```
$ python3 kakuros.py kakuro_input.txt
$ python3 futoshiki.py futoshiki_input.txt
```
  
## Output  

The solution of the corresponding Kakuro Puzzle will be like below:

<img src="https://drive.google.com/uc?export=view&id=1rkFVm9DY1zRSsNsvpfciuGTi52KyoEe2" alt="graph" width="30%"/>  

Representation of this solution is below:

```
x, 22, 18, 7
20, 9, 7, 4
19, 8, 9, 2
8, 5, 2, 1
```
The solution of the corresponding Futoshiki Puzzle will be like below:

<img src="https://drive.google.com/uc?export=view&id=1eGm7B4TBkHWy15-kA66Z668u2r6WhqWh" alt="graph" width="30%"/>  

Representation of this solution is below:
```
3, 2, 1, 4
4, 1, 2, 3
2, 3, 4, 1
1, 4, 3, 2
```

Programs will generate corresponding output file for each solution.