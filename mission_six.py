################################################################################
# mission_six.py
#Josie and Evelyn 
# our mission does and s-turn up to the lifter then drives to the "what's for sale" and raises the roof.

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
    # Your code goes here...
#s-turn begins mission
    r.robot.settings(700, 300, 300, 200)
    r.robot.straight(677)
    r.robot.drive(1000,93)
    wait(970)
    #it drives up to minecart lifter and lifts, 30 points 
    r.robot.straight(175)
    r.ram.run_time(-200,1000)
    #it raises the roof, 20 points
    r.robot.straight(605)
    r.robot.turn(45)
    r.robot.straight(400)

    r.robot.straight(-200)
    r.robot.turn(-54)
    r.robot.drive(1000,30)
    wait(2000)
    r.robot.drive(1000,-17)
    wait(2000)
    r.robot.stop()    
    r.robot.settings(400, 300, 300, 200)
    # r.robot.straight(200)
    #r.robot.turn(30)
    #r.robot.straight(900)   

   

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()