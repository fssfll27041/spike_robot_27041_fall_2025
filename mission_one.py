################################################################################
# mission_one.py
#
# Description:
# unearthed multi mission
#
# Author(s): Andreu, Jack
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
    for i in range(4):
        r.ram.run_time(1300, 590)
        r.ram.run_time(-1300, 590)

    # start market stall mission

    # turn left and proceed 20-30 cm
    r.robot.turn(-55) 
    r.robot.straight(280)
   
    # slight turn to the left then push boom foward
    r.robot.turn(-55)
    r.robot.straight(200)

    # Drive to the rear of tip the scales 
    r.robot.straight(280)
    r.robot.turn(30)
    r.robot.straight(170)
    r.robot.turn(80)
    r.robot.straight(320)
    r.robot.turn(50)
    r.robot.straight(60)
    r.ram.run_time(1300, 590)
    r.ram.run_time(-1300, 590)

    # Go back to home
    r.robot.turn(-7)
    #remember to add turbo mode
    r.robot.straight(-1000)






################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()