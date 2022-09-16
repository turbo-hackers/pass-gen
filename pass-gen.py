#!/usr/bin/env python3
# coded by TURB0
# github https://github.com/turbo-hackers

import random,os,sys,time

#colors
yellow ='\033[93m'
green ='\033[92m'
cyan ='\033[96m'
reset = '\033[0m'
blink = "\033[5;96m"
#Banner Code
def banner():
	r ='\033[91m' # red
	g ='\033[92m' # green
	b ='\033[96m' # blue
	y ='\033[93m' # yellow
	reset = '\033[0m'
	blink = "\033[5;96m"
	os.system("clear")
	print(g+"Tool is Starting....../"+reset)
	time.sleep(1)
	os.system("clear")
	print (b+"""
	        _____
	       / ___ \\
	      / /   \\ \\
	     _| |___| |_
	    |    ( )    |"""+r+"""     ┌──┐┌──┐┌──┐┌──┐     ┌──┐┌──┐┌──┐"""+b+"""
	    |    /_\    |"""+r+"""     ├──┘├──┤└──┐└──┐┌───┐│ ─┐├┤  │  │"""+g+"""
	╔═══════════════════╗"""+r+""" └   └  ┘└──┘└──┘└───┘└──┘└──┘└  ┘"""+g+"""
	║ \|/ \|/ \|/  ___  ║
	║ /|\ /|\ /|\ |___| ║
	╚═══════════════════╝ v 2.0 
	"""+reset)
	print (" ")
	print (y+"                      <===[["+b+" coded by"+blink+" TURB0 "+reset+y+"]]===>"+y+"\n")
	print (y+"                   <---("+r+" GitHub- Turbo Hackers "+y+")--->"+y+"\n"+reset)

#gen code
def gen():
	length = int(input(cyan+"\n\nEnter The Length Of The Password: "+reset))
	char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%^&!*_-+=?/\\:;"
	print (" ")
	print (yellow+"-------> Password Generated <-------"+reset)
	print (" ")
	password = (green+" "+reset)
	for i in range(length):
		
		password += random.choice(char)
		
	print ("\t"+password)
	print (" ")
	print (yellow+"-------> Take Your Password <-------"+reset)
def main():
	banner()
	gen()
main()
