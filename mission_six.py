################################################################################
# mission_six.py
# Authors: Josie and Evelyn 
# Date: 2025-10-09
#
# Our mission does and s-turn up to the lifter then drives to the 
#  "what's for sale" and raises the roof.
# Version: 1.0
#
# Dependencies:
# - robot
# - pybricks.tools
################################################################################
from robot import robot
from pybricks.tools import wait, StopWatch

def mission_six(r):
    print("Running Mission 6")

    # Drive forward, and gracefully s-turn to the mineshaft
    r.robot.settings(700, 300, 300, 200)
    r.robot.straight(687)
    r.robot.drive(1000,93)
    wait(970)

    # Next, drives up to minecart lifter and lifts, 30 points 
    r.robot.straight(175)
    r.ram.run_time(-200,1000)
    
    # Drive over to the market stall
    r.robot.straight(590)
    r.robot.turn(45)

    # Raises the market stall roof, 20 points
    r.robot.straight(400)
    r.robot.straight(-200)
    r.robot.turn(-55)

    # Do a fast S-turn all the way back to home 
    r.robot.drive(1000,25)
    wait(2300)
    r.robot.drive(1000,-20)
    wait(1000)
    r.robot.stop()    
    r.robot.settings(400, 300, 300, 200)

if __name__ == "__main__":
    from main import main
    main()