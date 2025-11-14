# A* Pathfinding Algorithm Implementation

A Python implementation of the A* pathfinding algorithm with 8-directional movement support, terrain costs, and grid visualization.

## Overview

This project implements the A* search algorithm to find optimal paths on a 2D grid with obstacles and variable terrain costs. The implementation supports both orthogonal (up/down/left/right) and diagonal movement, making it suitable for pathfinding in games, robotics, and spatial planning applications.

## Features

- **8-Directional Movement**: Supports both orthogonal and diagonal movement with appropriate cost calculations
- **Terrain Cost System**: Different cells can have different traversal costs (e.g., slow zones, mud, water)
- **Obstacle Avoidance**: Automatically navigates around walls and blocked cells
- **Optimized Heuristic**: Uses diagonal distance heuristic for accurate pathfinding with 8-directional movement
- **Path Visualization**: Built-in grid visualization showing paths, obstacles, and terrain costs
- **Multiple Test Scenarios**: Includes pre-configured test cases to validate the algorithm

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/robertbiv/python-web-scraper-and-data-visualizer.git
cd python-web-scraper-and-data-visualizer
```

2. No additional installation needed - the project uses only Python standard library modules.

## Usage

### Basic Usage

Run the main script to execute all test scenarios:

```bash
python eastgate_astar.py
```

### Example Output

```
Path from (0, 0) to (4, 4): [(0, 0), (1, 0), (2, 0), (3, 1), (4, 2), (4, 3), (4, 4)]
Path from (0, 0) to (4, 4): [(0, 0), (1, 0), (2, 0), (3, 1), (4, 2), (4, 3), (4, 4)]
Path from (2, 0) to (4, 4): [(2, 0), (3, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

Grid Visualization:
Costs:
1 2 1 1 1 
1 1 1 1 1 
1 1 1 2 1 
1 1 1 1 1 
1 1 2 1 1 

Grid with path:
S . . # . 
* # . # . 
* # . . . 
. * # # . 
# . * * G
```

Legend:
- `S` = Start position
- `G` = Goal position
- `*` = Path
- `#` = Wall/Obstacle
- `.` = Open cell

### Using the A* Function in Your Code

```python
from eastgate_astar import a_star
from eastgate_helper import get_office_grid, get_terrain_costs

# Get the grid and costs
grid = get_office_grid()
costs = get_terrain_costs(grid)

# Find a path from (0, 0) to (4, 4)
start = (0, 0)
goal = (4, 4)
path = a_star(grid, start, goal, costs)

if path:
    print(f"Path found: {path}")
else:
    print("No path found")
```

## Project Structure

```
.
├── README.md              # This file
├── eastgate_astar.py      # A* algorithm implementation and visualization
├── eastgate_helper.py     # Helper functions for grid and test scenarios
├── Homework-3_convertedToPDF.pdf  # Project documentation
└── RobertBennethum441Report.docx  # Project report
```

## Algorithm Details

### A* Algorithm

The A* algorithm is a graph traversal and pathfinding algorithm that uses a best-first search strategy. It evaluates nodes by combining:

- **g(n)**: The actual cost from the start node to node n
- **h(n)**: The estimated cost from node n to the goal (heuristic)
- **f(n) = g(n) + h(n)**: The total estimated cost

### Heuristic Function

This implementation uses a **diagonal distance heuristic**:

```
h(n) = min(dx, dy) * √2 + |dx - dy|
```

Where:
- `dx` = absolute difference in x-coordinates
- `dy` = absolute difference in y-coordinates
- √2 ≈ 1.414 (cost of diagonal movement)

This heuristic is admissible (never overestimates) and consistent for 8-directional movement.

### Movement Costs

- **Orthogonal moves** (up/down/left/right): cost = terrain_cost × 1.0
- **Diagonal moves**: cost = terrain_cost × 1.414 (√2)

The terrain cost is determined by the destination cell being entered.

## Key Functions

### `a_star(grid, start, goal, costs=None)`

Finds the optimal path from start to goal on the given grid.

**Parameters:**
- `grid`: 2D list where 0 = open, 1 = obstacle
- `start`: Tuple (row, col) for start position
- `goal`: Tuple (row, col) for goal position
- `costs`: Optional 2D list of terrain costs (defaults to 1 for all cells)

**Returns:**
- List of tuples representing the path from start to goal, or `None` if no path exists

### `show_grid(grid, path=None, costs=None)`

Visualizes the grid with the path, obstacles, and terrain costs.

**Parameters:**
- `grid`: 2D list representing the grid
- `path`: Optional list of coordinates representing the path
- `costs`: Optional 2D list of terrain costs

## Test Scenarios

The `eastgate_helper.py` module provides three test scenarios:

1. **Standard path**: From (0, 0) to (4, 4) with default obstacles
2. **Reuse test**: Same path to verify consistency
3. **Alternative start**: From (2, 0) to (4, 4) with an additional dynamic obstacle

## Implementation Notes

- Movement cost equals the cost of the destination cell you are moving into
- If start or goal is blocked or out of bounds, the function returns `None`
- The code defaults all costs to 1 if a cost grid is not provided
- Diagonal movement is properly weighted at √2 ≈ 1.414 times the terrain cost
- The algorithm uses a priority queue (heap) for efficient node selection

## License

This project is part of an academic assignment. Please refer to your institution's academic integrity policies regarding use and distribution.

## Contributing

This is an academic project. If you find issues or have suggestions, feel free to open an issue or submit a pull request.

## Author

Robert Bennethum