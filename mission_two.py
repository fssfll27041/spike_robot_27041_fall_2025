################################################################################
# mission_two.py
#
# Description:
# [Describe What your mission does here]
#
# Author(s): Josie  Evelyn
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

def mission_two(r):
    print("Running Mission 2")
    r.robot.straight(620)
    r.robot.turn(30)
    r.robot.straight(135)
    r.robot.turn(-72)
    r.robot.straight(155)
    r.robot.turn(-45)
    #r.robot.straight(170)
   # r.robot.turn(-45)
    #r.robot.turn(170#)
    r.robot.straight(80)
    r.robot.straight(-80)
    r.robot.turn(60)
    r.robot.straight(-340)
    r.robot.turn(-35)
    r.robot.straight(-340)



################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()