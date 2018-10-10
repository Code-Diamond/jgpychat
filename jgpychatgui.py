#!/usr/bin/python3
from tkinter import *
import tkinter as tk
import socket 
import select 
import sys 
import os
import signal
from threading import Thread
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
	#Receive message
	def receive():
		try:
			message = str(server.recv(2048).decode("utf-8"))
			receivedMessages.insert(0, message)
			chatWindow.update()
		except:
			print("Exception flag : 0")

	#connect
	intPort = int(port.get())
	server.connect((serverIP.get(), intPort)) 
	print("Connected")
	#distroy connect window
	connectWindow.destroy()
	
	########################
	#      Chat Window     #
	########################
	
	
	def send():
		message=messageBox.get()
		server.send(bytes(message.encode("utf-8")))
		messageList.insert(END,"[You]"+message)
	#Receive messages
	def receive():
		while True:
			try:
				message = str(server.recv(2048).decode("utf-8"))
				messageList.insert(END, message)
			except OSERROR:
				break
	def onClosing():
		chatWindow.destroy()
		os.kill(os.getpid(),signal.SIGKILL)

	chatWindow=tk.Tk()
	chatWindow.title("JGPyChat - Chat Window")
	#Message Frame
	messagesFrame = tk.Frame(chatWindow)
	messageBox = tk.StringVar()  
	messageBox.set("")

	scrollbar = tk.Scrollbar(messagesFrame)  
	
	# Contain messages in a listbox
	messageList = tk.Listbox(messagesFrame, height=15, width=50, yscrollcommand=scrollbar.set)
	scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
	messageList.pack(side=tk.LEFT, fill=tk.BOTH)
	messageList.pack()
	messagesFrame.pack()
	# User entry box
	entryBox = tk.Entry(chatWindow, textvariable=messageBox)
	entryBox.bind("<Return>", send)
	entryBox.pack()
	send_button = tk.Button(chatWindow, text="Send", command=send)
	send_button.pack()

	#Completely close program
	chatWindow.protocol("WM_DELETE_WINDOW", onClosing)
	#Threading for receiving messages
	receive_thread = Thread(target=receive)
	receive_thread.start()

	########################
	#Place window in middle
	########################
	w = 395 # width for the Tk connectWindow
	h = 380 # height for the Tk connectWindow
	# get screen width and height
	ws = chatWindow.winfo_screenwidth() # width of the screen
	hs = chatWindow.winfo_screenheight() # height of the screen
	# calculate x and y coordinates for the Tk connectWindow 
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	# set the dimensions of the screen and where it is placed
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
