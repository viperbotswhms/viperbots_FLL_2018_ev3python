ON=True
OFF=False

#Copyright of Viperbots FLL team  http://sites.google.com/view/viperbotsofficial/
#Can be freely used by any developors as long as you inform us on ViperbotsWHMS@gmail.com

#Constants.py - File defining all constants to be used by different Sensors and motors 

LEFT='LEFT'
RIGHT='RIGHT'

#Bypass constant for running with attachments or not, for testing
ATTACHMENT_CODE=ON

#Bypass constant for running with or without sensors, for testing
SENSOR=ON

#Constant for debug on or off
DEBUG=True

#Color sensor caliberation to the game table on white
WHITE_LIGHT_INTENSITY=90
BLACK_LIGHT_INTENSITY=10

#Color constants used by color sensor
COLOR_NOCOLOR='NoColor'
BLACK='Black'
BLUE='Blue'
GREEN='Green'
YELLOW='Yellow'
RED='Red'
WHITE='White'
BROWN='Brown'

#Modes for colorsensors
MODE_COL_REFLECT = 'COL-REFLECT' #Reflected light. Red LED on.
MODE_COL_AMBIENT = 'COL-AMBIENT' #Ambient light. Blue LEDs on.
MODE_COL_COLOR = 'COL-COLOR' #Color. All LEDs rapidly cycling, appears white.

#Modes for gyrosensor
MODE_GYRO_ANG = 'GYRO-ANG'
MODE_GYRO_RATE = 'GYRO-RATE'
MODE_GYRO_FAS = 'GYRO-FAS'
MODE_GYRO_G_A = 'GYRO-G&A'
MODE_GYRO_CAL = 'GYRO-CAL'

#Steering values limit for motor action
max_steering = 100
min_steering = -100
