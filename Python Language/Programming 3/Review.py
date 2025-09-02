# from socket import *
# s = socket(AF_INET , SOCK_STREAM)
# host = "127.0.0.1"
# port = 12345
# s.connect((host,port))
# s.send("Hello  , server")
# s.close()



# from socket import *
# s = socket(AF_INET , SOCK_STREAM)
# host = "127.0.0.1"
# port = 12345
# s.bind((host , port))
# s.listen(5)
# while True:
#     c , addr = s.accept()
#     print("got connection from" , addr)
#     data = c.recv(1024)
#     print(data)
#     c.sendall("Message Recevied!")
#     c.close()



# from tkinter import *
# top = Tk()
# top.title("tk#2")
# top.geometry("400x300")
# lbl1 = Label(top , text="Last Name : ")
# lbl1.grid(row = 0 , column = 0 , padx=10 , pady=5)
# e1 = Entry(top)
# e1.grid(row = 0 , column=1 , padx=10 , pady=5)
# lbl2 = Label(top , text="First Name : ")
# lbl2.grid(row = 1 , column = 0 , padx=10 , pady=5)
# e2 = Entry(top)
# e2.grid(row = 1 , column=1 , padx=10 , pady=5)
# lbl3 = Label(top , text="Job : ")
# lbl3.grid(row = 2 , column = 0 , padx=10 , pady=5)
# e3 = Entry(top)
# e3.grid(row = 2 , column=1 , padx=10 , pady=5)
# lbl4 = Label(top , text="Country : ")
# lbl4.grid(row = 3 , column = 0 , padx=10 , pady=5)
# e4 = Entry(top)
# e4.grid(row = 3 , column=1 , padx=10 , pady=5)
# btn1 = Button(top , text="Show")
# btn1.grid(row = 4 , column=0)
# btn2 = Button(top , text = "Quit")
# btn2.grid(row = 4 , column=1)
# top.mainloop()


# from tkinter import *
# top = Tk()
# top.title ("Login Form")
# top.geometry("400x300")
# lbl1 = Label(top , text= "Username : ")
# lbl1.pack()
# e1 = Entry(top)
# e1.pack()
# lbl2 = Label(top , text= "Password : ")
# lbl2.pack()
# e2 = Entry(top , show="*")
# e2.pack()
# btn1 = Button(top , text="Login")
# btn1.pack()
# top.mainloop()


# from tkinter import *
# top = Tk()
# top.title("My GUI")
# top.geometry("400x300")
# lbl1 = Label (top , text="Welcome to my Gui")
# lbl1.pack()
# ch1 = Checkbutton(top , text="Check me")
# ch1.pack()
# r1 = Radiobutton(top , text="Option 1" , value=1)
# r1.pack()
# r2 = Radiobutton(top , text="Option 2" , value=2)
# r2.pack()
# e1 = Entry(top)
# e1.pack()
# bt1 = Button(top , text="Submit")
# bt1.pack()
# bt2 = Button(top , text="Clear")
# bt2.pack()
# top.mainloop()



# class UserProfile:
#     def __init__(self, user_id):
#         self.user_id = user_id
#         # Load user details
#         self.details = self._load_user_details(user_id)
#         # Initialize payment gateway
#         self.payment = self._init_payment_gateway()
#         # Connect to notification service
#         self.notification = self._connect_notification_service()

#     def _load_user_details(self, user_id): return f"Details for {user_id}"
#     def _init_payment_gateway(self): return "Payment Gateway Initialized"
#     def _connect_notification_service(self): return "Notification Service Connected"

#     def display_profile(self):
#         print(f"User: {self.user_id}, Details: {self.details}")

#     def make_payment(self, amount):
#         print(f"{self.payment}: Processing ${amount}")

#     def send_notification(self, message):
#         print(f"{self.notification}: Sending '{message}'")


# class Facade : 
#     def __init__(self, user_id):
#         self.user = UserProfile(user_id)
    
#     def all_operations(self):
#         self.user._load_user_details(self.user.user_id)
#         self.user._init_payment_gateway()
#         self.user._connect_notification_service()
#     def display_profile(self):
#         self.user.display_profile()
#     def make_payment(self, amount):
#         self.user.make_payment(amount)
#     def send_notification(self, message):
#         self.user.send_notification(message)
    
# facade1 = Facade("user123")
# facade1.all_operations()
# facade1.display_profile()
# facade1.make_payment(100)
# facade1.send_notification("Hello")



