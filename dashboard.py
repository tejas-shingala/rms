from tkinter import *
from PIL import Image,ImageTk
from course import courseclass
from student import studentclass
from result import resultclass
from report import reportclass
class rms:
    def __init__(self, root):
        self.root = root
        self.root.title("result management system")
        self.root.geometry("1528x784+0+0")
        self.root.configure(background="white")
 
        logo_img = Image.open("images/logo.jpeg")  
        logo_img = logo_img.resize((50, 50), Image.LANCZOS)
        self.logo_dash = ImageTk.PhotoImage(logo_img)

        
        title = Label(self.root, text="Result Management System", padx=10, compound=LEFT,
                      image=self.logo_dash, font=("goudy old style", 20, "bold"),
                      bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

    
        self.root.iconphoto(False, self.logo_dash)
        
        M_frame = LabelFrame(self.root , text="menus" , font=("times new roman ",15),bg="white")
        M_frame.place(x=10,y=70,width=1500,height=80)

        btn_course = Button(M_frame, text="Course", font=("goudy old style",15,"bold"),bg="#0b5377",fg="white" , cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student = Button(M_frame, text="Student", font=("goudy old style",15,"bold"),bg="#0b5377",fg="white", cursor="hand2",command=self.add_student).place(x=270,y=5,width=200,height=40)
        btn_result = Button(M_frame, text="Result", font=("goudy old style",15,"bold"),bg="#0b5377",fg="white", cursor="hand2",command=self.add_result).place(x=520,y=5,width=200,height=40)
        btn_view = Button(M_frame, text="View student result", font=("goudy old style",15,"bold"),bg="#0b5377",fg="white", cursor="hand2",command=self.add_report).place(x=770,y=5,width=200,height=40)
        btn_logout = Button(M_frame, text="Logout", font=("goudy old style",15,"bold"),bg="#0b5377",fg="white", cursor="hand2").place(x=1020,y=5,width=200,height=40)
        btn_exit = Button(M_frame, text="Exit", font=("goudy old style",15,"bold"),bg="#0b5377",fg="white", cursor="hand2").place(x=1270,y=5,width=200,height=40)

        self.bg_image = Image.open("images/dashboard.jpg")
        self.bg_img = self.bg_image.resize((920, 350), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=600 , y = 180 , width = 920 ,height = 350)

        self.lbl_course = Label(self.root,text="total courses\n[ 0] ",font=("goudy old style", 20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=600,y=530,width=300,height=100)

        self.lbl_student = Label(self.root,text="total students\n[ 0] ",font=("goudy old style", 20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=910,y=530,width=300,height=100)

        self.lbl_result = Label(self.root,text="total result\n[ 0] ",font=("goudy old style", 20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1220,y=530,width=300,height=100)

        footer = Label(self.root, text="SRMS-Result Management System\n contact us for any technical issue ",compound=LEFT, font=("goudy old style", 12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=courseclass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentclass(self.new_win) 

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultclass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportclass(self.new_win)


if __name__ == "__main__":
    root = Tk()
    obj=rms(root)
    root.mainloop()
