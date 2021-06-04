#! /usr/bin/python

import subprocess
import get_data
import sys
import time

if len(sys.argv) != 8:
    exit("Invalid number of inputs")

timeout = time.time() + 60   # 60 seconds from now
while time.time() < timeout:
    cartesian_stiffness=get_data.data_array('rostopic echo -n 1 /bh/CartesianImpedance_trajectory_controller/useful_data_to_analyze/cartesian_stiffness')
    nullspace_stiffness=get_data.data_array('rostopic echo -n 1 /bh/CartesianImpedance_trajectory_controller/useful_data_to_analyze/nullspace_stiffness')
    nullspace_stiffness=nullspace_stiffness[0]
    ready=True
    for i in range(1, len(sys.argv)-1):
        if abs(1-cartesian_stiffness[i-1]/float(sys.argv[i])) > 0.05 and abs(nullspace_stiffness-float(sys.argv[7])) > 0.1:
            ready = False
    if ready == True:
        exit("Stiffness ready")
    else:
        print 'Waiting for stiffness. Time left:', timeout-time.time()
