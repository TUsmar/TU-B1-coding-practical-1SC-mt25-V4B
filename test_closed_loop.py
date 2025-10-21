import numpy as np
import matplotlib.pyplot as plt
import pandas as pt
from uuv_mission.dynamic import Mission, Submarine, ClosedLoop,Trajectory
from uuv_mission.terrain import plot_reference_and_terrain

def main():
    # Load mission from CSV (using forward slashes for path)
    mission = Mission.from_csv('data/mission.csv')
    
    # Create submarine and closed loop system
    sub = Submarine.__init__()

    closed_loop = ClosedLoop.__init__(sub, ClosedLoop.controller)
    
    # Run simulation with zero disturbances for testing
    T = len(mission.reference)
    disturbances = np.zeros(T)  # No disturbances for initial test

    
    
    # Run the closed-loop simulation
    Trajectory.plot_completed_mission(closed_loop.simulate(mission, disturbances),mission)
    
    # Create subplots for both visualizations
    #plt.figure(figsize=(12, 5))
    
    # First subplot: Reference and terrain
    #plt.subplot(1, 2, 1)
    #plot_reference_and_terrain(mission.reference, mission.cave_height, mission.cave_depth)
    #plt.title('Reference Path and Cave Terrain')
    
    # Second subplot: Simulation results

    #plt.subplot(1, 2, 2)
    #trajectory.plot_completed_mission(mission)
    #plt.title('Submarine Trajectory in Cave Environment')
    
    #plt.tight_layout()  # Adjust subplot spacing
    #plt.show()

if __name__ == "__main__":
    main()


