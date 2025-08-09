from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3
class reportclass:
    def __init__(self, root):
        self.root = root
        self.root.title("student result management system")
        self.root.geometry("1200x480+80+170")
        self.root.config(background="white")
        self.root.focus_force()


        title = Label(self.root, text="view student results",padx=10,compound=LEFT, font=("goudy old style", 20, "bold"), bg="orange", fg="#262626").place(x=10,y=15,width=1180,height=50)

        self.var_search=StringVar()
        lbl_search=Label(self.root,text="search by roll no",font=("goudy old style",20,"bold"),bg="white").place(x=280,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",20),bg="lightyellow").place(x=510,y=100,width=150)
        btn_search = Button(self.root, text="search", font=("goudy old style", 15,'bold'), bg='#03a9f4', fg='white', cursor="hand2").place(x=680,y=100, width=100, height=35)
        btn_clear = Button(self.root, text="clear", font=("goudy old style", 15,'bold'), bg='grey', fg='white', cursor="hand2").place(x=800,y=100, width=100, height=35)

        lbl_roll=Label(self.root,text="roll no",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_name=Label(self.root,text="name",font=("goudy old style",15,"bold"),bg="white",bd="2",relief=GROOVE).place(x=300,y=230,width=150,height=50)
        lbl_course=Label(self.root,text="course",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_marks=Label(self.root,text="marks obtained",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        lbl_full=Label(self.root,text="total marks",font=("goudy old style",15,"bold"),bg="white",bd="2",relief=GROOVE).place(x=750,y=230,width=150,height=50)
        lbl_per=Label(self.root,text="percentage",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)

        self.roll=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.roll.place(x=150,y=280,width=150,height=50)
        self.name=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd="2",relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.course=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=450,y=280,width=150,height=50)
        self.marks=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.marks.place(x=600,y=280,width=150,height=50)
        self.full=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd="2",relief=GROOVE)
        self.full.place(x=750,y=280,width=150,height=50)
        self.per=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.per.place(x=900,y=280,width=150,height=50)

        btn_delete = Button(self.root, text="delete", font=("goudy old style", 15,'bold'), bg='red', fg='white', cursor="hand2").place(x=520,y=350, width=150, height=35)

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
             cur.execute("select * from result where roll=?",(self.var_search.get(),))
             row=cur.fetchone()
             if row!=None:
                 self.roll.config(text="")
                 self.roll.config(text="")
                 self.roll.config(text="")
                 self.roll.config(text="")
                 self.roll.config(text="")
                 self.roll.config(text="")
                 self.roll.config(text="")
             else:
                 messagebox.showerror("Error", "record Not Found",parent=self.root)
            
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj=reportclass(root)
    root.mainloop()