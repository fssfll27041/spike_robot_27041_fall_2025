################################################################################
# mission_four.py
#
# Description:
# Push bolders/ Collect millistone
# 
# Authors: Eleanor Andreu Jack
# Date: 2025-11-22
# Version: 1.0
#
# Dependencies:
# - robot
# - pybricks.tools
#
################################################################################
from robot import robot
from pybricks.tools import wait, StopWatch

def mission_four(r):
    print("Running Mission 4")
 
    # gerald heavy lifting code:

    # Drive forward past the silo and push the ore out of bounds
    r.robot.straight(670)
    r.robot.turn(70)
    r.robot.straight(390)

    # Drive to millstone and pick it up using the amazing comb
    r.robot.turn(-95)
    r.ram.run_time(200,2000)
    r.robot.straight(195)
    r.ram.run_time(-200,2000)

    # Return to home, arcing a bit to avoid the wall
    r.robot.drive(-500,10)
    wait(2000)
    r.robot.stop()

if __name__ == "__main__":
    from main import main
    main()
