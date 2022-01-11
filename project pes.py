'''
from tkinter import *
from Pillow import ImageTk,Image
import math

board=Tk()
board.title("N-Queens Problem")

buttons={}
a=[]
nq=0
Q={}
img={}
resized={}
my_img={}

def makeGrid(n):
    b=[]
    for i in range(n):
        b.append(1)
    for i in range(n):
        a.append(b)

def onPressed(s,x,y):
    global nq
    buttons[s*x+y+1].destroy()
    img[nq] = Image.open("D:/ALSTON/comp_project/black_queen.png")
    resized[nq] = img[nq].resize((40,50), Image.ANTIALIAS)
    my_img[nq]=ImageTk.PhotoImage(resized[nq])
    Q[nq]=Label(board,image=my_img[nq])
    Q[nq].grid(row=x,column=y)
    if(nq<s):
        if(a[x][y]==1):
            nq+=1
            for i in range(len(a)):
                for j in range(len(a)):
                    if(i==x or j==y or math.fabs(i-x)==math.fabs(j-y)):
                        t=[]
                        for k in range(len(a[i])):
                            if(k==j):
                                t.append(0)
                            else:
                                t.append(a[i][k])
                        a[i]=t
                    if(i==x and j==y):
                        a[i][j]=2
        if(a[x][y]==0):
            print("You Lose")
            #TODO:Code to display alert for losing
            nq=s+1
    if(nq==s):
        print("You win")
        #TODO:Code to display alert for winning

def start():
    s=int(size.get()[16:])
    if(s>3):
        makeGrid(s)
        startButton.destroy()
        size.destroy()
        createBoard(s)
    else:
        pass
        #TODO:Code to display alert for invalid size

def createButton(color,x,y,s):
    buttons[s*x+y+1]=Button(board,bg=color,height=4,width=7,command=lambda: onPressed(s,x,y))
    buttons[s*x+y+1].grid(row=x,column=y)
    
    
def createBoard(n):
    for i in range(n):
        for j in range(n):
            if((i+j)%2==0):
                createButton("black",i,j,n)
            else:
                createButton("white",i,j,n)
                
size=Entry(board,width=20,border=5)
size.pack()
size.insert(0,"Enter grid size:")

startButton=Button(board,text="START!!!",command=start,fg="white",bg="red")
startButton.pack()

board.mainloop()
'''
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk , Image
import math

board=Tk()
board.title("N-Queens Problem")

buttons={}
a=[]
nq=0
Q={}
img={}
resized={}
my_img={}
root=Tk()
root.geometry("300x200")

def makeGrid(n):
    b=[]
    for i in range(n):
        b.append(1)
    for i in range(n):
        a.append(b)

def onPressed(s,x,y):
    global nq
    buttons[s*x+y+1].destroy()
    img[nq] = Image.open("D:/ALSTON/comp_project/black_queen.png")
    resized[nq] = img[nq].resize((40,50), Image.ANTIALIAS)
    my_img[nq]=ImageTk.PhotoImage(resized[nq])
    Q[nq]=Label(board,image=my_img[nq])
    Q[nq].grid(row=x,column=y)
    if(nq<s):
        if(a[x][y]==1):
            nq+=1
            for i in range(len(a)):
                for j in range(len(a)):
                    if(i==x or j==y or math.fabs(i-x)==math.fabs(j-y)):
                        t=[]
                        for k in range(len(a[i])):
                            if(k==j):
                                t.append(0)
                            else:
                                t.append(a[i][k])
                        a[i]=t
                    if(i==x and j==y):
                        a[i][j]=2
        if(a[x][y]==0):
            messagebox.showwarning("Ohh NOOO !!!", "You were spo close to winning . Its OK, you can try again. Hope to see you soon. ")
            
            nq=s+1
    if(nq==s):
        messagebox.showinfo("Congratulations !!!!", "Very well played, You are indeed an expert in chess. Hope to play with you again, Next time you will lose.")

def start():
    s=int(size.get()[16:])
    if(s>3):
        makeGrid(s)
        startButton.destroy()
        size.destroy()
        createBoard(s)
    else:
        messagebox.showerror("Invalid size","The entered grid size is invalid.Please enter a valid grid size")

def createButton(color,x,y,s):
    buttons[s*x+y+1]=Button(board,bg=color,height=4,width=7,command=lambda: onPressed(s,x,y))
    buttons[s*x+y+1].grid(row=x,column=y)
    
    
def createBoard(n):
    for i in range(n):
        for j in range(n):
            if((i+j)%2==0):
                createButton("black",i,j,n)
            else:
                createButton("white",i,j,n)
                
size=Entry(board,width=20,border=5)
size.pack()
size.insert(0,"Enter grid size:")

startButton=Button(board,text="START!!!",command=start,fg="white",bg="red")
startButton.pack()

board.mainloop()
