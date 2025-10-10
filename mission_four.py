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
    r.ram.run_time(100,1000)
    r.robot.straight(-70)
    r.robot.turn(-90)
    r.robot.straight(100)
    r.robot.turn(70)
    r.robot.straight(200)

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
