import numpy as np
import matplotlib.pyplot as plt

# Constants for the RL circuit
R = 1000  # Resistance in ohms
L = 0.5  # Inductance in henries
V_in = 5  # Input voltage in volts
time = np.linspace(0, 0.05, 500)  # Time array (0 to 50 ms)

# Time constant (tau) for the RL circuit
tau = L / R

# RL Response: Current in the RL circuit during growth and decay
I_max = V_in / R  # Maximum current (Ohm's Law)
I_rl_growth = I_max * (1 - np.exp(-time / tau))  # Current growth
I_rl_decay = I_max * np.exp(-time / tau)  # Current decay