# class Character:
#     def __init__ (self , symbol):
#         self.symbol = symbol
#     def display (self,  font , size):
#         print(f"Displaying {self.symbol} in {font} font , font size {size}")
# class CharacterFactory:
#     _characters = {}
#     @staticmethod
#     def get_character(symbol):
#         if symbol not in CharacterFactory._characters:
#             CharacterFactory._characters[symbol] = Character(symbol)
#         return CharacterFactory._characters[symbol]

# factory = CharacterFactory()
# char1 = factory.get_character('A')
# char2 = factory.get_character('B')
# char1.display("Arial" , 12)
# char2.display("Times New Roman" , 30)



# class handler :
#     def __init__ (self, successor = None):
#         self.successor = successor
#     def handle (self , request):
#         if self.successor:
#             self.successor.handle(request)
        
# class ConceretehandlerA(handler):
#     def handle(self, request):
#         if request == "A":
#             print("Handler A is processing the request")
#         else:
#             super().handle(request)
# class ConceretehandlerB(handler):
#     def handle(self, request):
#         if request == "B":
#             print("Handler B is processing the request")
#         else:
#             super().handle(request)
# class ConceretehandlerC(handler):
#     def handle(self, request):
#         if request == "C":
#             print("Handler C is processing the request")
#         else:
#             super().handle(request)
            
# A = ConceretehandlerA()
# B = ConceretehandlerB()
# C = ConceretehandlerC()
# A.successor = B
# B.successor = C
# A.handle("A")
# B.handle("B")
# C.handle("C")


# from socket import * 
# s = socket(AF_INET , SOCK_STREAM)
# host = "127.0.0.1"
# port  = 9999
# s.bind((host , port))
# s.listen(5)
# print("Server is listening on port", port)
# while True : 
#     c , addr = s.accept()
#     print("Got connection from", addr)
#     data = c.recv(1024)
#     data = data.decode('utf-8')
#     print("Received data:", data)
#     c.send(data.encode('utf-8'))
#     c.close()


# from socket import *
# s = socket(AF_INET, SOCK_STREAM)
# host = '127.0.0.1'
# port = 9999
# s.connect((host, port))
# while True : 
#     data = input("Enter message to send to server (or 'exit' to quit): ")
#     if data.lower() == 'exit':
#         break
#     s.send(data.encode('utf-8'))
#     response = s.recv(1024)
#     print("Received from server:", response.decode('utf-8'))
    
# from _thread import *
# import time 

# def print_time (threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print(f"{threadName}: {time.ctime(time.time())}")
# try:
#     start_new_thread(print_time, ("Thread-1", 2))
#     start_new_thread(print_time, ("Thread-2", 4))
# except:
#     print("Error: unable to start thread")
# while 1:
#     pass
    
    
# from threading import * 
# import time 

# def print_time (threadnmae , delay):
#     count =  0 
#     if count < 3 : 
#         time.sleep(delay)
#         count +=1 
#         print(f"{threadnmae}: {time.ctime(time.time())}")

# t1 = Thread (target = print_time , args = ("Thread-1", 1))
# t2 = Thread (target = print_time  , args = ("Thread-2", 2))

# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("done")


# import threading 
# def print_squeare (num):
#     print(f"The squeare of {num} is {num * num}")

# def print_cube (num):
#     print(f"The cube of {num} : {num * num * num}")
    
# t1 = threading.Thread(target = print_squeare, args=(10,))
# t2 = threading.Thread(target = print_cube, args=(10,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Done")



# from tkinter import *

# root = Tk()
# root.geometry("500x600")

# def btn_print():
#     print("you are clicked on me")

# def btn2_print():
#     print("hey there")

# def btn3_print():
#     print("hello sweety")

# def hello():
#     print("hello world")

# et1 = Entry(root)
# et1.pack()

# rdbtn1 = Radiobutton(root, text="male", value=1)
# rdbtn2 = Radiobutton(root, text="female", value=2)
# rdbtn1.pack()
# rdbtn2.pack()

# lb1 = Listbox(root)
# lb1.insert(END, "option one")
# lb1.insert(END, "option two")
# lb1.insert(END, "option three")
# lb1.insert(END, "option four")
# lb1.insert(END, "option five")
# lb1.pack()

# ckbtn = Checkbutton(root, text="auto save", font="14", command=hello)
# ckbtn.pack()

