#!/bin/bash

echo "Returning to the \"home\" position";
./change_goal.sh -0.5 -0.5 1 1 0 0 0 & ./change_stiffness.sh 50 50 50 30 30 30 20

python python_scripts/wait_for_stiffness.py 50 50 50 30 30 30 20

./change_stiffness.sh 200 200 200 100 100 100 0


python python_scripts/wait_for_stiffness.py 200 200 200 100 100 100 0

