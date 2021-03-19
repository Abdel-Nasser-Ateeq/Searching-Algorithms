# Searching-Algorithms
Searching-Algorithms

This project is trying to solve the Tower of Hanoi problem using Uniform Cost Search (UCS) and A* algorithms.

This project presents a general form for the ToH problem by the following:

    1. We might have from 3 to 6 stacks.
    2. We might have from 3 to 10 disks.
    3. There are 2 types of stacks:
        a. Wide stacks: the cost of taking the upper disk or placing a disk on top of such stacks is 2.
        b. Narrow stacks: the cost of taking the upper disk or placing a disk on top of such stacks is 1.

The input is:

    1. The Number of stacks.
    2. The Number of Disks.
    3. The goal state.
    4. The current state.
    5. Which stacks are wide.

The output is:
    
    1. A list of all movements from the start state to the goal state.
    2. The number of nodes expanded from the fringe until the goal is reached for each algorithm.


Note: This is the 1st version of the project. The A* algorithm needs to be updated to calculate the total cost instead of the subsequent cost.
