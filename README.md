# HW3 A* Pathfinding

This repository contains a simple A* implementation wired to the provided helper `eastgate_helper.py`.

## What it does
- Finds a 4-directional path (up/down/left/right) on a grid.
- Avoids obstacles where `grid[r][c] == 1`.
- Uses per-cell movement costs when entering a cell from `get_terrain_costs`.
- Heuristic: Manhattan distance (admissible/consistent with 4-dir moves and non-negative costs).

## Files
- `eastgate_astar.py` — Implementation of `a_star(grid, start, goal, costs)` and an executable `main()` that calls `eastgate_helper.test_scenarios(a_star)` to print paths.
- `eastgate_helper.py` — Provided; not modified.

## How to run (Windows PowerShell)
```powershell
python .\eastgate_astar.py
```
You should see three printed paths corresponding to the test scenarios.

## Notes
- Movement cost equals the cost of the destination cell you are moving into.
- If start or goal is blocked or out of bounds, the function returns `None`.
- The code defaults all costs to 1 if a cost grid is not provided.