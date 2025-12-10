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
    
    # Revised millstone mission from qualifier
    # r.robot.straight(95)
    # r.robot.turn(45)
    # r.robot.straight(220)
    # r.robot.turn(-45)
    # r.robot.straight(570)
    # r.robot.turn(-45)
    # r.ram.run_time(200,2000)
    # r.robot.straight(200)
    # r.ram.run_time(-200,2000)
    # r.robot.straight(-200)






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

    # Return to home, arcing a bit to avoid the wall
    # r.robot.drive(-500,10)
    # wait(2000)
    # r.robot.stop()

    # Drive forward past the silo and push the ore out of bounds
    # r.robot.straight(695)
    # r.robot.turn(70)
    # r.robot.straight(350)
    # r.robot.drive(300,-110)
    # wait(870)
    # r.robot.stop()

    # Drive to millstone and pick it up using the amazing comb
    # r.robot.turn(-75)
    # r.ram.run_time(200,2000)
    # r.robot.straight(40)
    # r.robot.turn(-37)
    # r.robot.straight(20)
    # r.ram.run_time(-200,2000)

    # Return to home, arcing a bit to avoid the wall
    # r.robot.drive(-500,10)
    # wait(2000)
    # r.robot.stop()

if __name__ == "__main__":
    from main import main
    main()