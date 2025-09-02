#Multithearding 
# import threading
# import time
# def print_number ():
#     for i in range (5):
#         print(f"Number : {i}")
#         time.sleep(2)
# def print_letter ():
#     for letter in "ABDALLAH":
#         print(f"Letter : {letter}")
#         time.sleep(2)
# thread1 = threading.Thread(target=print_number())
# thread2 = threading.Thread(target=print_letter())
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("Done!")


# using Lock 
# import threading
# import time
# lock = threading.Lock()
# def print_number ():
#     for i in range (5):
#         with lock : 
#             print(f"Number : {i}")
#             time.sleep(2)
# def print_letter ():
#     for letter in "ABDALLAH":
#         with lock :
#             print(f"Letter : {letter}")
#             time.sleep(2)
# thread1 = threading.Thread(target=print_number())
# thread2 = threading.Thread(target=print_letter())
# thread1.start()
# thread2.start()
# print("Done!")

