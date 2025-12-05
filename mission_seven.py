################################################################################
# mission_seven.py
#
# Description:
# Completes the salvage operation mission
#
# Author(s): Eleanor
# Date: 2025-11-28
# Version: 1.0
#
# Dependencies:
# - robot
# - pybricks.tools
#
################################################################################
from robot import robot
from pybricks.tools import wait, StopWatch

def mission_seven(r):
    print("Running Mission 7")

    # drives to the salvage operation mission and knocks the sand off
    r.robot.straight(500)
    r.ram.run_time(100,750)
    r.robot.straight(-70)

    # turns to go push the ship
    r.robot.turn(-70)
    r.robot.straight(100)
    r.robot.turn(70)
    r.ram.run_time(-200,500)
    r.robot.straight(450)

    # goes back to home
    r.robot.drive(-1000,-15)
    wait(2000)
    r.robot.stop()

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
