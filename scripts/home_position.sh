#!/bin/bash

echo "Returning to the \"home\" position";
./change_goal.sh -0.5 -0.5 1 1 0 0 0 & ./change_stiffness.sh 50 50 50 30 30 30 20
sleep 7




