# libs #
import time
import os

# vars #
loading = "Writing message..."
msg = ""
msg_quan = 0
flood_space = []

# main functions #
clear = lambda: os.system('clear')
def cont(slash):
	global command
	command = input(slash)
def flood_cyc():
	i = 0
	while i < int(msg_quan):
		i = i + 1
		print(msg)
		flood_space.append(msg)
###########################
#                      MENU                             #
###########################
print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\nFlood Machine\n▓▓▓▓▓▓▓by jbibigon▓▓▓\n[Enter to continue]")
cont("/")

###########################
#                      CMDS                             #
###########################
if command == "flood":
	msg = input("» Type a message: ")
	msg_quan = input("» Type a message quanity (number): ")
	print(loading)
	############
	time.sleep(1)
	clear()
	loading = "Successfully wrote a flood message!"
	print(loading)
	flood_cyc()
	############
	input("[Enter to copy text]")
	flood_msg = open("flood.txt", "w+")
	print("Successfully copied to file «flood.txt»!")
	flood_text = ' '.join(flood_space)
	print(flood_text)
	flood_msg.write(flood_text)
	flood_msg.close()
cont("/")
if command != "flood":
	print("Incorrect command!")