class Auv:
    def __init__(
            self, 
            name, 
            nThrusters,
            Thruster,
            sensors, 
            year,
            frame,
            housing,
            battery,
            camera
            ):
        self.name = name
        self.nThrusters = nThrusters
        self.Thruster = Thruster
        self.sensors = sensors
        self.year = year
        self.frame = frame
        self.housing = housing
        self.battery = battery
        self.camera = camera


brHue = Auv('BrHUE',
            6, 
            'Blue Robotics T200',
            ['Bii-7141 Hydrophones','MTi-G-AHRS IMU'],
            2020,
            'Forseti Aluminum Profile',
            'Ciprast Acrylic',
            'MaxAmps 5200mAh 4S LiPo',
            'Logitech C920'
            )

lua = Auv('Lua',
          8,
          'Blue Robotics T200',
          ['XSens Compass','Parker Lord Microstain Compass',
           'DVL A50', 'BAR 30 Depth Sensor', 'Mti-G-AHRS IMU',
           '3DM-CX5-10 IMU', 'Bii-7141 Hydrophones'],
          'Aluminum Profile',
          'Custom Format Acrylic',
          'URUAV 10000mAh 4S LiPo',
          'Logitech C270'
        )
#BrHUE 2020
# 6 Blue Robotics T200 Thrusters
# 5 deg of freedom: x,y,z,yaw,pitch
# ---STRUCTURAL
# aluminum frame
# naval aluminum cover
# acrylic main hull
# 3d printed ABS fillament thruster holders
# AISI 1020 Carbon Steel rods
# ---SENSORS
# camera logitech C920
# **Hydrophones Bii-7141
# 
# ---ELECTRICALS
# 4S Lipo Battery with Status and Temperature gauges
# Internal Coms: ATMEGA controller
#
#Lua
#---SENSORS
#camera logitech c270
#xsens compass, parker lord microstain compass
#DVL A50
#BAR 30 Depth Sensor
#MTi-G-AHRS IMU
#3DM-CX5-10 IMU
#
