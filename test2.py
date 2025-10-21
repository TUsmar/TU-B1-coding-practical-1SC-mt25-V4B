import numpy as np
import matplotlib.pyplot as plt
import pandas as pt
from uuv_mission.dynamic import Mission, Submarine, ClosedLoop, Trajectory, Controller
from uuv_mission.terrain import plot_reference_and_terrain
#functions
# Create mission from CSV
def load_saved_missionProfile():
    mission = Mission.from_csv('data/mission.csv')
    return(mission)
# Create random mission
def generate_random_mission():
    mission = Mission.random_mission(duration=160, scale=2.0)
    #plot_reference_and_terrain(mission.reference, mission.cave_height, mission.cave_depth)
    return(mission)

# Create submarine instance
sub = Submarine()

# Create closed loop instance with submarine
closed_loop = ClosedLoop(sub)

# Setup simulation parameters
disturbance_noise=0.2

#generate the mission
mission=generate_random_mission()

#simulate and plot the mission
Trajectory.plot_completed_mission(ClosedLoop.simulate_with_random_disturbances(closed_loop, mission, variance=disturbance_noise), mission)