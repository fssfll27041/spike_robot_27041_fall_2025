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
    r.robot.straight(580)
    r.robot.turn(45)
    r.robot.straight(400)

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
    """
    r.robot.straight(-300)
    r.robot.turn(-45)
    r.robot.drive(1000,41)
    wait(500)
    r.robot.drive(1000,-20)
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