
# Project 1: Search Algorithms in Action

## Project Team Members

Merve Çağlarer - 160709049  
Fatih Saraçoğlu - 160709001  

## Task

Implementing following search algorithms on a graph given as an input file:  
  
- Breadth-first search (BFS)  
- Depth-first search (DFS)  
- Uniform-cost search (UCS)  
  
## Input  
  
<img src="https://drive.google.com/uc?export=view&id=1MrKnNgTtwtyKgPswv9MUyHninxmMPE5J" alt="graph" width="54%"/>  
  
Above figure illustrates a sample graph and the corresponding input file:

```
A:{A:0, B:6, C:4, D:3, E:0, F:0, G:0}  
B:{A:6, B:0, C:2, D:0, E:4, F:0, G:0}  
C:{A:4, B:2, C:0, D:2, E:0, F:8, G:0}  
D:{A:3, B:0, C:2, D:0, E:3, F:0, G:0}  
E:{A:0, B:4, C:0, D:3, E:0, F:7, G:6}  
F:{A:0, B:0, C:8, D:0, E:7, F:0, G:6}  
G:{A:0, B:0, C:0, D:0, E:6, F:6, G:0}  
```
  
## Usage  
  
In order to run the program, you should give the text file as a command line argument:

```
$ python3 search.py graph.txt
```
  
## Output  
  
After entering initial and goal states, the **shortest path** between these states will be printed for each search algorithm if it's possible.

Suppose that initial state and goal state are `A` and `G`, respectively. The output will be:
```
BFS : A - B - E - G
DFS : A - B - C - D - E - F - G
UCS : A - D - E - G
```