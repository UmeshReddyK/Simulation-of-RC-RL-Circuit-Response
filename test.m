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
