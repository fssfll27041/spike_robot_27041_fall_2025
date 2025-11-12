################################################################################
# mission_two.py
#
# Description:
# [Describe What your mission does here]
#
# Author(s): Josie  Evelyn
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
#position edge of front pushy thingy should be line up with first yellow line in unearthed symbol (the one with gaps in it)
def mission_two(r):
    TIRE_DIAMETER = 88  # mm
    AXLE_TRACK = 100  # distance between the wheels, mm
    STRAIGHT_SPEED = 400  # mm/sec
    STRAIGHT_ACCEL = 300  # mm/sec^2
    TURN_RATE = 300  # deg/sec
    TURN_ACCEL = 200  # deg/sec^2


    print("Running Mission 2")
    r.robot.straight(620)
    r.robot.turn(30)
    r.robot.straight(130)
    r.robot.turn(-70)
    r.robot.straight(155)
    r.robot.turn(-45)
    #r.robot.straight(170)
   # r.robot.turn(-45)
    #r.robot.turn(170#)
    r.robot.straight(80)
    r.robot.straight(-15)
    r.robot.turn(60)
    #r.robot.straight(-340)
   # r.robot.turn(-35)
  #  r.robot.straight(-350)
         #bee kind
 
    # enable turbo mode
    r.robot.settings(1000, 1000, TURN_RATE, TURN_ACCEL)
    # race backwards to home
    r.robot.drive(-1000, -30)
    wait(2500)


    # disable turbo mode before other missions
    r.robot.stop()
    r.robot.settings(STRAIGHT_SPEED, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()