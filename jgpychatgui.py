#!/usr/bin/python3
from tkinter import *
import tkinter as tk

import socket 
import select 
import sys 
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect():
	try:
		strPort=port.get()
		intPort = int(strPort)
		server.connect((serverIP.get(), intPort)) 
		print("Connected")
		root.destroy()
		root2=tk.Tk()
		root2.title("JGPyChat - Chat Window")
		root2.mainloop()
	except:
		print("Unable to connect; bad address and port number!")

root = tk.Tk()

root.title("JGPyChat")

root.configure(background="#e5edf9")

separator0 = Frame()
separator0.pack(padx=35, pady=10)

serverLabel = Label(text="Server IP").pack()

separator1 = Frame()
separator1.pack(padx=35, pady=20)

serverIP = Entry(root, width=17, font="Times 20", justify=CENTER, background="#e5edf9",)
serverIP.pack()


separator2 = Frame()
separator2.pack(padx=35, pady=20)

serverLabel = Label(text="Port Number").pack()

separator3 = Frame()
separator3.pack(padx=35, pady=20)

port = Entry(root, width=17, font="Times 20", justify=CENTER, background="#e5edf9")
port.pack()


separator4 = Frame()
separator4.pack(padx=35, pady=20)

b = Button(root, text="Connect", width=25, height=2,command=connect)#command=connect
b.pack()


#Place window in middle
w = 395 # width for the Tk root
h = 380 # height for the Tk root
# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
# set the dimensions of the screen and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.mainloop()