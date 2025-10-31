################################################################################
# mission_seven.py
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

def mission_seven(r):
    print("Running Mission 7")
    # Your code goes here...

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()

    r.robot.straight(150)
    r.robot.turn(-90)
    r.robot.straight(340)
    r.robot.turn(-90)
    r.robot.straight(60)
    r.ram.run_time(-200,1000)
    r.robot.straight(-70)
    