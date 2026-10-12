# Foundational AI Algorithms & Search Models

This repository contains implementations of 10 classic Artificial Intelligence algorithms, covering core concepts in graph traversal, heuristic search, adversarial decision-making, and constraint satisfaction.

## 🧠 Implemented Algorithms

### 1. Uninformed Search (Blind Search)
* **Breadth-First Search (BFS):** Explores a tree or graph level by level. Guarantees the shortest path in unweighted graphs.
* **Depth-First Search (DFS):** Explores as deep as possible along each branch before backtracking. Highly memory-efficient for deep trees.

### 2. Informed Search (Heuristic Search)
* **A* (A-Star) Algorithm:** A pathfinding algorithm that calculates the optimal route by combining the exact cost incurred so far with a heuristic estimate of the remaining distance.
* **Hill Climbing Algorithm:** A local search technique that continuously moves in the direction of increasing value to find a mathematical peak (local/global optimum).

### 3. Adversarial Search & Game Theory
* **Minimax Algorithm:** A decision rule used for minimizing the possible loss for a worst-case scenario. Essential for zero-sum games.
* **Alpha-Beta Pruning:** An optimization for the Minimax algorithm that drastically reduces the number of nodes evaluated by pruning branches that cannot influence the final decision.
* **Tic-Tac-Toe:** A classic zero-sum game implementation, typically serving as the environment to test the Minimax and Alpha-Beta algorithms.

### 4. Classic State-Space & Constraint Problems
* **8 Queens Problem:** An algorithmic puzzle requiring the placement of 8 chess queens on an 8x8 chessboard so that no two queens threaten each other.
* **Traveling Salesman Problem (TSP):** An optimization problem seeking the shortest possible route that visits a list of cities exactly once and returns to the origin.
* **Water Jug Problem:** A classic state-space search problem solving how to measure an exact volume of water using two ungraduated jugs of different capacities.

## 🚀 How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
