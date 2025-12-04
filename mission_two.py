################################################################################
# mission_two.py
#
# Description:
# Release the ore from the forge and the who lived here mission
#
# Author(s): Josie  Evelyn
# Date: 2025-10-01
# Version: 1.0
#
# Dependencies:
# - robot
# - pybricks.tools
#
################################################################################
from robot import robot
from pybricks.tools import wait, StopWatch
# position edge of front pushy thingy should be line up with first yellow line 
# in unearthed symbol (the one with gaps in it)
def mission_two(r):
    TIRE_DIAMETER = 88  # mm
    AXLE_TRACK = 100  # distance between the wheels, mm
    STRAIGHT_SPEED = 400  # mm/sec
    STRAIGHT_ACCEL = 300  # mm/sec^2
    TURN_RATE = 300  # deg/sec
    TURN_ACCEL = 200  # deg/sec^2

    print("Running Mission 2")
    # Driving to the forge
    r.robot.straight(620)
    r.robot.turn(30)
    r.robot.straight(133)

    # Hit the forge to get 30 points
    r.robot.turn(-73)
    r.robot.straight(130)

    # Driving to "who lived here" and flipping the table
    r.robot.drive(100,-45)
    wait(850)
    r.robot.stop()

    # backing up and heading home
    r.robot.straight(-15)
    r.robot.turn(60)
 
    # enable turbo mode
    r.robot.settings(700, 300, TURN_RATE, TURN_ACCEL)
    
    # race backwards to home
    r.robot.drive(-1000,-20)
    wait(1750)
    
    # disable turbo mode before other missions
    r.robot.stop()
    r.robot.settings(STRAIGHT_SPEED, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)
    
    # Home sweet home
if __name__ == "__main__":
    from main import main
    main()