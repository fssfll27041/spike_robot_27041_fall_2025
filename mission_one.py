################################################################################
# mission_one.py
#
# Description:
# [Describe What your mission does here]
#
# Author(s): [Your Name(s)]
# Date: [YYYY-MM-DD]
# Version: 1.0
#
# Dependencies:
# - robot
# - pybricks.tools
#
################################################################################
from robot import robot
from pybricks.tools import wait, StopWatch

def mission_one(r):
    print("Running Mission 1")
    # Your code goes here...
    # Sample Code: Run attachment motors and drive motors
    # r.lam.run_time(1000,1000)
    # r.lam.run_time(-1000,1000)
    # r.ldm.run_time(1000,1000)
    # r.ldm.run_time(-1000,1000)
    # r.rdm.run_time(400,1000)
    # r.rdm.run_time(-400,1000)
    
    # position wheel 6 units on jig
    # move from home  to silo
    r.robot.straight(425)     
    # chop the lever
    for i in range(7):
        r.ram.run_time(1300, 700)
        r.ram.run_time(-1300, 700)

    # start market stall mission

    #turn left and proceed 20-30 cm
    r.robot.turn(-65) 
    r.robot.straight(250)

    # slight turn to the left then push boom foward
    
    

#
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()