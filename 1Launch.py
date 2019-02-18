#!/usr/bin/env python3

#Copyright of Viperbots FLL team  http://sites.google.com/view/viperbotsofficial/
#Can be freely used by any developors as long as you inform us on ViperbotsWHMS@gmail.com

#1Launch.py - this file is the main program for the Viperbots FLL Robot game execution

#Import Base functions
import Robot
import Constants
import CalibrateRobot
import Gyro

#Import actual execution runs. Each run is a set of missions.
import Run1
import Run2
import Run3

import TestBench

from time import sleep

def execute_run_bycode_bybutton(button_name):
    """
    Function to select which run to execute by pressing of different buttons on the EV3
    Input button name to the function
    """

    #Test bench invoked in center button
    if Robot.button.check_buttons(button_name) == Robot.button.enter:
        #Robot.sound.speak('center button pressed')
        if Constants.TEST_MODE:
            #Robot.sound.speak('Entering test mode')
            TestBench.test_run() 
    elif Robot.button.check_buttons(button_name) == Robot.button.left :
        #Robot.sound.speak('Left button pressed calling Run1')
        Run1.execute_run1()
    elif Robot.button.check_buttons(button_name) == Robot.button.right:
        #Robot.sound.speak('Right button pressed calling Run2')
        Run2.execute_run2()
    elif Robot.button.check_buttons(button_name) == Robot.button.up:
        #Robot.sound.speak('Up button pressed calling Run3')
        Run3.execute_run3()


def execute_run_bycode():
    """
    Function to select which run to execute by the color code of the top pointing color sensor on Robot
    Each attachment is coded with a colored brick placed right above the color sensor
    """

    if(Robot.top_cl.color_name == Constants.RUN1_CODE):
        Run1.execute_run1()
    elif (Robot.top_cl.color_name == Constants.RUN2_CODE):
        Run2.execute_run2()
    elif (Robot.top_cl.color_name == Constants.RUN3_CODE):
        Run3.execute_run3()
    else:
        Robot.sound.speak('I NEED MY ARMS')
        
#Main program starts here
#Announce robot ready to start
#Robot.sound.speak('Robot Ready')

#Main loop to run forever till escape button is pressed and program is ended

while True:
    while not Robot.button.any():
        Robot.sound.beep()
    else:
        #Selection code
        if Robot.button.any:
            sleep(0.3)
            #Selection of run by color coded attachment
            if Constants.ATTACHMENT_CODE:
                execute_run_bycode()
                #Robot.sound.speak('Run completed')
            else:
                #Selection of run by pressing different buttons on eV3 
                execute_run_bycode_bybutton(Robot.button.buttons_pressed)
                #Robot.sound.speak('Run completed')
else:
    pass

#End Main program