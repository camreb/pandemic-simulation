# Pandemic Simulation

## Project Description
Pandemic simulation is credit project in my studies, created in Python using the Pygame library. The program simulates the spread of a disease within a population, taking into account various parameters such as infection probability, incubation period and more.

![Simulation Preview](assets/pandemic.gif)

## Requirements
To run the program, you need to have the following installed:
- Python 3.10
- Pygame
- Matplotlib
- NumPy

Install the required libraries with:
```sh
pip install -r requirements.txt
```

## Running the Simulation
To start the simulation, use the following command:
```sh
python pandemic.py
```

## Features
- Simulation of the population as moving points in a random direction with varying speed. Infection occurs through contact between persons within the infection range. Infected persons have a probability of recovery or death.
- After the simulation is completed, a graphic visualization of the pandemic progress is displayed (number of people infected, number of specific cases)
- Optimization method using a grid-based partitioning of the window, reducing computations only to neighboring cells
- Frame rate counter
- The simulation parameters can be adjusted.

## Configuration
Simulation parameters can be modified in the `config.py` file.

### Visualization Settings

The simulation includes predefined settings for screen size and colors:

- `WIDTH = 600`, `HEIGHT = 400`: Defines the dimensions of the simulation window.
- `COLOR_DEFINITIONS`: A dictionary containing RGB values for different colors used in the simulation.
  - "grey": Background and dead individuals
  - "light_grey": Grid color
  - "white": Healthy individuals
  - "red": Infected individuals
  - "blue": Immune individuals
- `COLORS`: A dictionary mapping states to corresponding colors for easier reference.


### Simulation Parameters
The `Pandemic` class includes key parameters that can be adjusted:

- `n_people` (default `1500`): Number of people in the simulation
- `size` (default `2`): Size of the visualized individuals
- `speed` (default `0.01`): Movement speed of individuals
- `infect_dist` (default `5`): Maximum distance at which infection can occur
- `recover_time` (default `1000`): Number of frames needed for recovery
- `immune_time` (default `3000`): Duration of immunity after recovery
- `prob_catch` (default `0.1`): Probability of infection upon contact with an infected person
- `prob_death` (default `0.0001`): Probability of death after infection

Example modification of parameters in the code:
```python
pandemic = Pandemic(n_people=1000, speed=0.02, infect_dist=10, prob_catch=0.2, prob_death=0.001)
```