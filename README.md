<div align="center">

# 🧠 The AI Laboratory
**Classical AI & Advanced Search Heuristics**

[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)]()
[![Repository](https://img.shields.io/badge/Repository-AI--Experments-purple.svg)](https://github.com/vivikt-patra/AI-Experments)

*Exploring the foundations of machine intelligence through state-space search, optimization, and adversarial game theory.*

</div>

---

## 🎯 Project Overview
This repository contains clean, from-scratch implementations of 10 foundational Artificial Intelligence algorithms in Python. It serves as a practical exploration of how autonomous agents navigate complex spaces, solve constraint problems, and make optimal decisions in zero-sum environments.

## 🌟 The Algorithm Arsenal

<details open>
<summary><b>1. Uninformed Search (Blind Navigation)</b></summary>
<br>

* **Breadth-First Search (BFS):** [`BFS.py`](BFS.py) - Guarantees the shortest path in unweighted environments by exploring level-by-level.
* **Depth-First Search (DFS):** [`DFS.py`](DFS.py) - A memory-efficient approach that dives deep into single paths before backtracking.

</details>

<details open>
<summary><b>2. Informed Search (Heuristic Navigation)</b></summary>
<br>

* **A* (A-Star) Search:** [`A_algorithm.py`](A_algorithm.py) - Combines exact path cost `g(n)` with heuristic estimation `h(n)` to find the mathematical optimal route efficiently.
* **Hill Climbing:** [`hill_climbing.py`](hill_climbing.py) - A local search mathematical optimization technique that steps toward the highest neighboring value to find local/global peaks.

</details>

<details open>
<summary><b>3. Adversarial Search (Game Theory)</b></summary>
<br>

* **Minimax Algorithm:** [`minimax_algorithm.py`](minimax_algorithm.py) - The backbone of zero-sum game AI, calculating moves by assuming an opponent will always play optimally.
* **Alpha-Beta Pruning:** [`alpha_beta_pruning.py`](alpha_beta_pruning.py) - Drastically optimizes Minimax by mathematically pruning branches of the decision tree that cannot affect the final outcome.
* **Tic-Tac-Toe Environment:** [`tic_tac_toe.py`](tic_tac_toe.py) - A complete game state implemented to test adversarial decision-making agents.

</details>

<details open>
<summary><b>4. State-Space & Constraint Satisfaction</b></summary>
<br>

* **8 Queens Problem:** [`eight_queen.py`](eight_queen.py) - Solves the challenge of placing 8 chess queens on a board such that no two queens threaten each other.
* **Traveling Salesman (TSP):** [`tsp.py`](tsp.py) - Solves the classic NP-hard routing problem to find the shortest possible loop connecting a set of coordinates.
* **Water Jug Problem:** [`water_jug.py`](water_jug.py) - Explores state-space search to measure an exact volume of water using two ungraduated jugs and strict capacity constraints.

</details>

---

## 🚀 Quick Start

To run these algorithms locally on your machine:

```bash
# 1. Clone the repository
git clone https://github.com/vivikt-patra/AI-Experments.git

# 2. Navigate into the directory
cd AI-Experments

# 3. Execute any algorithm (Each file contains verified terminal execution output under #output)
python BFS.py
python A_algorithm.py
python minimax_algorithm.py
python alpha_beta_pruning.py
```
