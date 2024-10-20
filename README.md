# RC/RL Circuit Transient Response Simulation

## Overview

This project simulates the transient response of *RC (Resistor-Capacitor)* and *RL (Resistor-Inductor)* circuits using MATLAB. The tool allows users to input circuit parameters such as resistance, capacitance/inductance, and initial conditions to generate plots of voltage and current over time. The goal is to understand how these circuits behave under different conditions using first-order differential equations.

## Features

- *RC Circuit Simulation*: Plots the voltage across the capacitor and current through the resistor over time.
- *RL Circuit Simulation*: Plots the current through the inductor and voltage across the resistor over time.
- *User Inputs*: Resistance (R), Capacitance (C), Inductance (L), Initial Conditions (Voltage or Current), and Simulation Time.
- *Visualization*: MATLAB generates the plots for the circuit responses.

## Structure

- *Team 1*: Developed the mathematical models for the transient response of RC and RL circuits.
- *Team 2*: Created the MATLAB scripts to plot the circuit responses.
- *Team 3*: Wrote test cases and provided documentation for the project.

## Getting Started

### Prerequisites

- MATLAB software installed on your computer.

### Usage

1. Clone the repository:
   bash
   git clone [https://github.com/UmeshReddyK/Simulation-of-RC-RL-Circuit-Response.git)](https://github.com/UmeshReddyK/Simulation-of-RC-RL-Circuit-Response.git)
   
2. Open MATLAB and navigate to the folder where the script is located.

3. Open the script file in MATLAB.

4. Run the scripts from /scripts folder in the MATLAB environment.
   

5. Input the required circuit parameters when prompted:
   - *Resistance (R)* in ohms
   - *Capacitance (C)* or *Inductance (L)* in farads or henries, respectively
   - *Initial Voltage/Current*
   - *Simulation Time*

6. MATLAB will generate and display the plots for the transient response.

## Mathematical Model

### RC Circuit

The voltage across the capacitor \(V_C(t)\) in an RC circuit is given by:


$$ V_C(t) = V_0 e^{-\frac{t}{RC}} $$


Where:
- \(V_0\) is the initial voltage across the capacitor,
- \(R\) is the resistance in ohms,
- \(C\) is the capacitance in farads,
- \(t\) is the time in seconds.

### RL Circuit

The current through the inductor \(I_L(t)\) in an RL circuit is given by:


$$ I_L(t) = I_0 e^{-\frac{R}{L}t} $$


Where:
- \(I_0\) is the initial current through the inductor,
- \(R\) is the resistance in ohms,
- \(L\) is the inductance in henries,
- \(t\) is the time in seconds.

## Testing

To validate the implementation, run the provided test cases in MATLAB. The tests ensure that the simulated responses match expected values for both RC and RL circuits.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

