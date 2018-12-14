import Robot
import Constants
import CalibrateRobot
import ResetRobot

from time import sleep

#Copyright of Viperbots FLL team  http://sites.google.com/view/viperbotsofficial/
#Can be freely used by any developors as long as you inform us on ViperbotsWHMS@gmail.com

#Gyro.py - Gyro execution functions

from ev3dev2.motor import SpeedNativeUnits

def check_steer_limit(steering):
        """
        Function to verify that the correction steering calculated by PID falls within range
        """
        if steering > Constants.max_steering:
                steering = Constants.max_steering
        elif steering < Constants.min_steering:
                steering = Constants.min_steering
        return steering

#move without drift for a certain rotations
#used in Run2 tube module
def gyro_mov_on_for_rotations(speed,rotations,current_zero_angle):
        """
        Function for applying proportional correction
        where robot movement is sampled on intervals of rotations
        specific for tube module mission
        """
        Robot.robot_gyro.mode = Constants.MODE_GYRO_ANG
        measured_angle=Robot.robot_gyro.angle    
        sleep(0.2)
        rot=1
        while not rot>=rotations:   
                gain=-6
                kp=gain*(current_zero_angle-measured_angle)
                steering=kp
                Robot.steer_pair.on_for_rotations(steering,speed,rot)
                rot=rot+0.5

#consistant speed and direction
def gyro_speed_direction_control_fwd(delta_angle,speed,rotations):
        """
        Function for  moving consistently at an angle specified by delta angle and speed.
        """
        Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
        current_zero_angle=Robot.robot_gyro.angle
        sleep(0.2)

        #desired angle = current angle + delta angle
        desired_angle=current_zero_angle+delta_angle

        left_speed=desired_angle+speed
        right_speed=desired_angle-speed

        #move tank
        Robot.tank_pair.on_for_rotations(left_speed,right_speed,rotations)


#proportional correction
def proportional_correction(desired_value,current_value,kp_factor):
        """
        Function for calcutatng the proportional correction for any movement
        """
        target_value = desired_value
        current_value = current_value
        kp = kp_factor

        error = target_value - current_value
        correction = kp *error
        return correction
        

def PID_correction(desired_value,current_value,kp_factor,ki_factor,kd_factor):
        """
        Function for calculating the PID correction to be applied for steering value
        """
        target_value = desired_value
        current_value = current_value
        kp = kp_factor
        ki = ki_factor
        kd=kd_factor

        integral=0
        derivative=0
        last_error = 0

        error = target_value - current_value

        P_correction = kp *error
        
        integral=integral+error

        I_correction = ki * integral


        derivative = error - last_error

        D_correction = kd *error

        final_correction = P_correction + I_correction + D_correction

        last_error = error

        steering = check_steer_limit(final_correction)
        return steering
        

#using pid correction for moving straight until whie line detected on left
def gyro_mov_straight_until_white_left(speed):
        """
        Function for PID corrected movement until white line is detected by the left color sensor
        """
        
        #Robot.sound.speak('applying PID')

        target_value = 0      
        kp = 0.3
        ki = 0.001
        kd=0.2

        integral=0
        derivative=0
        last_error = 0

        while not(Robot.bottom_cl_left.reflected_light_intensity>Constants.WHITE_LIGHT_INTENSITY):
                Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
                current_value=Robot.robot_gyro.angle
                error = target_value - current_value

                P_correction = kp *error
        
                integral=integral+error

                I_correction = ki * integral


                derivative = error - last_error

                D_correction = kd *error

                final_correction = P_correction + I_correction + D_correction

                last_error = error

                steering = check_steer_limit(final_correction)

        
                Robot.steer_pair.on(steering,speed) 

