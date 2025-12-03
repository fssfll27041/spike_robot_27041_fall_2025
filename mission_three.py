################################################################################
# mission_three.py
#
# Description:
# [Describe What your mission does here]
#
# Author: Eleanor
# Date: 2025-10-1
# Version: 1.0
#
# Dependencies:
# - robot
# - pybricks.tools
#
################################################################################

from robot import robot
from pybricks.tools import wait, StopWatch

def mission_three(r):
    print("Running Mission 3: Gerald")


    # Sets the speed for the mission
    r.robot.settings(600, 300, 300, 200)

    # The robot goes straight to knock the soil deposit, 
    # then goes back a bit to knock the other side
    r.robot.straight(785)
    r.robot.straight(-145)

    # Turns to go lift up the airbrush with the amazing comb attachment
    r.robot.turn(-90)
    r.robot.straight(-80)
    r.robot.straight(90)
    r.ram.run_time(-200,2000)

    # Turns to go to the map reveal mission
    r.robot.straight(-30)
    r.robot.turn(75)
    r.ram.run_time(180,2000)

    # Goes to lift up the topsoil
    r.robot.straight(150)
    r.ram.run_time(-200,2000)

    # Turns to push the topsoil section
    r.robot.turn(-50)
    r.robot.straight(90)
    r.robot.straight(-90)
    r.robot.turn(15)
    r.robot.straight(80)

    # Goes back home by arcing to go faster
    r.robot.drive(-1000,30)
    wait(3000)
    r.robot.stop()
    r.robot.settings(400, 300, 300, 200)

if __name__ == "__main__":
    from main import main
    main()
