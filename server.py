import socket 
from tkinter import *
from threading import Thread
import random
from unicodedata import name


SERVER = None
ip_address = '127.0.0.1'
PORT = 6000

def setup():
    print("\n\t\t\t\t\t***Welcome to the Tambola game***")


    global SERVER
    global PORT
    global IP_ADDRESS


    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    thread = Thread(target = recivedMsg)
    thread.start

def playerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1

    nameWindow = Tk()
    nameWindow.name = ["Tambola Family Fun"]
    nameWindow.geometry('800x600')

    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./assets/background.png")
    canvas1 = canvas(nameWindow, width = 500, height = 500)
    canvas1.pack(fill = "both", expans = True)

    canvas1.create_image(0, 0, image = bg, aqnchor = "nw")
    canvas1.create_test( screen_width/4.5, screen_height/8, test = "Enter Name", font = ("Chalkboard SE", 60),fill = black)

    nameEntry = Entry(nameWindow, width = 15, justify = 'center', font('chalkboard SE', 38), bd = 5, bg = 'white')
    nameEntry.place(x = screen_width/7, y = screenHeight/5.5)

    button = Button(nameWindow, text="save", font - ('Chalkboard SE'), width = 11, command = saveName, height = 2, bg = "80deea", bd = 3)
    button.place(x = screen_wdith/6, y = screenHeight/5.5)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()

def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())

def acceptConnections():
    global CLIENTS
    global SERVER

    while True:
        player_socket, addre = SERVER.accept()
        player_name = player_socket.recv(1024).decode().strip()
        print(player_name)
        if(len(CLIENTS.keys()) == 0 ):
            CLIENTS[player_name] = {'player_type': 'player1'}
        else:
            CLIENTS[player_name] = {'player_type': 'player2'}

        CLIENTS[player_name]["player_socket"] = player_socket
        CLIENTS[player_name]["address"] = addre
        CLIENTS[player_name]['player_name'] = player_name
        CLIENTS[player_name]['turn'] = False

        print(f"Connection established with {player_name}: {addres}")
        



