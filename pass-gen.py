#!/usr/bin/env python3
# coded by TURB0
# github https://github.com/turbo-hackers

import random,os,sys,time

# colors
r ='\033[91m' # red
g ='\033[92m' # g
s_b ='\033[96m' # sky_blue
y ='\033[93m' # y
p = '\033[94m' # purple
pi = '\033[95m' # pink
reset = '\033[0m'
blink = "\033[5;96m"

def main():
	
	#Banner Code
	def banner():
		
		os.system("clear")
		print (s_b+"""
            _____
           / ___ \\
          / /   \\ \\
         _| |___| |_
        |    ( )    |"""+r+"""     ┌──┐┌──┐┌──┐┌──┐     ┌──┐┌──┐┌──┐"""+s_b+"""
        |    /_\    |"""+r+"""     ├──┘├──┤└──┐└──┐┌───┐│ ─┐├┤  │  │"""+g+"""
    ╔═══════════════════╗"""+r+""" └   └  ┘└──┘└──┘└───┘└──┘└──┘└  ┘"""+g+"""
    ║ \|/ \|/ \|/  ___  ║
    ║ /|\ /|\ /|\ |___| ║
    ╚═══════════════════╝ v1.0 
		"""+reset)
		print ("                  "+y+"<===[["+s_b+" coded by"+blink+" TURB0 "+reset+y+"]]===>\n"+reset)
		print ("               "+y+"<---("+r+" GitHub- Turbo Hackers "+y+")--->"+y+"\n"+reset)

	#gen code
	def gen():
		length = int(input(s_b+"\n\nEnter The Length Of The Password: "+reset))
		char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%^&!*_-+=?/\\:;"
		print (" ")
		print (y+"-------> Password Generated <-------"+reset)
		print (" ")
		password = (g+" "+reset)
		for i in range(length):
			
			password += random.choice(char)
			
		print ("\t"+password)
		print (" ")
		print (y+"-------> Take Your Password <-------"+reset)

	banner()
	gen()


try:
	main()
except:
	print(y+"\n["+r+"Error"+y+"]"+s_s_b+" Something went wrong! Please try again after some time.")
	error_msg = input(s_b+"Press any key to Close the program ... ")
	exit(0)

