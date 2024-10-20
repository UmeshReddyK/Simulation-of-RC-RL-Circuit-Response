
import numpy as np
import matplotlib.pyplot as plt

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
