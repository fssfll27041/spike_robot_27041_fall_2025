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
    # gerald heavy lifting code:

    r.robot.straight(670)
    # should be 90
    r.robot.turn(70)
    r.robot.straight(390)
    # should be -110
    r.robot.turn(-90)
    r.ram.run_time(200,2000)
    # should be 130
    r.robot.straight(195)
   # r.ram.run_time(200,2000)
    r.ram.run_time(-200,2000)
   # r.robot.straight(-320)
    r.robot.drive(-500,10)
    wait(2000)
    r.robot.stop()





    

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