# btn1 = Button(root, text="hello my brother", command=btn_print, bg="red", fg="green", width=20, height=2)
# btn2 = Button(root, text="hello there", command=btn2_print, bg="red", fg="green", width=20, height=2)
# btn3 = Button(root, text="hello sweety", command=btn3_print, bg="red", fg="green", width=20, height=2)
# btn1.pack()
# btn2.pack()
# btn3.pack()

# lbl = Label(root, text="This is a label", font=("Arial", 12))
# lbl.pack()

# scale = Scale(root, from_=0, to=100, orient=HORIZONTAL)
# scale.pack()

# spin = Spinbox(root, from_=0, to=10)
# spin.pack()

# txt = Text(root, height=5, width=30)
# txt.pack()

# root.mainloop()



# from tkinter import * 

# parent = Tk ()
# parent.title ("Students")
# parent.geometry("400x300")
# name = Label(parent , text="Name : ")
# name.grid(row=0 , column=0 , padx=10 , pady=5)
# e1 = Entry(parent)
# e1.grid(row=0 , column=1)
# ID_Number = Label(parent , text="ID Number : ")
# ID_Number.grid(row=1 , column=0 , padx=10 , pady=5)
# e2 = Entry(parent)
# e2.grid(row=1 , column=1)
# Department = Label(parent , text="Department : ")
# Department.grid(row=2 , column=0 , padx=10 , pady=5)
# e3 = Entry(parent)
# e3.grid(row=2 , column=1)
# btn = Button(parent , text="Submit" , bg="red" , fg="green")
# btn.grid(row=3 , column=0 , columnspan=2 , padx=10 , pady=5)
# parent.mainloop()


# from tkinter import * 
# root = Tk()
# root.title("Students")
# root.geometry("400x300")
# name  = Label(root , text="Name :")
# name.place(x=10 , y=10)
# e1 = Entry(root)
# e1.place(x=100 , y=10)
# root.mainloop()


# from tkinter import * 
# from functools import partial

# def Call_result(result_label, num1, num2):
#     num1 = int(num1.get())
#     num2 = int(num2.get())
#     result = num1 + num2
#     result_label.config(text=f"Result: {result}")
#     return 

# root = Tk()
# root.title("Simple Calculator")
# root.geometry("400x300")

# number1 = StringVar()
# number2 = StringVar()

# # Use grid instead of pack here
# title_label = Label(root, text="Simple Calculator")
# title_label.grid(row=0, column=1, columnspan=2, pady=10)

# Label(root, text="Enter First Number:").grid(row=1, column=0, padx=10, pady=5)
# Entry(root, textvariable=number1).grid(row=1, column=1, padx=10, pady=5)

# Label(root, text="Enter Second Number:").grid(row=2, column=0, padx=10, pady=5)
# Entry(root, textvariable=number2).grid(row=2, column=1, padx=10, pady=5)

# result_label = Label(root)
# result_label.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

# call_result = partial(Call_result, result_label, number1, number2)
# Button(root, text="Add", command=call_result).grid(row=3, column=0, padx=10, pady=5)

# root.mainloop()


# from flask import Flask
# app = Flask(__name__)
# app.route('/')
# def hello():
#     return "Hello , World"
# if __name__ == "__main__":
#     app.run(host="0.0.0.0")

# from tkinter import * 

# app = Tk()
# app.title("User Greeter")
# app.geometry("400x300")

# def greet_user():
#     name = e1.get()
#     greeting = f"Hello, {name}!"
#     lbl2.config(text=greeting)
# lbl1 = Label(app, text="Enter your name:")
# lbl1.grid(row=0, column=0, padx=10, pady=5)
# e1 = Entry(app)
# e1.grid(row=0, column=1, padx=10, pady=5)
# lbl2 = Label(app)
# lbl2.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
# btn1 = Button(app, text="Greet me", command=greet_user)
# btn1.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
# app.mainloop()


