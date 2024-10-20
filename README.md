# RC/RL Circuit Response Simulation

## Problem Statement
The objective of this project is to develop a simulation tool that models the transient response of RC (Resistor-Capacitor) and RL (Resistor-Inductor) circuits. Users can input the parameters of the circuits to visualize the voltage or current response over time.

## Team Collaboration
- *Team 1*: Created the mathematical model for RC and RL circuits.
- *Team 2*: Developed plotting functions using Matplotlib.
- *Team 3*: Wrote test cases and documentation.

## Features
- Simulates voltage response for RC circuits.
- Simulates current response for RL circuits.
- Interactive plotting of results using Matplotlib.
- User-friendly input for circuit parameters.

## Mathematical Models
1. *RC Circuit*:
   - Voltage across the capacitor over time:  
   $$ V(t) = V_0 \cdot (1 - e^{-t / (R \cdot C)}) $$
   
2. *RL Circuit*:
   - Current through the inductor over time:  
   $$ I(t) = I_0 \cdot e^{-t / (L / R)}  $$

## Requirements
Make sure you have Python 3.x installed along with the following libraries:
- numpy
- matplotlib

You can install the required libraries using pip:
bash
```
pip install numpy matplotlib
```

## Usage
1. Clone the repository to your local machine:
   bash
   
```
   git clone https://github.com/UmeshReddyK/Simulation-of-RC-RL-Circuit-Response.git rc-rl-circuit-simulation

   cd rc-rl-circuit-simulation
```

2. Run the simulation script:
   bash
   ```
   python rc_rl_circuit_simulation.py
   ```

3. Follow the prompts to enter the circuit parameters:
   - For RC Circuit: Input resistance (R), capacitance (C), initial voltage (V0), end time, and time step.
   - For RL Circuit: Input resistance (R), inductance (L), initial current (I0), end time, and time step.

4. The results will be displayed in graphical form.

## Example
An example run for an RC circuit with R = 100Ω, C = 0.01F, and V0 = 10V will display a plot of the voltage response over time.

## Test Cases
Test cases are included to validate the functionality of the simulation. Ensure that all tests pass by running the test suite:
bash
```
python rc_rl_circuit_simulation.py`
```

## Documentation
Documentation for the project is available in the docs folder. It includes detailed explanations of the mathematical models, usage instructions, and examples.

## Contributing
We welcome contributions! Please fork the repository and submit a pull request. Ensure that your code adheres to the project's coding standards and includes appropriate test coverage.

## Acknowledgements
Thank you to all team members for their collaboration and contributions to this project.
