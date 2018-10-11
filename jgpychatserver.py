#JGPyChatServer server side script
import socket 
import select 
import sys 
from thread import *
#Cmd line server for jgpychat
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
#requires 3 arguments on cmd line
if len(sys.argv) != 3: 
    print ("Correct usage: script, IP address, port number")
    exit() 
#setup server variables
ip = str(sys.argv[1]) 
port = int(sys.argv[2]) 
server.bind((ip, port))
#listen for clients 
server.listen(100) 
clients = [] 
#Client connection function
def clientThread(conn, addr): 
    conn.send("Welcome to the chat!") 
    while True: 
            try: 
                message = conn.recv(2048) 
                if message: 
                    print ("<" + addr[0] + "> " + message )
                    sendMessage = "<" + addr[0] + "> " + message 
                    broadcast(sendMessage, conn) 
                else: 
                    remove(conn) 
            except: 
                continue
#Broadcast messages
def broadcast(message, connection): 
    for client in clients: 
        if client!=connection: 
            try: 
                client.send(message) 
            except: 
                client.close() 
                remove(client) 
#Remove connection
def remove(connection): 
    if connection in clients: 
        clients.remove(connection)
#Start server loop 
while True: 
    conn, addr = server.accept() 
    clients.append(conn)   
    print (addr[0] + " connected")
    start_new_thread(clientThread,(conn,addr))     
conn.close() 
server.close() 
