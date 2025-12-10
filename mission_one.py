################################################################################
# mission_one.py
#
# Description:
# unearthed multi silo / mahket basket/five below/
#
# Authors: Andreu, Jack
# Date: 2025-10-01
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

    # ------------------------------------------------------
    # position wheel 6 units on jig before mission start
    # ------------------------------------------------------

    # move from home to silo
    r.robot.straight(410)     
    # chop the lever to eject food
    for i in range(4):
        r.ram.run_time(1170, 697)
        r.robot.turn(3)
        r.ram.run_time(-1170, 697)

    # Go back to home
    r.robot.straight(-420)
    r.robot.straight(-30)

    
    
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()