# from tkinter import *
# app = Tk()
# app.title("Temperature Converter")
# app.geometry("400x300")
# def convert_temp():
#     temp = float(e1.get())
#     unit = lst1.get(lst1.curselection())
#     if unit == "Celsius":
#         result = (temp * 9/5) + 32
#     elif unit == "Fahrenheit":
#         result = (temp - 32) * 5/9
#     else:
#         result = None
#     lbl2.config(text=str(result))
#     return result
# lbl1 = Label(app, text="Enter temperature:")
# lbl1.grid(row=0, column=0, padx=10, pady=5)
# e1 = Entry(app)
# e1.grid(row=0, column=1, padx=10, pady=5)
# lbl2 = Label(app)
# lbl2.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
# lbl3 = Label(app, text="Select unit:")
# lbl3.grid(row=2, column=0, padx=10, pady=5)
# lst1 = Listbox(app, height=2)
# lst1.insert(1, "Celsius")
# lst1.insert(2, "Fahrenheit")
# lst1.grid(row=2, column=1, padx=10, pady=5)
# btn1 = Button(app, text="Convert", command=convert_temp)
# btn1.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
# app.mainloop()


# class WeatherData:
#     def __init__(self):
#         self.temperature = 0

#     def set_temperature(self, temp):
#         self.temperature = temp
#         # لازم تحدث كل display يدوي
#         print(f"Phone Display: {temp}")
#         print(f"Web Display: {temp}")


# class obserevr:
#     def Update(self , temp):
#         pass
# class phonedisplay(obserevr):
#     def Update(self, temp):
#         print(f"Phone Display: {temp}")
# class webdisplay(obserevr):
#     def Update(self, temp):
#         print(f"Web Display: {temp}")
# class WeatherData:
#     def __init__ (self):
#         self.observers = []
#         self.temperture = 0
#     def attach(self, observer):
#         self.observers.append(observer)
#     def notify_all(self):
#         for observer in self.observers:
#             observer.Update(self.temperture)
#     def set_temperature(self, temp):
#         self.temperture = temp
#         self.notify_all()
# weather = WeatherData()
# weather.attach(phonedisplay())
# weather.attach(webdisplay())
# weather.set_temperature(25)

# class European_Socket:
#     def Voltage(self):
#         return 230
# class US_Socket:
#     def Voltage(self):
#         return 120
# class Adapter:
#     def __init__ (self,  socket):
#         self.socket =  socket
#     def Voltage(self):
#         return int(str(self.socket.Voltage()).replace("230", "120"))
# european = European_Socket()
# US_adapter = Adapter(european)
# print(f"European Socket Voltage: {US_adapter.Voltage()}V")



# class pizza:
#     def __init__ (self):
#         self.dough = None
#         self.sauce = None
#         self.cheese = None
#         self.toppings = []
#     def __str__(self) :
#         return f"Pizza with {self.dough}, {self.sauce}, {self.cheese} and toppings: {self.toppings}"
# class PizzaBulider:
#     def __init__(self):
#         self.pizza = pizza()
#     def add_dough(self, dough):
#         self.pizza.dough = dough
#         return self
#     def add_sauce(self, sauce):
#         self.pizza.sauce = sauce
#         return self
#     def add_cheese(self, cheese):
#         self.pizza.cheese = cheese
#         return self
#     def add_topping(self , toppings):
#         self.pizza.toppings.append(toppings)
#         return self
#     def build(self):
#         return self.pizza
# # Example usage
# builder = PizzaBulider()
# pizza = builder.add_dough("thin").add_sauce("tomato").add_cheese("mozzarella").add_topping("pepperoni").build()
# print(pizza)

# class SingletonLogger:
#     _instance = None

#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#             print("New Logger Created")
#         return cls._instance

# log1 = SingletonLogger()
# log2 = SingletonLogger()  # نفس الكائن


# class Memento:
#     def __init__(self, state):
#         self._state = state

#     def get_state(self):
#         return self._state

# class TextEditor:
#     def __init__(self):
#         self._text = ""

#     def write(self, text):
#         self._text += text

#     def create_memento(self):
#         return Memento(self._text)

#     def restore(self, memento):
#         self._text = memento.get_state()

#     def get_text(self):
#         return self._text

# # Client
# editor = TextEditor()
# editor.write("Hello ")
# save_point = editor.create_memento()
# editor.write("World")
# print(editor.get_text())  # Hello World

# editor.restore(save_point)
# print(editor.get_text())  # Hello


# class CarsFactory:
#     def create_car(self , car_type):
#         if car_type == "sedan":
#             return Sedan()
#         elif car_type == "suv":
#             return SUV()
#         else :
#             raise ValueError("Unknown car type")
# class Sedan:
#     def drive(self):
#         return "Driving a sedan car"
# class SUV:
#     def drive(self):
#         return "Driving an SUV car"
# car = CarsFactory()
# print(car.create_car("sedan").drive())  




