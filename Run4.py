import Robot
import Constants
import ResetRobot

from time import sleep

def run4_part1():
        #Go Forward

#    Robot.steer_pair.on_for_rotations(0, -30, 2.4)
#    Robot.tank_pair.off()

    #Turn 90* Left

#    Robot.tank_pair.on_for_rotations(-40,-20,0.8)
#    Robot.tank_pair.off()
#    Robot.steer_pair.on_for_rotations(0, -15,1.7)
#    Robot.tank_pair.off()



    #Turn 90* Right

 
#    Robot.tank_pair.on_for_rotations(-20,-40,0.9)
#    Robot.tank_pair.off()

    # Pause 
    Robot.attachment_right.on_for_rotations(70,0.2)
    Robot.attachment_right.off()

def run4_part2():
    
    #Pause

    
    #Robot.attachment_right(-15,3)
    #Robot.attachment_right.off()

    #Continue

    Robot.steer_pair.on_for_rotations(0,-15,2)

    #Pause

    Robot.steer_pair.off()
    Robot.attachment_left(15,3)

    #Continue

    Robot.steer_pair.on_for_rotations(0,-50,2)

    #Turn left

    Robot.right_wheel.on_for_rotations(-30, 3)
    Robot.steer_pair.on_for_rotations(0, -50, 2)

    #Backwards

    Robot.steer_pair.on_for_rotations(30, 3)

    #Turn Left

    Robot.right_wheel.on_for_rotations(-30, 3)
    Robot.steer_pair.on_for_rotations(0, -50, 2)
    
    #Pause
    Robot.steer_pair.off()
    Robot.attachment_right(50,3)
    Robot.attachment_right(-50,3)

    #Turn left
    Robot.right_wheel.on_for_rotations(-30, 3)
    Robot.steer_pair.on_for_rotations(0, -50, 2)
    
    #Pause
    Robot.steer_pair.off()
    hitontop = 0
    while hitontop < 60:
        #Robot.attachment_right(50,3)        
        hitontop = hitontop = 1

#Defining Run

def run4():

    ResetRobot.reset_wheel_motors()
    ResetRobot.reset_attachment_motors()

    run4_part1()



def execute_run4():
    Robot.sound.speak('Executing Run4')
    run4()