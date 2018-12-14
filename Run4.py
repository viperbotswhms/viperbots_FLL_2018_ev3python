from time import sleep

#Copyright of Viperbots FLL team  http://sites.google.com/view/viperbotsofficial/
#Can be freely used by any developors as long as you inform us on ViperbotsWHMS@gmail.com

#Run4.py - Steps for Run 4 execution corresponding to pseuedo code. Check run diagram in website to match

import Robot
import Constants
import ResetRobot

def run4_part1():
        """
        1. Move forward to after extraction.
        2. Turn 90 degrees left. And go forward till near mid of crater crossing
        3. Turn right 100 degrees to align to edge of line for throwing meteoroid
        4. Rotate gear on right to turn pole 4C in throwing action pushing meteoroid to its position. Pull back motor (M14-2 – 8/12 points)
        5. Turn slight left to be aligned to food chamber. Go forward till in front of food chamber.
        6. Rotate left motor to slide to drop water core sample on food growth chamber (M05-4 – 8 points)

        """

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
    """
        7. Go forward till first position of satellite X. 
        8. Turn left to align to corner of lander mission. 
        9. Push box attachment 4B to lander area
        10. Pull back leaving attachment 4B containing, lander and Extracted brick in lander area (M03-2 – 4, M05-3 -2, M15-2/3 – 6 points) 
        11. Turn 45 degrees left aligning to other teams solar panel
        12. Rotate right motor to align hooking portion of 4C at height of other team’s solar panel
        13. Move forward to edge of table pushing solar panel out using attachment Q (M02-1/2 – 22 points)
        14. Turn towards aerobics mission ensuring 4C is over its bars and satellites on 4E are over outer orbit (M12-2/3 – 8+8 points)
        15. Keep hitting aerobics handle with attachment 4C (M08-1/2/3 – 22 points)

    """
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
    """
    Execute Run 4 missions in order
    """    
    ResetRobot.reset_wheel_motors()
    ResetRobot.reset_attachment_motors()

    run4_part1()



def execute_run4():
    """
    Main execute function for Run 2
    """
    Robot.sound.speak('Executing Run4')
    run4()