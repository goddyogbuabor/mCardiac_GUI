from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from recognition import Classification
from feature_extract import Feature_extraction
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math
import os
from tkinter.filedialog import asksaveasfile
from functools import partial
from tkcalendar import*

window = tk.Tk(className='Personalised Recommendations')
my_string_var = tk.StringVar()

def center_window(w=300, h=300):
    # get screen width and height
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
center_window(600, 450) 

def send_message():
        import smtplib, ssl

        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = ""
        receiver_email = ""
        #password = input("Enter Password: ")
        password = ""
       
        message = """\
        Subject: Recommendation

        Please do more of walking for 30 minutes"""

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
            server = smtplib.SMTP(smtp_server,port)
            server.starttls(context=context) # Secure the connection
            server.login(sender_email, password)
            #Send email here
            server.sendmail(sender_email, receiver_email, message)
        except Exception as e:
            # Print any error messages 
            print(e)
        finally:
            server.quit() 
            
var = tk.StringVar()
var2 = tk.StringVar()

lblstart = Label(window, text="Patient Email:", fg="red",  font=("Helvetica", 12))
lblstart.pack()

txtstart = tk.Entry(window,textvariable=var, width =30)
txtstart.pack(pady=8)
   
   
lblheading = Label(window, text="Please enter recommendation for patient", fg="red", font=("Helvetica", 12))
lblheading.pack(pady=8)   
            
textmessage = Text(window, height = 7, width =40)
textmessage.pack(pady=3)

msg = Button(window, text='Send Message',command =send_message, height=2, width =20, justify=LEFT, padx=1)
msg.pack(pady=3)


window.mainloop() 