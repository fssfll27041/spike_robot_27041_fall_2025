################################################################################
# mission_five.py
#
# Description:
# [Describe What your mission does here]
#
# Author(s): Josie Evelyn
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

def mission_five(r):
    print("Running Mission 5")
    # Your code goes here...
    r.robot.straight(775)
    r.robot.turn(90)
    r.robot.straight(400)
    r.robot.turn(-100)
    r.ram.run_time(1000,500)
    r.robot.straight(200)
    
    





################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()