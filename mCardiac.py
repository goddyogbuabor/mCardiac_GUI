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

window = tk.Tk(className='MCardiac Application')
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

def importFile():
    filename = filedialog.askopenfilename(initialdir ="/", title ="Import File", filetypes=(("CSV file", ".csv"),("All files","*.*")))
 
def save(): 
    files = [('All Files', '*.*'),  
             ('CSV Files', '*.csv'), 
             ('Text Document', '*.txt')] 
    file = asksaveasfile(filetypes = files, defaultextension = files)  
    
def search_activity(start_date,end_date):
    dataDir ='../mCardiac_GUI/'
    dataset = pd.read_csv(dataDir+'ActivityData.csv')
    
    df = dataset[(dataset['timestamp'] >start_date) & (dataset['timestamp'] <= end_date)]
    ax = plt.axes()
    ax = sns.scatterplot(x='timestamp', y='Activity', hue='Activity', data=df, legend=False)
    ax.xaxis.set_minor_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
    ax.xaxis.set_minor_locator(mdates.MinuteLocator())
    ax.xaxis.set_major_locator(plt.MaxNLocator(20))
    plt.gcf().autofmt_xdate()
    plt.show()
                
def TrainAlgorithm():
     
    extractF = Feature_extraction()
    extractF.train_feature()
    clf = Classification()
    clf.train_algorithm()
    messagebox.showinfo("Success", "Algorithm Trained Successfully")
     
def ClassifyActivity():
    extract = Feature_extraction()
    extract.Classify_feature()
    clf = Classification()
    clf.classify()
    
    messagebox.showinfo("Success", "Activity Classified Successfully")
    
def send_msg():
    clf = Classification()
    clf.send_message()
    messagebox.showinfo("Success", "Message Sent Successfully")  

def plotView():
    clf = Classification()
    clf.view_activity()
   

#Create Menu
menubar =Menu(window, background='red', foreground='black', activebackground='white', activeforeground='black') 
window.config(menu=menubar)

#create menu item
fileMenu =Menu(menubar)
menubar.add_cascade(label="MainMenu", menu=fileMenu)
fileMenu.add_command(label="View Actiivity Details", command=plotView)
fileMenu.add_command(label="Exit", command=window.quit)

#create heading  
lblheading = Label(window, text="Cardiac Condition Monitoring", fg="red", font=("Helvetica", 18))
lblheading.pack(pady=8)

button2 = Button(window, text='Train Algorithm', command =TrainAlgorithm,height=2, width =40, justify=LEFT, padx=2)
button2.pack(pady=8)

button3 = Button(window, text='Classification',command =ClassifyActivity, height=2, width =40, justify=LEFT, padx=2)
button3.pack(pady=8)

#button4 = Button(window, text='View Activity Details',command =plotView, height=2, width =40, justify=LEFT, padx=1)
#button4.pack(pady=3)

def display():
    start = var.get() 
    end =  var2.get()
    search_activity(start,end)
   

var = tk.StringVar()
var2 = tk.StringVar()


lblsearch = Label(window, text="Please Enter Start and End Date", fg="red",  font=("Helvetica", 10))
lblsearch.pack()

lblstart = Label(window, text="Start Date", fg="black",  font=("Helvetica", 14))
lblstart.pack()

txtstart = tk.Entry(window,textvariable=var)
txtstart.pack(pady=2)
Label(window, text="(yyyy-mm-dd HH:MM:SS)").pack(pady=5)

lblend = Label(window, text="End Date", fg="black",  font=("Helvetica", 14))
lblend.pack()
txtend = tk.Entry(window, textvariable=var2)
txtend.pack(pady=5)

button5 = Button(window, text='Search for Activities',command =display, height=2, width =25, justify=LEFT, padx=1)
button5.pack(pady=3)

window.mainloop()   