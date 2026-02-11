# BE AIML – Artificial Intelligence Lab Experiments  

This repository contains **Artificial Intelligence Laboratory experiments** for  
**B.E. Artificial Intelligence & Machine Learning (AIML)**.

**Student Name:** Kamesh  
**Subject:** Artificial Intelligence Lab  
**Languages Used:** Java, Python  

---

## 📂 Experiments List  

---

## Experiment 1  

### Title: Solving N-Queens Problem  

**Aim:**  
To implement the N-Queens problem using backtracking in Python.

**Description:**  
The N-Queens problem is a constraint satisfaction problem where N queens must be placed on an N×N chessboard such that no two queens attack each other.

**Algorithm:**  
1. Place a queen in the first column  
2. Check if the position is safe  
3. If safe, move to the next column  
4. If not safe, backtrack  
5. Repeat until all queens are placed  

**File:** `queens.py`  

**Output / Result:**  

<img src="images/experiment1.png" width="400"/>

---

## Experiment 2  

### Title: A* Algorithm  

**Aim:**  
To implement the A* search algorithm in Python.

**Description:**  
A* is a heuristic search algorithm used to find the shortest path between nodes in a graph.  

f(n) = g(n) + h(n)

Where:  
g(n) = cost from start node  
h(n) = heuristic estimate to goal  

**Algorithm:**  
1. Initialize open and closed lists  
2. Add start node to open list  
3. Select node with lowest f(n)  
4. Expand neighbors  
5. Repeat until goal is reached  

**File:** `a*.py`  

**Output / Result:**  

<img src="images/experiment2.png" width="400"/>

---

## Experiment 3  

### Title: Hill Climbing Algorithm  

**Aim:**  
To implement the Hill Climbing algorithm using Java.

**Description:**  
Hill Climbing is a local search algorithm that continuously moves towards increasing value to find the peak solution.

**Algorithm:**  
1. Start with an initial state  
2. Evaluate neighboring states  
3. Select the best neighbor  
4. Move to that neighbor  
5. Repeat until no better neighbor exists  

**File:** `hillclimb.java`  

**Output / Result:**  

<img src="exp3/hillclimb.png" width="400"/>

---

## Experiment 4  

### (i) Minimax Algorithm  

**Aim:**  
To implement the Minimax algorithm for decision-making in game theory.

**Description:**  
Minimax is a recursive algorithm used in two-player games where one player maximizes and the other minimizes.

**Algorithm:**  
1. Define the game tree  
2. Assign utility values to terminal states  
3. Recursively evaluate nodes  
4. Choose optimal move  

**File:** `exp4/minmax.py`  

**Output / Result:**  

<img src="exp4/minmax.png" width="400"/>

---

### (ii) Alpha-Beta Pruning  

**Aim:**  
To implement Alpha-Beta Pruning to optimize Minimax.

**Description:**  
Alpha-Beta pruning reduces the number of nodes evaluated by eliminating branches that do not affect the final decision.

**Algorithm:**  
1. Initialize alpha = -∞ and beta = +∞  
2. Apply Minimax logic  
3. Prune when beta ≤ alpha  
4. Return optimal value  

**File:** `exp4/alpha-beta.py`  

**Output / Result:**  

<img src="exp4/alpha-beta.png" width="400"/>

---

## Experiment 5  

**Title:** _To be added_  
**Description:** _To be added_  

---

## 📁 Folder Structure  

AI-Lab-Experiments/
│
├── queens.py
├── a*.py
├── hillclimb.java
├── README.md
│
├── images/
│   ├── experiment1.png
│   ├── experiment2.png
│
├── exp3/
│   └── hillclimb.png
│
└── exp4/
    ├── minmax.py
    ├── alpha-beta.py
    ├── minmax.png
    └── alpha-beta.png

---

## ✅ Conclusion  

This repository is created for academic purposes to understand and implement various Artificial Intelligence algorithms as part of the BE AIML curriculum.