# ======================================================================== Design Patterns =====================================================================================

#Q1 
# class ReportGenerator:
#     def generate_pdf_report(self, data):
#         print("PDF Header")
#         for item in data:
#             print(f"PDF item: {item}")
#         print("PDF Footer")
#         # Complex PDF generation logic...
#         return "pdf_report.pdf"

#     def generate_csv_report(self, data):
#         header = ",".join(data[0].keys() if data else [])
#         rows = [",".join(str(item[key]) for key in header.split(',')) for item in data]
#         # Complex CSV generation logic...
#         return "csv_report.csv"

# # Client
# data_list = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
# generator = ReportGenerator()
# pdf = generator.generate_pdf_report(data_list)
# csv = generator.generate_csv_report(data_list)

#Answer1:
# class ReportFactory:
#     def create_report(self , report_type):
#         if report_type == "pdf":
#             return Pdf()
#         elif report_type == "csv":
#             return Csv()
#         else :
#             raise ValueError("Unknown report type")
# class Pdf:
#     def generate(self, data):
#         print("PDF Header")
#         for item in data:
#             print(f"PDF item: {item}")
#         print("PDF Footer")
#         # Complex PDF generation logic...
#         return "pdf_report.pdf"
# class Csv:
#     def generate(self, data):
#         header = ",".join(data[0].keys() if data else [])
#         rows = [",".join(str(item[key]) for key in header.split(',')) for item in data]
#         # Complex CSV generation logic...
#         return "csv_report.csv"

# report = ReportFactory()
# pdf_report = report.create_report("pdf").generate([{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}])


#Q2
# class Logger:
#     def __init__(self, file_path):
#         self.file_path = file_path
#         print(f"Logger instance created for {file_path}")

#     def log(self, message):
#         with open(self.file_path, "a") as f:
#             f.write(message + "\n")

# # Usage in different modules
# logger1 = Logger("app.log")
# logger1.log("Module 1 event")

# logger2 = Logger("app.log") # Another instance for the same log file
# logger2.log("Module 2 event")

# Answer2:
# from typing_extensions import Self


# class SingletonLogger:
#     _instance = None 
    
#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#             print("New Logger Created")
#         return cls._instance
#     def log(self, message):
#         with open("app.log", "a") as f:
#             f.write(message + "\n")
# # Usage in different modules
# logger1 = SingletonLogger()
# print(logger1.log("Module 1 event"))

# logger2 = SingletonLogger() # Another instance for the same log file
# print(logger2.log("Module 2 event"))


#Q3
# class TextEditor:
#     def __init__(self):
#         self.content = ""
#         self.history = [] # Simplified history

#     def type(self, text):
#         self.history.append(self.content) # Save current state before change
#         self.content += text

#     def undo(self):
#         if self.history:
#             self.content = self.history.pop() # Directly manipulates history
#         else:
#             print("Nothing to undo")

# # Client
# editor = TextEditor()
# editor.type("Hello ")
# editor.type("World!")
# print(f"Current: {editor.content}")
# editor.undo()
# print(f"After Undo: {editor.content}")
# # The editor is managing its own history directly and exposing its state saving mechanism.

# Answer3:
# class Memento:
#     def __init__ (self , state):
#         self.state = state
#     def get_state(self):
#         return self.state
# class Text_Editor:
#     def __init__ (self):
#         self.text = ""
#     def write(self, text):
#         self.text += text
#     def create_memento(self):
#         return Memento(self.text)
#     def restore(self , memento):
#         self.text = memento.get_state()
#     def get_text(self):
#         return self.text

# editor = Text_Editor()
# editor.write("Hello ")
# save_point = editor.create_memento()
# editor.write("World!")
# print(f"Current: {editor.get_text()}")
# editor.restore(save_point)
# print(f"After Undo: {editor.get_text()}")
    
    
#Q4
# class Stock: # Subject
#     def __init__(self, symbol, price):
#         self.symbol = symbol
#         self.price = price
#         self.chart_display = ChartDisplay() # Tightly coupled observer
#         self.ticker_display = TickerDisplay() # Tightly coupled observer

#     def set_price(self, price):
#         self.price = price
#         self.chart_display.update(self.symbol, self.price)
#         self.ticker_display.update(self.symbol, self.price)

# class ChartDisplay: # Observer 1
#     def update(self, symbol, price):
#         print(f"Chart: {symbol} is now ${price}")

