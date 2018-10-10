#!/usr/bin/python3
from tkinter import *
import tkinter as tk
import socket 
import select 
import sys 
#Client side server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
########################
#        Connect       #
########################
def connect():
	#Send message method
	def send():
		message=messageBox.get()
		server.send(bytes(message.encode("utf-8")))
		receivedMessages.insert(END,"\n"+message)
	#connect
	intPort = int(port.get())
	server.connect((serverIP.get(), intPort)) 
	print("Connected")
	#distroy connect window
	connectWindow.destroy()
	
	########################
	#      Chat Window     #
	########################
	
	chatWindow=tk.Tk()
	chatWindow.title("JGPyChat - Chat Window")

	#Spacing
	chatWindowHeaderSpacing = Frame()
	chatWindowHeaderSpacing.pack(padx=35, pady=20)
	# User received messages box
	receivedMessages = Entry(chatWindow, width=200, font="Times 20", justify=CENTER, background="#e5edf9",)
	receivedMessages.pack()
	#Spacing
	receivedMessagesSpacing = Frame()
	receivedMessagesSpacing.pack(padx=35, pady=20)
	#User Entry box
	messageBox = Entry(chatWindow, width=17, font="Times 20", justify=CENTER, background="#e5edf9",)
	messageBox.pack()
	#Spacing
	sendButtonSpacing = Frame()
	sendButtonSpacing.pack(padx=35, pady=20)
	#Send buton
	sendButton = Button(chatWindow, text="Send", width=25, height=2,command=send)
	sendButton.pack()
	
	#socket functionality
	sockets = [sys.stdin, server] 
	read_sockets,write_socket, error_socket = select.select(sockets,[],[]) 
	for socks in read_sockets: 
		if socks == server: 
			message = str(socks.recv(2048).decode("utf-8"))
			receivedMessages.insert(0, message)
		else:  
			send()
			
	#same window characteristics as the main window
	chatWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
	chatWindow.mainloop()
	
########################
#      Main Window     #
########################
#Create connect window
connectWindow = tk.Tk()
connectWindow.title("JGPyChat")
connectWindow.configure(background="#e5edf9")
#Header spacing
headerSpacing = Frame()
headerSpacing.pack(padx=35, pady=10)
#Label for Entry
serverLabel = Label(text="Server IP").pack()
#Spacing
serverLabelSpacing = Frame()
serverLabelSpacing.pack(padx=35, pady=20)
#Server IP Entry
serverIP = Entry(connectWindow, width=17, font="Times 20", justify=CENTER, background="#e5edf9",)
serverIP.pack()
#Spacing
seperatorSpacing = Frame()
seperatorSpacing.pack(padx=35, pady=20)
#Label for port Entry
portLabel = Label(text="Port Number").pack()
#Spacing
portLabelSpacing = Frame()
portLabelSpacing.pack(padx=35, pady=20)
#Server Port Entry
port = Entry(connectWindow, width=17, font="Times 20", justify=CENTER, background="#e5edf9")
port.pack()
#Spacing
connectButtonSpacing = Frame()
connectButtonSpacing.pack(padx=35, pady=20)
#Connect Button
connectButton = Button(connectWindow, text="Connect", width=25, height=2,command=connect)#command=connect
connectButton.pack()
########################
#Place window in middle
########################
w = 395 # width for the Tk connectWindow
h = 380 # height for the Tk connectWindow
# get screen width and height
ws = connectWindow.winfo_screenwidth() # width of the screen
hs = connectWindow.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk connectWindow 
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
# set the dimensions of the screen and where it is placed
connectWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

connectWindow.mainloop()
