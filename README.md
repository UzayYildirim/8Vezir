# 8 Vezir Problemi

8 satranç veziri, iki vezirin birbirini tehdit etmemesi şartıyla bir satranç tahtasına nasıl yerleştirilir?

(2 vezir aynı sütun, satır veya köşegen üzerinde olmamalıdır)

The 8 queens problem was first proposed by the chess player **Max Bezzel** in 1848. It was also studied by many mathematicians such as Gauss and Georg Cantor. The first solution was proposed by Franz Nauck in 1850 and also raised the "8 Queens Problem".

We know how much the maximum number of queens can be placed for each n x n chessboards. Neither attack the other, it is equal to n. One of the classic combinatorial problems is the eight queens problem, which is a method of placing eight queens on an 8 x 8 board, such as a chessboard, each of which **_do not conflict_** with another queen (**_they cannot attackç_**) The 8 Queens Problem has been generalized by placing _n_ queens so that the queens do not attack each other. The latest solution was found for the n = 26 value. The solution for n = 27 has not been found yet, since very high computational power is required.

**Multiple** methods can be shown to solve the 8 Queens Problem. Some of these are Brute Force, Genetic Algorithm, Hill Climbing, Random Walk and GBF/A methods. There will be 96 different solutions in an 8x8 table.

![enter image description here](https://i.ibb.co/MVxk9PM/tahta.png)

In the genetic algorithm method, a recursive method will be used, which will start from the first column at the top left, then place a queen in the second column and move it until it finds a place in the first column where the queen cannot attack.
![enter image description here](https://i.ibb.co/tmV44w3/gorsellestirme.png)

# Single Point Crossover

A waypoint is selected in the parent array. All data beyond this point in the organism array is exchanged between the two parents. Crossover points are selected with taking _Positional Bias_ into consideration.<br>

![enter image description here](https://i.ibb.co/brWzh2M/tekNokta.jpg)
![enter image description here](https://i.ibb.co/6P12bMv/tek-Nokta-2.jpg)
# Two Point Crossover

This is a special case of the N-point Crossover technique. Two points are randomly selected on the chromosomes (strandeds) and genetic material is changed at these points.
<br>
![enter image description here](https://i.ibb.co/hsDxMF9/2Nokta.jpg)
![enter image description here](https://i.ibb.co/XW0c6gg/2Nokta-2.jpg)
## Solution of 8 Queens Problem with Genetic Algorithm

First of all, the population size is found according to the board size. The initial population is randomly generated. The resulting chromosome candidates are then evaluated. After the evaluation, we move on to the next generation. The aim here is to select the ones that are considered to be the best among the chromosomes from the pool. A predetermined single point or double point cross is applied according to the user input. **Mutation** is applied to new offsprings that appear in the meantime. It is repeated until the best generation is found (i.e. the generation with queens that are not in a position to attack each other on the chessboard is detected) or until the maximum number of iterations is completed.

## How to use 8 Queens?

**NumPy library is required for the program to run. It can be installed using the command ** **“pip install numpy”** ** in the terminal.** [**Detailed information can be obtained from NumPy's site.**](https://numpy.org/install/)

When the script is launched, you will be asked for the board size, crossover type (single point/double point), whether to use mutations and the maximum number of iterations that can be made.

Recommended values:

Board Size: **8**  
Type of crossover: **1**  
Mutation usage: **yes**  
Maximum iterations: **2000**

Parameters should be given taking into account the system specifications, otherwise the process may take too long. For example, given the board size of 32 and the number of iterations high, it would not be feasible for the computer to complete the operation (with the current code) in terms of time complexity.

Then the program will start trying to solve the 8 Queens problem by creating the first population by following the given parameters.
![enter image description here](https://i.ibb.co/NnrDMcb/8-Vezir-Initial.jpg)
It will print the overall Fitness value of the generations on the screen every generation and when the process is complete:

**If the problem has been solved without reaching the maximum number of iterations:**

It will display the generation of queens that do not attack each other (ie, do not overlap) and the total number of iterations.

**If the script couldn't solve the problem without reaching the maximum number of iterations:**

It will display the total number of iterations.

You can exit the program using Enter key.



https://user-images.githubusercontent.com/105719360/171736613-f979408b-2b46-4079-9372-d757ced8b470.mp4



## Experiment and Results

In this study, two different techniques were experimented with. These are the **Single Point Crossover** and **Two Point Crossover** methods. It has been tried to determine which of these two techniques is more effective in solving the 8 Queens Problem using genetic algorithms.

**Conditions for the experiment:**

**For a choice of *8* board size:**

**CPU**: Intel(R) Core(TM) i5-8300H CPU @ 2.30GHz

**OS**: Windows 10 Pro 21H2 (Build Numarası 19044.1706)

**CPU Architecture**: 64-Bit (x86-64)

**Python Version**: Python 3.10

**Amount of RAM allocated for Python**: 12GB

**NumPy Library Version**: numpy-1.22.4-cp310-cp310-win_amd64.whl

<br>

**For a choice of *16* board size:**

**CPU**: AMD Ryzen 9 5950X 16-Core CPU @ 3.40GHz

**OS**: Windows Server 2019

**CPU Architecture**: 64-Bit (x86-64)

**Python Version**: Python 3.10

**Amount of RAM allocated for Python**: 3GB

**NumPy Library Version**: numpy-1.22.4-cp310-cp310-win_amd64.whl

The maximum iteration value for all tests is 2000.

Mutation feature was used in all tests.

![enter image description here](https://i.ibb.co/gyv29KX/8-Vezir-Sonuclar.jpg)


**As a result, it has been determined that the Single Point Crossover technique gives better results for the 8 Queens problem. To reach this result, the test was repeated at least 5 times for each type of crossover.**

Thanks for checking out 8 Queens!
