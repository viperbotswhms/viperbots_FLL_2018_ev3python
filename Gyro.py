import Robot
import Constants
import CalibrateRobot
import ResetRobot

from time import sleep


#Copyright of Viperbots FLL team  http://sites.google.com/view/viperbotsofficial/
#Can be freely used by any developors as long as you inform us on ViperbotsWHMS@gmail.com

#Gyro.py - Gyro execution functions

from ev3dev2.motor import SpeedNativeUnits

#Initiatilization of PID variables
integral = 0
derivative = 0
last_error = 0

#PID Contstants
KP_FACTOR = 0.3        #Proportional Constant
KI_FACTOR = 0.001      #Integral Constant
KD_FACTOR = 0.2        #Detivative Constant

#Gyro based rotation functions
def gyro_speed_direction_control_fwd(delta_angle,speed,rotations):
        """
        Function for  moving consistently at an angle specified by delta angle and speed.
        """

        Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
        current_zero_angle=Robot.robot_gyro.angle
        sleep(0.2)

        desired_angle=current_zero_angle+delta_angle

        left_speed=desired_angle+speed
        right_speed=desired_angle-speed

        #move tank
        Robot.tank_pair.on_for_rotations(left_speed,right_speed,rotations)

#PID functions
def check_steer_limit(steering):
        """
        Function to verify that the correction steering calculated by PID falls within range
        """
        if steering > Constants.max_steering:
                steering = Constants.max_steering
        elif steering < Constants.min_steering:
                steering = Constants.min_steering
        return steering

def PID_reset():
        '''
        Function to reset the PID variables
        '''
        integral = 0
        derivative = 0
        last_error = 0

def PID_correction(desired_value,current_value):
        '''
        Function to calculate the steering value for each iteration of the PID correction
        '''
        target_value = desired_value
        current_value = current_value
        kp = KP_FACTOR
        ki = KI_FACTOR
        kd = KD_FACTOR

        #Proportional Correction
        error = target_value - current_value
        P_correction = kp *error

        #Integral Correction
        integral= integral + error
        I_correction = ki * integral

        #Derivative Correction
        derivative = error - last_error
        D_correction = kd *derivative

        #Total correction to be applied
        final_correction = P_correction + I_correction + D_correction

        last_error = error

        steering = check_steer_limit(final_correction)
        return steering

#proportional correction
def proportional_correction(desired_value,current_value):
        """
        Function for calcutatng the proportional correction for any movement
        """
        target_value = desired_value
        current_value = current_value
        kp = KP_FACTOR

        error = target_value - current_value
        correction = kp *error
        return correction

def gyro_mov_on_for_rotations(speed,rotations,current_zero_angle):
        """
        Function for applying proportional correction where robot movement is sampled on intervals of rotations specific for straight motion
        """

        Robot.robot_gyro.mode = Constants.MODE_GYRO_ANG
        measured_angle=Robot.robot_gyro.angle 
        sleep(0.2)   
        rot=1
        while not rot>=rotations:   
                kp = KP_FACTOR*(current_zero_angle-measured_angle)
                steering=kp
                Robot.steer_pair.on_for_rotations(steering,speed,rot)
        rot=rot+0.5

#using pid correction for moving straight until whie line detected on left
def gyro_mov_straight_until_white_left(speed):
        """
        Function for PID corrected movement until white line is detected by the left color sensor
        """

        #Robot.sound.speak('applying PID')

        target_value = 0      
        kp = KP_FACTOR
        ki = KI_FACTOR
        kd = KD_FACTOR

        while not(Robot.bottom_cl_left.reflected_light_intensity>Constants.WHITE_LIGHT_INTENSITY):
                Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
                current_value=Robot.robot_gyro.angle
                sleep(0.2)
                #Proportional Correction
                error = target_value - current_value
                P_correction = kp *error
                #Integral Correction
                integral= integral + error
                I_correction = ki * integral
                #Derivative Correction
                derivative = error - last_error
                D_correction = kd *derivative

                #Total correction to be applied
                final_correction = P_correction + I_correction + D_correction

                last_error = error                
                steering = check_steer_limit(final_correction)
        
                Robot.steer_pair.on(steering,speed) 

def gyro_mov_straight_until_white_right(speed):
        """
        Function for PID corrected movement until white line is detected by the right color sensor
        """

        #Robot.sound.speak('applying PID')

        target_value = 0      
        kp = KP_FACTOR
        ki = KI_FACTOR
        kd = KD_FACTOR

        while not(Robot.bottom_cl_right.reflected_light_intensity>Constants.WHITE_LIGHT_INTENSITY):
                Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
                current_value=Robot.robot_gyro.angle
                sleep(0.2)
                #Proportional Correction
                error = target_value - current_value
                P_correction = kp *error
                #Integral Correction
                integral= integral + error
                I_correction = ki * integral
                #Derivative Correction
                derivative = error - last_error
                D_correction = kd *derivative

                #Total correction to be applied
                final_correction = P_correction + I_correction + D_correction

                last_error = error                
                steering = check_steer_limit(final_correction)
        
                Robot.steer_pair.on(steering,speed) 
        