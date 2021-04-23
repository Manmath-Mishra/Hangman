from tkinter import *;PhotoImage 
import random
from tkinter import messagebox
import time
chances=5
def click(event):
    global status,words,choice,z,find,chances,num
    text= str(event.widget.cget("text"))
    
    if text in choice:
        status.set("letter already present")
        correct.update()
    elif text in z:
        index= z.index(text) 
        del choice[index] 
        choice.insert(index,text)
        wording.config(text=choice)
        wording.update()
        status.set("Correct guess!!!")
        correct.update()
        if choice.count("_")==0:
            status.set("Congrats !!!")
            correct.update()
            gmail=PhotoImage(file=r"C:\Users\RAHUL\Downloads\Inkedsaved man_LI.png")
            lab=Label(image=gmail)
            lab.photo=gmail
            lab.place(x=200,y=205)
            messagebox.showinfo("Result","YOU SAVED THE MAN!!")
            time.sleep(2)
            root.destroy()
    else:
        status.set(f"Try again! chances left:{chances-1}")
        correct.update()
        chances-=1
        if chances==0:
            status.set(f"Correct word: {z}")
            correct.update()
            gmail=PhotoImage(file=r"C:\Users\RAHUL\Downloads\hanged final.png")
            lab=Label(image=gmail)
            lab.photo=gmail
            lab.place(x=165,y=164)
            messagebox.showinfo("Result","YOU MURDERED THE MAN!!")
            time.sleep(2)
            root.destroy()



root= Tk()
root.geometry("600x570")
root.title("HANGMAN 2.0")
root.resizable(0,0)
root.config(bg="green")
header=Label(root,text="HANGMAN",font="algerian 20 bold",fg="red",relief=SUNKEN)
header.pack(fill=BOTH)
f1= Frame(root,borderwidth=3,bg="green")
f1.place(y=70)
A= Button(f1,text="A",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f1,text="B",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f1,text="C",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f1,text="D",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f1,text="E",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f1,text="F",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f1,text="G",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f1,text="H",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f1,text="I",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f1,text="J",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f1,text="K",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f1,text="L",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f1,text="M",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)

#Row 2 starts

f2= Frame(root,borderwidth=3,bg="green")
f2.place(y=110)
A= Button(f2,text="N",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f2,text="O",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f2,text="P",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f2,text="Q",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f2,text="R",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f2,text="S",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f2,text="T",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f2,text="U",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f2,text="V",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f2,text="W",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f2,text="X",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f2,text="Y",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
A= Button(f2,text="Z",bg="yellow",padx=7,pady=4)
A.pack(side=LEFT,padx=7)
A.bind("<Button-1>",click)
#Buttons end

#List operations
words= ["DIFFICULT","OUTSTANDING","SUFFRAGE","ZOOLOGIST","BOTANIST","EXPERIENCE"]
find= [["_","I","F","F","I","_","_","_","_"],["_","_","T","_","T","_","N","D","_","N","_"],["S","_","F","F","_","_","_","E"],["_","O","O","_","O","_","_","S","_"],["_","O","T","_","_","I","_","T"],["E","_","_","E","_","_","E","N","_","E"]]
choice= random.choice(find)
num=find.index(choice)
z= words[num]

#status and labelling starts

l1= Label(root,text="Word :-",fg="blue",font="algerian 20 bold",bg="green")
l1.place(y=450,x=110)
wording= Label(root,fg="red",text=choice,font="algerian 20 bold",bg="green")

wording.place(y=450,x=230)
stat=Label(root,text="STATUS :",fg="yellow",font="algerian 18 bold",bg="green")
stat.place(y=499,x=60)
status= StringVar()
correct= Entry(root,textvariable=status,font="algerian 18")
correct.place(y=499,x=200,width=350)

root.mainloop()