# Plotting the results
plt.figure(figsize=(10, 5))

# Plot for current growth
plt.subplot(1, 2, 1)
plt.plot(time, I_rl_growth, label="Growth")
plt.title('RL Circuit Current Growth')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.grid(True)

# Plot for current decay
plt.subplot(1, 2, 2)
plt.plot(time, I_rl_decay, label="Decay", color='orange')
plt.title('RL Circuit Current Decay')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.grid(True)

# Show the plots
plt.tight_layout()
plt.show()


# Plotting the results
plt.figure(figsize=(10, 5))

# Plot for charging
plt.subplot(1, 2, 1)
plt.plot(time, V_c_charge, label="Charging")
plt.title('RC Circuit Charging')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)

# Plot for discharging
plt.subplot(1, 2, 2)
plt.plot(time, V_c_discharge, label="Discharging", color='orange')
plt.title('RC Circuit Discharging')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)

# Show the plots
plt.tight_layout()
plt.show()
