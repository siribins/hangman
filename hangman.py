import tkinter as tk
from tkinter import *
import tkinter.font as font
import csv
import random
from PIL import ImageTk, Image
word=None
Letter=None
letter=None
count=0


def easy():
        global word
        f=open("Words1.csv",'r')
        reader=csv.reader(f)
        wrds= list(reader)
        length=len(wrds)
        val=random.randrange(1,length-1)
        word=wrds[val][0]
        word=word.upper()
        func1()
        window.mainloop()
        

def medium():
        global word
        global guess
        f=open("Words1.csv",'r')
        reader=csv.reader(f)
        wrds= list(reader)
        length=len(wrds)
        val=random.randrange(1,length-1)
        word=wrds[val][1]
        word=word.upper()
        func1()
        window.mainloop()
        

def difficult():
        global word
        f=open("Words1.csv",'r')
        reader=csv.reader(f)
        wrds= list(reader)
        length=len(wrds)
        val=random.randrange(1,length-1)
        word=wrds[val][2]
        word=word.upper()
        func1()
        window.mainloop()
        
  
def submit():
    
        global window, Letter
        global guess
        global wrong, correct
        global count

        if count==0:
            if len(Letter.get())!=1:
                count=0
        elif Letter.get().isdigit():
            count=0
        elif Letter.get()==" ":
            count=0
        elif Letter.get().isalpha()==False:
            count=0
        else:    
            if len(Letter.get())!=1:
                count-=1
            elif Letter.get().isdigit():
                count-=1
            elif Letter.get()==" ":
                count-=1
            elif Letter.get().isalpha()==False:
                count-=1

        b='_'
        if Letter.get().upper() in ('A','E','I','O','U'):
                L=tk.Label(window, text=("NO VOWELS PLEASE"),font=("Ebrima", 15)).place(x=100, y=450)
            
        elif Letter.get().upper() in word:
                b=''
                L2=tk.Label(window, text='      CORRECT!!                    ',font=("Ebrima", 15)).place(x=100, y=450)
                correct.append(Letter.get().upper())
                for i in word:
                    if i in ('A','E','I','O','U') or i in correct:
                        b+=i
                    else:
                        b+=" _"
                L1=tk.Label(window, text=b,font=("Ebrima", 15)).place(x=100, y=200)
                wrong.append(Letter.get().upper())
                L=tk.Label(window, text="LETTERS GUESSED SO FAR: ",font=("Ebrima", 15)).place(x=100, y=600)
                L2=tk.Label(window, text=wrong ,font=("Ebrima", 15)).place(x=400, y=600)
                
        else:
                if Letter.get().upper() in wrong or Letter.get().upper() in correct:
                    L=tk.Label(window, text=("LETTER ALREADY TRIED"),font=("Ebrima", 15)).place(x=100, y=450)
                else:
                    count+=1
                    wrong.append(Letter.get().upper())
                    L2=tk.Label(window, text='       INCORRECT                ',font=("Ebrima", 15)).place(x=100, y=450)
                    L=tk.Label(window, text="LETTERS GUESSED SO FAR: ",font=("Ebrima", 15)).place(x=100, y=600)
                    L2=tk.Label(window, text=wrong ,font=("Ebrima", 15)).place(x=400, y=600)
                    for i in word:
                        if i in ('A','E','I','O','U') or i in correct:
                            b+=i
                        else:
                            b+=" _"

        if b.count("_")==0:
                    window.destroy()
                    win = tk.Tk()
                    win.title("VICTORY")
                    win.geometry('400x400')
                    image1 = Image.open("image0.png")
                    test=ImageTk.PhotoImage(image1)

                    label1= tk.Label(image=test)
                    label1.image=test

                    label1.place(x=0, y=0)
                    L2=tk.Label(win, text='YOU WIN!!',font=("Ebrima", 15)).place(x=100, y=100)
                    L2=tk.Label(win, text='THE WORD IS:',font=("Ebrima", 15)).place(x=100, y=150)
                    L2=tk.Label(win, text=word,font=("Ebrima", 15)).place(x=100, y=200)
                    
                    
        if count==1:
                image1 = Image.open("hm2.png")
                test=ImageTk.PhotoImage(image1)

                label1= tk.Label(image=test)
                label1.image=test

                label1.place(x=350, y=200)
                            
        elif count==2:       
                image1 = Image.open("hm3.png")
                test=ImageTk.PhotoImage(image1)

                label1= tk.Label(image=test)
                label1.image=test

                label1.place(x=350, y=200)
                
        elif count==3:                        
                image1 = Image.open("hm4.png")
                test=ImageTk.PhotoImage(image1)

                label1= tk.Label(image=test)
                label1.image=test

                label1.place(x=350, y=200)
                
        elif count==4:
                image1 = Image.open("hm5.png")
                test=ImageTk.PhotoImage(image1)

                label1= tk.Label(image=test)
                label1.image=test

                label1.place(x=350, y=200)
                
        elif count==5:                     
                image1 = Image.open("hm6.png")
                test=ImageTk.PhotoImage(image1)

                label1= tk.Label(image=test)
                label1.image=test

                label1.place(x=350, y=200)
                
        elif count==6:
                image1 = Image.open("hm7.png")
                test=ImageTk.PhotoImage(image1)

                label1= tk.Label(image=test)
                label1.image=test

                label1.place(x=350, y=200)

                window.destroy()

                win = tk.Tk()
                win.title("DEFEAT")
                win.geometry('400x400')
                image1 = Image.open("image0.png")
                test=ImageTk.PhotoImage(image1)

                label1= tk.Label(image=test)
                label1.image=test

                label1.place(x=0, y=0)
                L4=tk.Label(win, text=("YOU LOSE! THE WORD WAS: "),font=("Ebrima", 15))
                L4.place(x=50,y=100)
                L5=tk.Label(win, text=word,font=("Ebrima", 15)).place(x=50, y=150)
                


