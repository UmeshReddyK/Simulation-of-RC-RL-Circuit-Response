
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
=======
# Constants for the RC circuit
R = 1000  # Resistance in ohms
C = 1e-6  # Capacitance in farads
V_in = 5  # Input voltage in volts
time = np.linspace(0, 0.05, 500)  # Time array (0 to 50 ms)

# Time constant (tau) for the RC circuit
tau = R * C

# RC Charging: Voltage across the capacitor during charging
V_c_charge = V_in * (1 - np.exp(-time / tau))

# RC Discharging: Voltage across the capacitor during discharging
V_c_discharge = V_in * np.exp(-time / tau)

