################################################################################
# mission_one.py
#
# Description:
# unearthed multi silo / mahket basket/five below/
#
# Author(s): Andreu, Jack
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

# TODO get theses from robot.py
TIRE_DIAMETER = 88  # mm
AXLE_TRACK = 100  # distance between the wheels, mm
STRAIGHT_SPEED = 400  # mm/sec
STRAIGHT_ACCEL = 300  # mm/sec^2
TURN_RATE = 300  # deg/sec
TURN_ACCEL = 200  # deg/sec^2

def mission_one(r):
    print("Running Mission 1")

    # ------------------------------------------------------
    # position wheel 6 units on jig before mission start
    # ------------------------------------------------------

    # move from home to silo
    r.robot.straight(405)     
    # chop the lever to eject food
    for i in range(4):
        r.ram.run_time(1300, 697)
        r.robot.turn(2)
        r.ram.run_time(-1300, 697)

    # start market stall mission
    # turn left and proceed 20-30 cm
    r.robot.turn(-52)
    r.robot.straight(253)

    # slight turn to the left then push boom foward
    r.robot.turn(-55)
    r.robot.straight(285)

    # Drive to the rear of tip the scales using arc turn
    r.robot.arc(250,120)
    r.robot.turn(60) 
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
