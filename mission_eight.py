################################################################################
# mission_eight.py
#
# Description:
# Maaket basket (Tip the scales)
#
# Authors: Jack, and Andreu 
# Date: 12/9/2025
# Version: 1.0
#
# Dependencies:
# - robot
# - pybricks.tools
#
################################################################################
from robot import robot
from pybricks.tools import wait, StopWatch

# TODO get theses from robot.py
TIRE_DIAMETER = 88  # mm
AXLE_TRACK = 100  # distance between the wheels, mm
STRAIGHT_SPEED = 400  # mm/sec
STRAIGHT_ACCEL = 300  # mm/sec^2
TURN_RATE = 300  # deg/sec
TURN_ACCEL = 200  # deg/sec^2

def mission_eight(r):
    print("Running Mission 8")

    #drive to wares
    r.robot.drive(275, -20 )
    wait(2000)
    r.robot.stop()
    #wack the boom
    r.ram.run_time(1170 / 2, 697 * 2)
    r.robot.straight(40)
    r.robot.turn(-50)
    r.ram.run_time(-1170 / 2, 697 * 2)
    r.robot.turn(-25)

    # Drive to the rear of tip the scales using arc turn
    r.robot.straight(300)
    r.robot.arc(250,120)
    r.robot.turn(45) 
    r.robot.straight(45)   
    
    # Wack raised basket
    r.ram.run_time(1300, 580)
    r.ram.run_time(-1300, 580)

    # Go back to home
    r.robot.turn(-50)

    # enable turbo mode
    r.robot.settings(1000, 1000, TURN_RATE, TURN_ACCEL)

    # race backwards to home
    r.robot.drive(-1000, 30)
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