################################################################################
# mission_four.py
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

def mission_four(r):
    print("Running Mission 4")
    # Your code goes here...
    # Sample code:

    r.robot.straight(500)
    r.ram.run_time(100,750)
    r.robot.straight(-70)
    r.robot.turn(-70)
    r.robot.straight(100)
    r.robot.turn(70)
    r.ram.run_time(-200,500)
    r.robot.straight(450)
    #r.robot.straight(-600)
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
