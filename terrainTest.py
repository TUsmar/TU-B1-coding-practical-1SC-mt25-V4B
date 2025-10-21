import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from uuv_mission.terrain import plot_reference_and_terrain
from uuv_mission.dynamic import Mission

# Load mission from CSV
#terraindata = Mission.from_csv('data\mission.csv')
#test for random mission generation
terraindata = Mission.random_mission(duration=200, scale=2.0)
#plt.figure()
#plt.plot(terraindata.reference, 'b')
#plt.plot(terraindata.cave_depth, 'r')
#plt.plot(terraindata.cave_height, 'r')
#plt.show()
# Plot the reference and terrain data
plot_reference_and_terrain(terraindata.reference, terraindata.cave_height, terraindata.cave_depth)