def func1():
            global Letter
            global guess
            global wrong, correct
            global count
            a=''
            for i in word:
                if i in ('A','E','I','O','U'):
                    a+=i
                else:
                    a+=' _'
            L1=tk.Label(window, text=a,
            font=("Ebrima", 15)).place(
            x=100, y=200) 

            wrong=[]
            correct=[]
            
            L2=tk.Label(window, text='ENTER A LETTER:',font=("Ebrima", 15)).place(x=100, y=300)

            Letter = StringVar(window,value='')
            LetterEntry = tk.Entry(window, textvariable=Letter).place(x=100, y=350)
            guess=Letter.get()
            Letterbutton = tk.Button(window, text="SUBMIT", font=("Ebrima", 10), command=submit).place(x=100, y=400)
            image1 = Image.open("hm1.png")
            test=ImageTk.PhotoImage(image1)

            label1= tk.Label(image=test)
            label1.image=test

            label1.place(x=350, y=200)
            
        
        
            

        
window = tk.Tk()
window.title("HANGMAN")
window.geometry('700x700')

image1 = Image.open("image0.png")
test=ImageTk.PhotoImage(image1)

label1= tk.Label(image=test)
label1.image=test

label1.place(x=0, y=0)
  
tk.Label(window, text="Select difficulty:",
          font=("Ebrima", 15)).place(
   x=100, y=25)

myFont = font.Font(family='Ebrima')

Buttoneasy = Button(window, text="EASY", command=easy )
Buttoneasy['font']=myFont
Buttoneasy.place(x=50, y=100)

Buttonmedium = Button(window, text="MEDIUM", command=medium)
Buttonmedium['font']=myFont
Buttonmedium.place(x=150, y=100)

Buttonhard = Button(window, text="DIFFICULT", command=difficult)
Buttonhard['font']=myFont
Buttonhard.place(x=300, y=100)
  
window.mainloop()

