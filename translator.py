#use internet
from googletrans import Translator
import pyttsx3
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
root.title("Translator-Any language to English")

#defining variable
en = tk.StringVar()

#making GUI
label = tk.Label(root,text="Enter Text:").grid(row=0, column=0)
entry = tk.Entry(root,textvariable=en).grid(row=0, column=1,ipady=10,ipadx=200)

#function
def trans():
    global speech
    x=en.get()
    translator = Translator()
    trans = translator.translate(x)
    speech = trans.text
    TA.insert('end',speech)
    
def speak():
    engine = pyttsx3.init()
    engine.say(speech)
    engine.runAndWait()
    
    
#button
Tr=tk.Button(root,text="Translate",fg="green",command=trans).grid(row=1,column=0,padx=10,pady=10)
sp=tk.Button(root,text="Speak",fg="blue",command=speak).grid(row=1,column=1,padx=10,pady=10)

#textarea
TA= tk.Text(root,height=20,width=30)
TA.grid(row=2,column=0,padx=10,pady=10)


    
root.mainloop()