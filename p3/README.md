# Project 3: Solving Knapsack Using Genetic Algorithms  

## Project Team Members

Merve Çağlarer - 160709049  
Fatih Saraçoğlu - 160709001

## Task
  
In this project, we will have a knapsack and some objects. Our aim is to put these objects into the knapsack without exceeding its capacity while we're trying to maximize the benefit.
 
## Input 

The program accepts three text files to get the required information:

`c.txt` : capacity of the knapsack  
`w.txt` : weights of objects  
`v.txt` : values of objects  

When the program is executed, parameters that are needed for the steps of the genetic algorithm will be gotten from the user.
   
## Usage

```
$ python3 knapsack_ga.py
```

After executing above command, the program will start to ask the parameters from the user as represented below:  

<img src="https://drive.google.com/uc?export=view&id=1u3OjjBRQ9f55N68swlKas0Avt8toyvlm" alt="demo-of-knapsack-ga" width="80%"/>
  
  

## Output

After applying genetic algorithm, the fittest chromosome’s weight, value and also itself will be written to the output file named **output.txt**.

With given example values, the best solution is:

`chromosome` : 101010111000011  
`weight` : 749  
`value` : 1458  

In this project, the aim is to get close to the best solution as soon as possible. 


## Analysis

Some graphs about how close our implementation is to the best solution are given with different parameters below:

<img src="https://drive.google.com/uc?export=view&id=1J6ZNAkMI-q3iroH0F3tQQBmrX3V7RjCf" alt="analysis-of-knapsack-ga" width="80%"/>

<img src="https://drive.google.com/uc?export=view&id=16O6UBI55R1LV3p813xiOcftyZ8vgFwIy" alt="analysis-of-knapsack-ga" width="80%"/>