#using pid correction for moving straight until whie line detected on right
def gyro_mov_straight_until_white_right(speed):
        """
        Function for PID corrected movement until white line is detected by the right color sensor
        """
        
        #Robot.sound.speak('applying PID')

        target_value = 0      
        kp = 0.3
        ki = 0.001
        kd=0.2

        integral=0
        derivative=0
        last_error = 0

        while not(Robot.bottom_cl_right.reflected_light_intensity>Constants.WHITE_LIGHT_INTENSITY):
                Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
                current_value=Robot.robot_gyro.angle
                error = target_value - current_value

                P_correction = kp *error
        
                integral=integral+error

                I_correction = ki * integral


                derivative = error - last_error

                D_correction = kd *error

                final_correction = P_correction + I_correction + D_correction

                last_error = error

                steering = check_steer_limit(final_correction)

        
                Robot.steer_pair.on(steering,speed) 
        

def gyro_mov_straight_until_white_left_angled(speed):
        """
        Function for PID corrected movement until white line is detected by the left color sensor
        Robot moving on a striaght path
        """
        
        #Robot.sound.speak('applying PID')
        Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
        target_value = Robot.robot_gyro.angle   
        sleep(0.2)   
        kp = 0.3
        ki = 0.001
        kd=0.2

        integral=0
        derivative=0
        last_error = 0

        while not(Robot.bottom_cl_left.reflected_light_intensity>Constants.WHITE_LIGHT_INTENSITY):
                Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
                current_value=Robot.robot_gyro.angle
                error = target_value - current_value

                P_correction = kp *error
        
                integral=integral+error

                I_correction = ki * integral


                derivative = error - last_error

                D_correction = kd *error

                final_correction = P_correction + I_correction + D_correction

                last_error = error

                steering = check_steer_limit(final_correction)

        
                Robot.steer_pair.on(steering,speed) 

def gyro_mov_straight_until_white_right_angled(speed):
        """
        Function for PID corrected movement until white line is detected by the right color sensor
        Robot moving on a striaght path
        """
        
        #Robot.sound.speak('applying PID')
        Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
        target_value = Robot.robot_gyro.angle   
        sleep(0.2)   
        kp = 0.3
        ki = 0.001
        kd=0.2

        integral=0
        derivative=0
        last_error = 0

        while not(Robot.bottom_cl_right.reflected_light_intensity>Constants.WHITE_LIGHT_INTENSITY):
                Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
                current_value=Robot.robot_gyro.angle
                error = target_value - current_value

                P_correction = kp *error
        
                integral=integral+error

                I_correction = ki * integral


                derivative = error - last_error

                D_correction = kd *error

                final_correction = P_correction + I_correction + D_correction

                last_error = error

                steering = check_steer_limit(final_correction)

        
                Robot.steer_pair.on(steering,speed) 

def gyro_mov_on_for_rotation_PCorrection(speed,rotations,kp):
        """
        Function for PID corrected movement using proportional correction only
        Robot moving on a striaght path
        """   
        #Robot.sound.speak('applying PID')
        Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
        target_value = 0    
        kp = kp
        ki = 0
        kd=0

        integral=0
        derivative=0
        last_error = 0

        #while not(Robot.bottom_cl_right.reflected_light_intensity>Constants.WHITE_LIGHT_INTENSITY):
        Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
        current_value=Robot.robot_gyro.angle
        error = target_value - current_value

        P_correction = kp *error
        
        integral=integral+error

        I_correction = ki * integral


        derivative = error - last_error

        D_correction = kd *error

        final_correction = P_correction + I_correction + D_correction

        last_error = error

        steering = check_steer_limit(final_correction)

        
        Robot.steer_pair.on_for_rotations(steering,speed,rotations) 

def gyro_mov_on_for_rotation_PID(speed,rotations,kp,ki,kd):
        """
        Function for PID corrected movement using P,I and D correction
        Robot moving on a striaght path
        """
        
        #Robot.sound.speak('applying PID')
        Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
        target_value = 0    
        kp = kp
        ki = ki
        kd=kd

        integral=0
        derivative=0
        last_error = 0

        #while not(Robot.bottom_cl_right.reflected_light_intensity>Constants.WHITE_LIGHT_INTENSITY):
        Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
        current_value=Robot.robot_gyro.angle
        error = target_value - current_value

        P_correction = kp *error
        
        integral=integral+error

        I_correction = ki * integral


        derivative = error - last_error

        D_correction = kd *error

        final_correction = P_correction + I_correction + D_correction

        last_error = error

        steering = check_steer_limit(final_correction)

        
        Robot.steer_pair.on_for_rotations(steering,speed,rotations) 

