import os

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
                camera,
                teamSize
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
                self.teamSize = teamSize
        def __repr__(self):
                text = f"""
\033[34m{self.name}\033[0m
Production Year: {self.year}
Team Size: {self.teamSize}\033[36m
--Structure--
Frame: {self.frame}
Housing: {self.housing}
Battery: {self.battery}
Camera: {self.camera}
Thrusters: {self.nThrusters} {self.Thruster}
\033[32m---Sensors---
"""             
                for item in self.sensors:
                        text += item+'\n'
                text += '\033[0m'
                return text
        
        def getYear(self):
                return self.year


brHue = Auv('BrHUE',
            6, 
            'Blue Robotics T200',
            ['Bii-7141 Hydrophones','MTi-G-AHRS IMU'],
            2020,
            'Forseti Aluminum Profile',
            'Ciprast Acrylic',
            'MaxAmps 5200mAh 4S LiPo',
            'Logitech C920',
            35
            )

lua = Auv('Lua',
          8,
          'Blue Robotics T200',
          ['XSens Compass','Parker Lord Microstain Compass',
           'DVL A50', 'BAR 30 Depth Sensor', 'Mti-G-AHRS IMU',
           '3DM-CX5-10 IMU', 'Bii-7141 Hydrophones'],
           2022,
          'Aluminum Profile',
          'Custom Format Acrylic',
          'URUAV 10000mAh 4S LiPo',
          'Logitech C270',
          42
        )

auvList = [brHue, lua]

def clear():
        if os.name == 'nt':
                os.system('cls')
        else:
                os.system('clear')

def sortAuvYear(auvList):
        auvList.sort(key= lambda auv: auv.year, reverse=True)

def sortAuvTeamSize(auvList):
        auvList.sort(key= lambda auv: auv.teamSize, reverse=True)

def mainMenu():
        msg = ''
        while True:
                clear()
                print("\033[34m") #print em azul
                print("""
Welcome to
░▒█▄░▒█░█▀▀▄░█░▒█░▀█▀░░▀░░█░░█░▒█░█▀▀
░▒█▒█▒█░█▄▄█░█░▒█░░█░░░█▀░█░░█░▒█░▀▀▄
░▒█░░▀█░▀░░▀░░▀▀▀░░▀░░▀▀▀░▀▀░░▀▀▀░▀▀▀
AUV Showcase""")
                print(msg)
                print("\033[0m") #retornar cor do terminal
                print("Please choose an AUV")
                for i in range(len(auvList)):
                        print(f"{str(i+1)} - {auvList[i].name}  ({auvList[i].year}/{auvList[i].teamSize} members)")
                print("\033[34m'y' to sort by AUVs by year\n't' to sort by team size\n'q' to quit\033[0m")
                choice = input()
                if (choice == 'y'):
                        sortAuvYear(auvList)
                        msg = ''
                elif (choice == 't'):
                        sortAuvTeamSize(auvList)
                        msg = ''
                elif (choice == 'q'):
                        clear()
                        return 0
                else:
                        if (choice.isdigit()):
                                if (int(choice) >= 1 and int(choice) <= len(auvList)):
                                        clear()
                                        print(auvList[int(choice)-1])
                                        print("press enter to return to main menu")
                                        input()
                                        msg=''
                                else:
                                        msg="\033[31mInvalid input...\033[0m"
                        else:
                                msg="\033[31mInvalid input...\033[0m"


mainMenu()

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
