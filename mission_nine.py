################################################################################
# mission_nine.py
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

def mission_nine(r):
    print("Running Mission 9")
    # Your code goes here
    r.robot.straight(391)
    r.robot.straight(-391)

#position front third line lined up with front pushy thingy (remember that it is the black line underneath the red line) 




    #####
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()