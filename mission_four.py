################################################################################
# mission_four.py
#
# Description:
# Push bolders / Collect millistone
# 
# Authors: Eleanor Andreu Jack
# Date: 2025-11-22
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
    
    # Revised millstone mission
    r.robot.settings(700, 300, 300, 200)
    r.robot.straight(200)
    r.robot.drive(225,45)
    wait(1000)
    r.robot.drive(225,-45)
    wait(1250)
    r.robot.stop()
    r.robot.straight(300)
    r.robot.drive(225,-45)
    wait(1000)
    r.ram.run_time(200,2000)
    r.robot.straight(-200)

if __name__ == "__main__":
    from main import main
    main()