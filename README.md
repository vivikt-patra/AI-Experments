<div align="center">

# 🧠 The AI Laboratory
**Classical AI & Advanced Search Heuristics**

[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)]()
[![Repository](https://img.shields.io/badge/Repository-AI--Experiments-purple.svg)](https://github.com/vivikt-patra/AI-Experiments)

*Exploring the foundations of machine intelligence through state-space search, optimization, and adversarial game theory.*

</div>

---

## 🎯 Project Overview
This repository contains highly optimized, from-scratch implementations of 10 foundational Artificial Intelligence algorithms. It serves as a practical exploration of how autonomous agents navigate complex spaces, solve constraint problems, and make optimal decisions in zero-sum environments.

## 🌟 The Algorithm Arsenal

<details>
<summary><b>1. Uninformed Search (Blind Navigation)</b></summary>
<br>

* **Breadth-First Search (BFS):** Guarantees the shortest path in unweighted environments by exploring level-by-level.
* **Depth-First Search (DFS):** A memory-efficient approach that dives deep into single paths before backtracking.

</details>

<details>
<summary><b>2. Informed Search (Heuristic Navigation)</b></summary>
<br>

* **A* (A-Star) Search:** Combines exact path cost `g(n)` with heuristic estimation `h(n)` to find the mathematical optimal route efficiently.
* **Hill Climbing:** A local search mathematical optimization technique that steps toward the highest neighboring value to find local/global peaks.

</details>

<details>
<summary><b>3. Adversarial Search (Game Theory)</b></summary>
<br>

* **Minimax Algorithm:** The backbone of zero-sum game AI, calculating moves by assuming an opponent will always play optimally.
* **Alpha-Beta Pruning:** Drastically optimizes Minimax by mathematically pruning branches of the decision tree that cannot affect the final outcome.
* **Tic-Tac-Toe Environment:** A complete game state implemented to test the Minimax and Alpha-Beta agents.

</details>

<details>
<summary><b>4. State-Space & Constraint Satisfaction</b></summary>
<br>

* **8 Queens Problem:** Solves the challenge of placing 8 chess queens on a board such that no two queens threaten each other.
* **Traveling Salesman (TSP):** Solves the classic NP-hard routing problem to find the shortest possible loop connecting a set of coordinates.
* **Water Jug Problem:** Explores state-space search to measure an exact volume of water using two ungraduated jugs and strict capacity constraints.

</details>

---

## 🚀 Quick Start

To run these algorithms locally on your machine:

```bash
# 1. Clone the repository
git clone [https://github.com/vivikt-patra/AI-Experiments.git](https://github.com/vivikt-patra/AI-Experiments.git)

# 2. Navigate into the directory
cd AI-Experiments

# 3. Execute an algorithm (Example: A-Star)
python A_star.py
