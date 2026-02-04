import time
import math
from tabulate import tabulate

# Helium atom 
KB = 1.380649e-23
MASS = 6.646e-27    # Mass

def run_simulation(start_temp, end_temp, steps):
    data_log = []
    current_temp = start_temp
    
    # Temp drop every cycle
    decrement = (start_temp - end_temp) / steps

    print(f"\n[INITIATING THERMAL DRAIN: {start_temp}K to {end_temp}K]")
    print("-" * 50)

    for i in range(steps + 1):
        
        calc_temp = max(current_temp, 1e-20) 
        velocity = math.sqrt((3 * KB * calc_temp) / MASS)
        
        #KE = 1/2 m v^2
        ke = 0.5 * MASS * (velocity**2)
        
        status = "CLASSICAL" if current_temp > 0.01 else "QUANTUM LIMIT"
        
        # Table
        data_log.append([
            f"{i+1}", 
            f"{current_temp:.6f}", 
            f"{velocity:.4f}", 
            f"{ke:.2e}",
            status
        ])
        
        current_temp -= decrement
        time.sleep(0.1)  

    headers = ["Step", "Temp (K)", "Velocity (m/s)", "Kinetic Energy (J)", "State"]
    print(tabulate(data_log, headers=headers, tablefmt="grid"))

# Run 
run_simulation(start_temp=1.0, end_temp=0.0, steps=20)