################################################################################
# mission_five.py
#
# Description:
# [Describe What your mission does here]
#
# Author(s): Josie Evelyn
# Date: [YYYY-MM-DD]
# Version: 1.0
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
    r.robot.straight(390)
    r.robot.turn(-95)
    r.ram.run_time(1000,500)
    r.robot.straight(52)
    r.robot.drive(10, 0)
    r.ram.run_time(-100,1000)
    wait(750)
    r.robot.stop()
    r.robot.straight(75)
    r.robot.turn(75)
    r.robot.straight(700)
    r.robot.turn(40)
    r.robot.straight(350)
    r.robot.straight(-175)
    r.robot.turn(-30)
    r.robot.straight(200)
    r.robot.turn(30)
    r.robot.straight(900)

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()