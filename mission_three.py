################################################################################
# mission_three.py
#
# Description:
# [Describe What your mission does here]
#
# Author(s): [Gerald/Eleanor]
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

def mission_three(r):
    print("Running Mission 3: Gerald")
    # Your code goes here...
    # Sample Code: Test running the attachment motor until stalled
  #r.robot.straight(200)
   # r.robot.turn(-30)
    r.robot.straight(820)
    r.robot.straight(-150)
    r.robot.turn(-90)
    r.robot.straight(-40)
    r.robot.straight(50)
    r.ram.run_time(-200,2000)
    r.robot.turn(80)
    r.ram.run_time(180,2000)
    r.robot.straight(150)
    r.ram.run_time(-200,2000)
    r.robot.turn(-50)
    r.robot.straight(110)
    r.robot.straight(-150)
    r.robot.turn(60)
    r.robot.straight(-800)
   # r.robot.turn(60)
   # r.robot.turn(-60)
   # r.robot.turn(30)
   # r.robot.straight(-100)
   # r.robot.straight(-200)
   # r.robot.straight(120)
#r.ram.run_time(-200,2000)

if __name__ == "__main__":
    from main import main
    main()
