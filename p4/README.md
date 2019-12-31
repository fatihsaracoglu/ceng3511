
# Project 4: Mobile Price Classification using KNN

## Project Team Members 

Fatih Saraçoğlu - 160709001  
Merve Çağlarer - 160709049

  
## Task

In this project, you are expected to implement a KNN classifier in order to help Bob.

Bob has started his own mobile company. He wants to give tough fight to big companies like Apple, Samsung etc.

He does not know how to estimate price of mobiles his company creates. In this competitive mobile phone market you cannot simply assume things. To solve this problem he collects sales data of mobile phones of various companies.

Bob wants to find out some relation between features of a mobile phone(eg: RAM, Internal Memory etc.) and its selling price. But he is not so good at Machine Learning. So he needs your help to solve this problem.

In this problem you do not have to predict actual price but a price range indicating how high the price is.

## Input

The program accepts a training dataset and also a test dataset.

In this project, a training dataset which consists of 1000 rows and 20 columns, and also a test dataset which has same number of rows and columns as training dataset will be used.


## Usage

```
$ python3 knn.py
```

Then, the program will ask you to enter the k value to evaluate accuracy values.

  

## Output


After running the algorithm, a graph that shows the accuracy values according to the k value will be written to the output file named **plot.pdf**.

An example for `k = 10`:

<img src="https://drive.google.com/uc?export=view&id=1ykc9jiIfOL9WblxQDKtJZDamOw0Syjs1" alt="knn-accuracy-graph" width="80%"/>