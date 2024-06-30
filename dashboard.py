from tkinter import*
from PIL import Image,ImageTk
from course import courseclass
from student import studentclass
from result import resultclass
from report import reportclass
from tkinter import messagebox
import sqlite3
import os

class RMS:
    
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1537x835+-8+-2")

#=================================================================logo========================================================================

        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")

#================================================================Title========================================================================
        
        title=Label(self.root,text="Sharma Computer Tutorial's \nStudent Management Dashboard",image=self.logo_dash,padx=10,compound=LEFT,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=90)

#================================================================Menu=========================================================================

        m_frame=LabelFrame(self.root,text="Menus",font=("times new roman",15))
        m_frame.place(x=10,y=90,width=1515,height=100)

        btn_course=Button(m_frame,text="Course",font=("goudy old style",15),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=25,y=5,width=250,height=55)
        btn_student=Button(m_frame,text="Student",font=("goudy old style",15),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=290,y=5,width=250,height=55)
        btn_result=Button(m_frame,text="Result",font=("goudy old style",15),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=555,y=5,width=250,height=55)
        btn_view=Button(m_frame,text="View Student Result",font=("goudy old style",15),bg="#0b5377",fg="white",cursor="hand2",command=self.view_result).place(x=820,y=5,width=250,height=55)
        btn_logout=Button(m_frame,text="Logout",font=("goudy old style",15),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=1085,y=5,width=250,height=55)
        btn_exit=Button(m_frame,text="Exit",font=("goudy old style",15),bg="#e43b06",fg="white",cursor="hand2",command=self.exit).place(x=1350,y=5,width=150,height=55)


#==============================================================Content Window=================================================================

        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((1080,500),Image.ANTIALIAS)

        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=510,y=195,width=800,height=490)

        
        self.left=ImageTk.PhotoImage(file="images/side.png")
        left=Label(self.root,image=self.left).place(x=20,y=190,height=600,width=400)

#=============================================================Update details==================================================================

        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=0,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=450,y=695,width=320,height=100)

        self.lbl_student=Label(self.root,text="Total Student\n[ 0 ]",font=("goudy old style",20),bd=0,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=815,y=695,width=320,height=100)

        self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),bd=0,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1180,y=695,width=320,height=100)

        self.update_details()
#================================================================Footer=======================================================================
        
        footer=Label(self.root,text="SMS.Student Management System",font=("goudy old style",12,),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)


#=================================================================Def=========================================================================

    def update_details(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()   
        try:
             cur.execute("select * from course")
             cr=cur.fetchall()
             self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
             
             cur.execute("select * from student")
             cr=cur.fetchall()
             self.lbl_student.config(text=f"Total Student\n[{str(len(cr))}]")
             
             cur.execute("select * from Result")
             cr=cur.fetchall()
             self.lbl_result.config(text=f"Total Result\n[{str(len(cr))}]")
                
             self.lbl_course.after(200,self.update_details)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")

    def add_course(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=courseclass(self.new_win)
    
    def add_student(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=studentclass(self.new_win)
    
    def add_result(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=resultclass(self.new_win)
    
    def view_result(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=reportclass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            os.system("python login.py")
            self.root.destroy()

    def exit(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()             

if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()