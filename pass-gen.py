#!/bin/python
import random,os,sys,time

#colors
yellow ='\033[93m'
green ='\033[92m'
cyan ='\033[96m'
black ='\033[1m'
#Banner Code
def banner():
	r ='\033[91m' # red
	g ='\033[92m' # green
	b ='\033[96m' # blue
	y ='\033[93m' # yellow
	bl ='\033[1m' # black
	os.system("clear")
	print(g+bl+"Tool is Starting....../"+g+bl)
	time.sleep(1)
	os.system("clear")
	print (b+bl+"""
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
	"""+bl+b)
	print (" ")
	print (y+bl+"                      <===[["+b+bl+" coded by TURB0 "+y+bl+"]]===>"+y+bl+"\n")
	print (y+bl+"                   <---("+r+bl+" GitHub- Turbo Hackers "+y+bl+")--->"+y+bl+"\n")

#gen code
def gen():
	length = int(input(cyan+black+"\n\nEnter The Length Of The Password: "+cyan+black))
	char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%^&!*_-+=?/\\:;"
	print (" ")
	print (yellow+black+"-------> Password Generated <-------"+yellow+black)
	print (" ")
	password = (green+black+" "+green+black)
	for i in range(length):
		
		password += random.choice(char)
		
	print ("\t"+password)
	print (" ")
	print (yellow+black+"-------> Take Your Password <-------"+yellow+black)
def main():
	banner()
	gen()
main()