# class TickerDisplay: # Observer 2
#     def update(self, symbol, price):
#         print(f"Ticker: {symbol} @ ${price}")

# # Client
# stock_apple = Stock("AAPL", 150)
# stock_apple.set_price(155)

# # Answer4:
# class Observer:
#     def update(self , price):
#         pass
# class ChartDisplay(Observer):
#     def update(self,price):
#         print(f"Chart: Stock price updated to ${price}")
# class TickerDisplay(Observer):
#     def update(self, price):
#         print(f"Ticker: Stock price updated to ${price}")
# class price:
#     def __init__ (self):
#         self.observers = []
#         self.price = 0
#     def attach(self, observer):
#         self.observers.append(observer)
#     def notify_all(self):
#         for observer in self.observers:
#             observer.update(self.price)
#     def set_price(self, price):
#         self.price = price
#         self.notify_all()
# # # Client
# stock = price()
# stock.attach(ChartDisplay())
# stock.attach(TickerDisplay())
# stock.set_price(100)


#Q5
# class OldPaymentGateway:
#     def submit_payment_details(self, card_number, expiry, amount_val):
#         print(f"OldGateway: Processing ${amount_val} for card {card_number}")
#         return True

# class NewSystemClient:
#     def process_order(self, card_no, card_exp_date, total_amount):
#         # Needs to use OldPaymentGateway, but interfaces don't match
#         # Client might try to directly call and map:
#         opg = OldPaymentGateway()
#         success = opg.submit_payment_details(card_no, card_exp_date, total_amount)
#         if success:
#             print("NewSystemClient: Payment successful via old gateway.")
#         else:
#             print("NewSystemClient: Payment failed via old gateway.")

# # Client
# client = NewSystemClient()
# client.process_order("1234-5678-9012-3456", "12/25", 100.50)

# Answer5:
# class OldPaymentGateway:
#     def submit_payment(self, card_number, expiry, amount_val):
#         return f"Payment processed with OldGateway: Card: {card_number}, Expiry: {expiry}, Amount: {amount_val}"

# class PaymentAdapter:
#     def __init__(self, socket):
#         self.socket = socket
        
#     def submit_payment(self, card_number, expiry, amount_val):
#         # Forward the payment details to the OldPaymentGateway
#         return self.socket.submit_payment(card_number, expiry, amount_val).replace("OldGateway", "NewSystem")

# # Usage example
# old_gateway = OldPaymentGateway()
# new_adapter = PaymentAdapter(old_gateway)

# # This will now work correctly
# result = new_adapter.submit_payment("1234-5678-9012-3456", "12/25", 100.50)
# print(result)

#Q6
# class Computer:
#     def __init__(self, case, mainboard, cpu, ram_gb, storage_gb, gpu=None):
#         self.case = case
#         self.mainboard = mainboard
#         self.cpu = cpu
#         self.ram_gb = ram_gb
#         self.storage_gb = storage_gb
#         self.gpu = gpu
#         print("Computer created with complex constructor.")

# # Client creating different configurations
# gaming_pc = Computer("Tower", "ATX", "i9", 32, 1000, "RTX4080")
# office_pc = Computer("Mini-Tower", "Micro-ATX", "i5", 16, 500, None)
# # Many optional parameters, constructor can become very long.

# Answer6:
# class Computer:
#     def __init__(self):
#         self.case =  None
#         self.mainboard = None
#         self.cpu = None
#         self.ram_gb = None
#         self.storage_gb = None
#         self.gpu = None
#     def __str__ (self):
#         return f"Computer with {self.case}, {self.mainboard}, {self.cpu}, {self.ram_gb}GB RAM, {self.storage_gb}GB Storage, GPU: {self.gpu}"
# class ComputerBuilder:
#     def __init__ (self):
#         self.computer = Computer()
#     def add_case(self, case):
#         self.computer.case = case
#         return self
#     def add_mainboard(self, mainboard):
#         self.computer.mainboard = mainboard
#         return self
#     def add_cpu(self, cpu):
#         self.computer.cpu = cpu
#         return self
#     def add_ram(self, ram_gb):
#         self.computer.ram_gb = ram_gb
#         return self
#     def add_storage(self, storage_gb):
#         self.computer.storage_gb = storage_gb
#         return self
#     def add_gpu(self, gpu):
#         self.computer.gpu = gpu
#         return self
#     def build(self):
#         return self.computer
# builder = ComputerBuilder()
# pc = builder.add_case("Tower").add_mainboard("ATX").add_cpu("i9").add_ram(32).add_storage(1000).add_gpu("RTX4080").build()
# print(pc)  
    
