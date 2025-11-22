################################################################################
# mission_six.py
#
# Description:
# [Describe What your mission does here]
#
# Author(s): Josie Evelyn
# Date: [2025-11-8]
# Version: 1.0
#
# Dependencies:
# - robot
# - pybricks.tools
#
################################################################################
from robot import robot
from pybricks.tools import wait, StopWatch

def mission_six(r):
    print("Running Mission 6")
    # Your code goes here...

    r.robot.settings(700, 300, 300, 200)
    r.robot.straight(700)
    r.robot.drive(1000, 90)
    wait(900) 
    r.robot.straight(200)
    r.robot.settings(400, 300, 300, 200)

    #r.robot.turn(90)
    """#r.robot.straight(390)
    #r.robot.turn(-95)
    #r.ram.run_time(1000,500)
    #r.robot.straight(52)
    r.robot.drive(30, 0)
    r.ram.run_time(-300,1000)
    wait(500)
    r.robot.stop()
    r.robot.straight(75)
    r.robot.turn(75)
    r.robot.settings(600, 300, 300, 200)
    r.robot.straight(655)
    r.robot.turn(40)
    r.robot.straight(350)
    r.robot.straight(-100)
    r.robot.turn(-30)
    r.robot.drive(1000,20)
    wait(1000)
    r.robot.drive(1000,-20)
    wait(2000)
    r.robot.stop()    
    r.robot.settings(400, 300, 300, 200)
    # r.robot.straight(200)
    #r.robot.turn(30)
    #r.robot.straight(900)
    """
   
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()