#================================================================================TKinter=================================================================================================
# from tkinter import *

# def convert_celsius():
#     temp = float(e1.get())
#     fahrenheit = (temp * 9/5) + 32
#     lbl3.config(text=f"{fahrenheit:.2f} °F")
    
# def convert_fahrenheit():
#     temp = float(e2.get())
#     celsius = (temp - 32) * 5/9
#     lbl3.config(text=f"{celsius:.2f} °C")

# app = Tk()
# app.title("Temperature Converter")
# app.geometry("400x300")

# lbl1 = Label(app, text="Input Celsius")
# lbl1.grid(row=0, column=0, padx=5, pady=5)
# e1 = Entry(app)
# e1.grid(row=0, column=1, padx=5, pady=5)

# lbl2 = Label(app, text="Input Fahrenheit")
# lbl2.grid(row=1, column=0, padx=5, pady=5)
# e2 = Entry(app)
# e2.grid(row=1, column=1, padx=5, pady=5)

# bt1 = Button(app, text="Convert to Fahrenheit", command=convert_celsius)
# bt1.grid(row=0, column=2, padx=5, pady=5)

# bt2 = Button(app, text="Convert to Celsius", command=convert_fahrenheit)
# bt2.grid(row=1, column=2, padx=5, pady=5)

# lbl3 = Label(app, text="")
# lbl3.grid(row=2, column=1, padx=5, pady=5)

# app.mainloop()



# from tkinter import *
# app = Tk()
# app.title("Q-2")
# app.geometry("300x300")
# lbl1 = Label(app , text="Name:")
# lbl1.grid(row=0 , column=0, padx=5, pady=5)
# e1 = Entry(app)
# e1.grid(row=0 , column=1, padx=5, pady=5)
# lbl2 = Label(app , text="Age:") 
# lbl2.grid(row=1 , column=0, padx=5, pady=5)
# e2 = Entry(app)
# e2.grid(row=1 , column=1, padx=5, pady=5)
# lbl3 = Label(app , text="Gender:")
# lbl3.grid(row=2 , column=0, padx=5, pady=5)
# gender = IntVar()
# r1 = Radiobutton(app , text="Male" , variable=gender , value="1")
# r2 = Radiobutton(app , text="Female" , variable=gender , value="2")
# r1.grid(row=2 , column=1, padx=5, pady=5)
# r2.grid(row=2 , column=2, padx=5, pady=5)
# bt1 = Button(app , text="Submit")
# bt1.grid(row=3 , column=1, padx=5, pady=5)
# app.mainloop()



# from tkinter import *

# app = Tk()
# app.title("tk #2")
# app.geometry("300x300")

# lbl1 = Label(app , text="Last Name:")
# lbl1.grid(row=0 , column=0, padx=5, pady=5)
# e1 = Entry(app)
# e1.grid(row=0 , column=1, padx=5, pady=5)

# lbl2 = Label(app , text="First Name:")
# lbl2.grid(row=1 , column=0, padx=5, pady=5)
# e2 = Entry(app)
# e2.grid(row=1 , column=1, padx=5, pady=5)

# lbl3 = Label(app , text="Job:")
# lbl3.grid(row=2 , column=0, padx=5, pady=5)
# e3 = Entry(app)
# e3.grid(row=2 , column=1, padx=5, pady=5)

# lbl4 = Label(app , text="Country:")
# lbl4.grid(row=3 , column=0, padx=5, pady=5)
# e4 = Entry(app)
# e4.grid(row=3 , column=1, padx=5, pady=5)

# bt1 = Button(app , text="Show")
# bt1.grid(row=4, column=0, padx=5, pady=10)

# bt2 = Button(app , text="Quit")
# bt2.grid(row=4, column=1, padx=5, pady=10)

# app.mainloop()


# from tkinter import *
# app = Tk()
# app.title("My GUI")
# app.geometry("400x300")
# lbl1 = Label(app , text ="Welcome to my GUI")
# lbl1.pack()
# ch1 = Checkbutton(app , text="Check me")
# ch1.pack()
# radio = IntVar()
# r1 = Radiobutton(app , text="Option 1" , variable=radio , value="1")
# r2 = Radiobutton(app , text="Option 2" , variable=radio , value="2")
# r1.pack()
# r2.pack()
# e1 = Entry(app)
# e1.pack()
# bt1 = Button(app , text="Submit")
# bt1.pack()
# bt2 = Button(app , text="Clear")
# bt2.pack()
# app.mainloop()


# from tkinter import *
# app = Tk()
# app.title("My GUI")
# app.geometry("400x300")
# lbl1 = Label(app , text ="Welcome to my GUI")
# lbl1.pack()
# sl1 = Scale(app , from_=0 , to=100 , orient = HORIZONTAL)
# sl1.pack()
# app.mainloop()

# import socket
# import threading

# clients = []

# def handle_client(client):
#     while True:
#         try:
#             msg = client.recv(1024).decode()
#             broadcast(msg, client)
#         except:
#             clients.remove(client)
#             client.close()
#             break

# def broadcast(msg, sender):
#     for c in clients:
#         if c != sender:
#             try:
#                 c.send(msg.encode())
#             except:
#                 pass

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('localhost', 12345))
# server.listen()

# print("Server is running...")

# while True:
#     client, addr = server.accept()
#     clients.append(client)
#     threading.Thread(target=handle_client, args=(client,)).start()



# from socket import *
# from threading import Thread
# clients = []
# def handle_client(client):
#     while True:
#         msg = client.recv(1024).decode()
#         for c in clients:
#             if c != client:
#                 c.send(msg.encode())

# server = socket(AF_INET , SOCK_STREAM)
# host = '127.0.0.1'
# port = 12345
# server.bind((host, port))
# server.listen()
# while True:
#     c, addr = server.accept()
#     clients.append(c)
#     Thread(target=handle_client, args=(c,)).start()
#     print(f"Connected to {addr}")
#     c.send("Welcome to the chat room!".encode())




# from socket import *
# from threading import Thread
# def recive (client):
#     while True:
#         msg = client.recv(1024).decode()
#         print(msg)
# def send(client):
#     while True:
#         msg = input()
#         client.send(msg.encode())
# c = socket(AF_INET , SOCK_STREAM)
# host = '127.0.0.1'
# port = 12345
# c.connect((host , port))
# Thread(target=recive, args=(c,)).start()
# Thread(target=send, args=(c,)).start()