#Q7
# class VideoConverter:
#     def convert_to_mp4(self, video_file): print(f"Converting {video_file} to MP4")
#     def convert_to_avi(self, video_file): print(f"Converting {video_file} to AVI")
#     def add_watermark(self, video_file): print(f"Adding watermark to {video_file}")
#     def resize_video(self, video_file, resolution): print(f"Resizing {video_file} to {resolution}")


# # Answer7:
# class Facade:
#     def __init__(self):
#         self.converter = VideoConverter()
    
#     def convert_video(self, video_file, format_type):
#         if format_type == "mp4":
#             self.converter.convert_to_mp4(video_file)
#         elif format_type == "avi":
#             self.converter.convert_to_avi(video_file)
#         else:
#             raise ValueError("Unsupported format")
    
#     def process_video(self, video_file, resolution):
#         self.converter.add_watermark(video_file)
#         self.converter.resize_video(video_file, resolution)
# video = Facade()
# video.convert_video("input.mov", "mp4")
# video.process_video("input_mp4_version.mp4", "720p")
    
# ======================================================================== End of Design Patterns =====================================================================================


# class Projector :
#     def on (self):
#         print("Projector is ON")
#     def off (self):
#         print("Projector is OFF")
# class Soundsystem:
#     def on (self):
#         print("Sound system is ON")
#     def off (self):
#         print("Sound system is OFF")
# class DVDPlayer:
#     def on (self):
#         print("DVD Player is ON")
#     def off (self):
#         print("DVD Player is OFF")
# class Facade:
#     def __init__ (self):
#         self.projector = Projector()
#         self.soundsystem = Soundsystem()
#         self.dvdplayer = DVDPlayer()
#     def watch_movie(self):
#         self.projector.on()
#         self.soundsystem.on()
#         self.dvdplayer.on()
#     def stop_movie(self):
#         self.projector.off()
#         self.soundsystem.off()
#         self.dvdplayer.off()
# movie = Facade()
# movie.watch_movie()
# movie.stop_movie()



# class Handler:
#     def __init__(self , success = None):
#         self.successor = success
#     def handle(self , request):
#         if self.successor:
#             self.successor.handle(request)
#         else:
#             print("error")
# class ConcreteHandlerA(Handler):
#     def handle(self, request):
#         if request == "A":
#             print("Handle A")
#         else:
#             super().handle(request)
# class ConverterHandlerB(Handler):
#     def handle(self , request):
#         if request == "B":
#             print("Handle B")
#         else:
#             super().handle(request)
# handle_a = ConcreteHandlerA()
# handle_b = ConverterHandlerB()
# handle_a.successor = handle_b
# handle_a.handle("A")
# handle_a.handle("B")
# handle_a.handle("C")


# class Memento:
#     def __init__(self , state):
#         self.state = state
#     def get_state(self):
#         return self.state
# class Originator:
#     def __init__(self):
#         self.state = ""
#     def write_state(self , state):
#         self.state += state
#     def create_memento(self):
#         return Memento(self.state)
#     def restore(self , memento):
#         self.state = memento.get_state()
#     def get_state (self):
#         return self.state
# originator = Originator()
# originator.write_state("state1")
# save_point = originator.create_memento()
# originator.write_state("state2")
# print(originator.get_state())
# originator.restore(save_point)
# print(originator.get_state())


# class observer:
#     def update(self):
#         pass
# class subject:
#     def __init__(self):
#         self.observers = []
#         self.message = ""
#     def attach(self, observer):
#         self.observers.append(observer)
#     def notify_all(self):
#         for observer in self.observers:
#             observer.update(self.message)
#     def set_message(self, message):
#         self.message = message
#         self.notify_all
# message = subject()
# message.attach(observer())
# message.set_message("Hello, Observers!")
# print(message.message)


# class EuropeanSocket:
#     def Voltage(self):
#         return "230"
# class AmericanDevice:
#     def Voltage(self):
#         return "120"
# class Adapter:
#     def __init__(self , socket):
#         self.socket = socket
#     def Voltage(self):
#         return self.socket.Voltage().replace("230", "120")
# european = EuropeanSocket()
# us_adapter = Adapter(european)
# print(us_adapter.Voltage())  