def gyro_mov_on_for_rotation_PID_seconds(speed,seconds,kp,ki,kd):
        """
        Function for PID corrected movement for seconds (time limited)       
        """
        
        #Robot.sound.speak('applying PID')
        Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
        target_value = 0    
        kp = kp
        ki = ki
        kd=kd

        integral=0
        derivative=0
        last_error = 0

        time_counter=0

        #while not(Robot.bottom_cl_right.reflected_light_intensity>Constants.WHITE_LIGHT_INTENSITY):
        Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
        current_value=Robot.robot_gyro.angle
        error = target_value - current_value

        P_correction = kp *error
        
        integral=integral+error

        I_correction = ki * integral


        derivative = error - last_error

        D_correction = kd *error

        final_correction = P_correction + I_correction + D_correction

        last_error = error

        steering = check_steer_limit(final_correction)

        while time_counter!=seconds:
                Robot.steer_pair.on_for_seconds(steering,speed,1)
                time_counter = time_counter+1
        #Robot.steer_pair.on_for_rotations(steering,speed,rotations) 

def mov_on_angle_straight(delta_angle,speed,rotations,kp,ki,kd):
        """
        Function for PID corrected movement at an angle limited by rotations   
        """
                #Robot.sound.speak('applying PID')
        Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
        target_value = Robot.robot_gyro.angle + delta_angle
        sleep(0.2)
        kp = kp
        ki = ki
        kd=kd

        integral=0
        derivative=0
        last_error = 0

        #while not(Robot.bottom_cl_right.reflected_light_intensity>Constants.WHITE_LIGHT_INTENSITY):
        Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
        current_value=Robot.robot_gyro.angle
        error = target_value - current_value

        P_correction = kp *error
        
        integral=integral+error

        I_correction = ki * integral


        derivative = error - last_error

        D_correction = kd *error

        final_correction = P_correction + I_correction + D_correction

        last_error = error

        steering = check_steer_limit(final_correction)

        
        Robot.steer_pair.on_for_rotations(steering,speed,rotations) 

#All functions below are for the unit testing off the gyro file accessed by test bench

def test_PID():
        Robot.sound.speak('Testing PID')

        target_value = 0      
        kp = 0.3
        ki = 0.001
        kd=0.2

        integral=0
        derivative=0
        last_error = 0

        rotations = 4
        tacho_counts = 10

        while not target_value:
                Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
                current_value=Robot.robot_gyro.angle
                error = target_value - current_value

                P_correction = kp *error
        
                integral=integral+error

                I_correction = ki * integral


                derivative = error - last_error

                D_correction = kd *error

                final_correction = P_correction + I_correction + D_correction

                last_error = error

                steering = check_steer_limit(final_correction)

                #Robot.steer_pair.on(steering,-75)
               
                Robot.steer_pair.on_for_rotations(steering,-100,0.1)

def test_PID_rotations(speed,rotations):
        Robot.sound.speak('Testing PID')

        target_value = 0      
        kp = 0.3
        ki = 0.001
        kd=0.2

        integral=0
        derivative=0
        last_error = 0

        rotations = 4
        tacho_counts = 10

        while not target_value:
                Robot.robot_gyro.mode=Constants.MODE_GYRO_ANG
                current_value=Robot.robot_gyro.angle
                error = target_value - current_value

                P_correction = kp *error
        
                integral=integral+error

                I_correction = ki * integral


                derivative = error - last_error

                D_correction = kd *error

                final_correction = P_correction + I_correction + D_correction

                last_error = error

                steering = check_steer_limit(final_correction)

                #Robot.steer_pair.on(steering,-75)
               
                Robot.steer_pair.on_for_rotations(steering,speed,rotations)




