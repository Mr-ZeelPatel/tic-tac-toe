from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

db=sqlite3.connect('tictactoe.db')
cursor=db.cursor()
cursor.execute('create table match_data (player1 Text,player2 Text,winner Text)')
def ins_data(p1,p2,win):
    cursor.execute('insert into match_data(player1,player2,winner) values(?,?,?)',(p1,p2,win))
    db.commit()


    
    

root=Tk()

root.geometry("940x320")

pl1=simpledialog.askstring("Player name","Enter player 1 name")
pl2=simpledialog.askstring("Player name","Enter player 2 name")
tree=ttk.Treeview(root)
tree.place(x="520",y="60")
tree['columns']=("Player 1","Player 2","Winner")
tree.column("#0", width=0, minwidth=0)
tree.column("Player 1", width=130)
tree.column("Player 2", width=130)
tree.column("Winner", width=130)
tree.heading("Player 1", text="Player 1")
tree.heading("Player 2", text="Player 2")
tree.heading("Winner", text="Winner")
scroll=ttk.Scrollbar(root,orient='vertical',command=tree.yview)
scroll.place(x="915",y="60",height="170px")

root.title('Tic Tac Toe : {}\'s turn'.format(pl1))
ans=None
activePlayer=1
p1=[]
p2=[]

def win():
    winner=-1
    if ((1 in p1) and (2 in p1) and (3 in p1)):
        winner=1
        ins_data(pl1,pl2,pl1)
    if ((1 in p2) and (2 in p2) and (3 in p2)):
        winner=2
        ins_data(pl1,pl2,pl2)

    
    if ((4 in p1) and (5 in p1) and (6 in p1)):
        winner=1
        ins_data(pl1,pl2,pl1)
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        winner=2
        ins_data(pl1,pl2,pl2)
        
   
    if ((7 in p1) and (8 in p1) and (9 in p1)):
        winner=1
        ins_data(pl1,pl2,pl1)
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        winner=2
        ins_data(pl1,pl2,pl2)
    
    
    
    if ((1 in p1) and (4 in p1) and (7 in p1)):
        winner=1
        ins_data(pl1,pl2,pl1)
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        winner=2
        ins_data(pl1,pl2,pl2)


    if ((2 in p1) and (5 in p1) and (8 in p1)):
        winner=1
        ins_data(pl1,pl2,pl1)
    if ((2 in p2) and (5 in p2) and (8 in p2)):
        winner=2
        ins_data(pl1,pl2,pl2)
    
    
    
    if ((3 in p1) and (6 in p1) and (9 in p1)):
        winner=1
        ins_data(pl1,pl2,pl1)
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        winner=2
        ins_data(pl1,pl2,pl2)
    
    
    
    if ((1 in p1) and (5 in p1) and (9 in p1)):
        winner=1
        ins_data(pl1,pl2,pl1)
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        winner=2
        ins_data(pl1,pl2,pl2)
        
        
    if ((3 in p1) and (5 in p1) and (7 in p1)):
        winner=1
        ins_data(pl1,pl2,pl1)
    if ((3 in p2) and (5 in p2) and (7 in p2)):
        winner=2
        ins_data(pl1,pl2,pl2)

    
        
    if winner==1:
        messagebox.showinfo('Result','Congrats, {} has won the game'.format(pl1))
        ans=messagebox.askquestion("Exit","Do you want to play again?")
        
    
    elif winner==2:
        messagebox.showinfo('Result','Congrats, {} has won the game'.format(pl2))
        ans=messagebox.askquestion("Exit","Do you want to play again?")
    
    if((len(p1)==5 or len(p2)==5) and winner==-1):
        messagebox.showinfo('Result','Match tie!!!')
        ins_data(pl1,pl2,"tie")
        ans=messagebox.askquestion("Exit","Do you want to play again?")
    
    if(ans=='yes'):
        b1.config(text="")
        b1.config(state="normal")
        b2.config(text="")
        b2.config(state="normal")
        b3.config(text="")
        b3.config(state="normal")
        b4.config(text="")
        b4.config(state="normal")
        b5.config(text="")
        b5.config(state="normal")
        b6.config(text="")
        b6.config(state="normal")
        b7.config(text="")
        b7.config(state="normal")
        b8.config(text="")
        b8.config(state="normal")
        b9.config(text="")
        b9.config(state="normal")
        p1.clear()
        p2.clear()   
        
    elif(ans=='no'):
        db.close()
        root.destroy()
def setLayout(id,symbol):
    if id==1:
        b1.config(text=symbol)
        b1.state(['disabled'])
    
    if id==2:
        b2.config(text=symbol)
        b2.state(['disabled'])
        
    if id==3:
        b3.config(text=symbol)
        b3.state(['disabled'])
    
    if id==4:
        b4.config(text=symbol)
        b4.state(['disabled'])
    
    if id==5:
        b5.config(text=symbol)
        b5.state(['disabled'])

    if id==6:
        b6.config(text=symbol)
        b6.state(['disabled'])
    
    if id==7:
        b7.config(text=symbol)
        b7.state(['disabled'])
    
    if id==8:
        b8.config(text=symbol)
        b8.state(['disabled'])
    
    if id==9:
        b9.config(text=symbol)
        b9.state(['disabled'])


def button_Click(id):
    global activePlayer
    global p1
    global p2
    if (activePlayer==1):
        setLayout(id,"X")
        p1.append(id)
        activePlayer=2
        root.title('Tic Tac Toe : {}\'s turn'.format(pl2))
        print("P1:{}".format(p1))
        
    
    elif (activePlayer==2):
        setLayout(id,"O")
        p2.append(id)
        activePlayer=1
        root.title('Tic Tac Toe : {}\'s turn'.format(pl1))
        print("P2:{}".format(p2))

    win()
    




b1=ttk.Button(root,text="  ")
b1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
b1.config(command=lambda:button_Click(1))



b2=ttk.Button(root,text="  ")
b2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
b2.config(command=lambda:button_Click(2))

b3=ttk.Button(root,text="  ")
b3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
b3.config(command=lambda:button_Click(3))

b4=ttk.Button(root,text="  ")
b4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
b4.config(command=lambda:button_Click(4))

b5=ttk.Button(root,text="  ")
b5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
b5.config(command=lambda:button_Click(5))

b6=ttk.Button(root,text="  ")
b6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
b6.config(command=lambda:button_Click(6))

b7=ttk.Button(root,text="  ")
b7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
b7.config(command=lambda:button_Click(7))

b8=ttk.Button(root,text="  ")
b8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
b8.config(command=lambda:button_Click(8))

b9=ttk.Button(root,text="  ")
b9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
b9.config(command=lambda:button_Click(9))

def get_data(name):
    try:
        tree.delete(*tree.get_children())
        cursor.execute('select * from match_data where player1=? OR player2=?',(name,name))
        data=cursor.fetchall()
        for i in data:
            if (i):
                tree.insert('','end',values=(i[0],i[1],i[2]))
            else:
                print('No data found')
    except:
        print('Error')

def btnclick():
    n=etr.get()
    get_data(n)
    
lbl=Label(root,text='Name')
lbl.place(relx=0.6,rely=0.04,anchor=NE)
etr=Entry(root)
etr.place(relx=0.65,rely=0.04)
fetch=ttk.Button(root,text="Fetch data",command=lambda:btnclick())
fetch.place(relx=0.80,rely=0.04)
root.mainloop()
