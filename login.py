from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os

class loginclass:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1537x835+-8+-2")
        self.root.config(bg="#021e2f")
        self.root.focus_force()



#===============================================================================Background===============================================================================

        #-------------------------------Right Frame------------------------------------

        right_lbl=Label(self.root,bg="#021e2f",bd=0)
        right_lbl.place(x=550,y=0,relheight=1,relwidth=1)

        #-------------------------------logo------------------------------------

        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")

        #-------------------------------Title------------------------------------
        
        title=Label(self.root,text="Sharma Computer Tutorial's \nStudent Management Dashboard",image=self.logo_dash,padx=10,compound=LEFT,font=("goudy old style",17,"bold"),bg="#021e2f",fg="white").place(x=0,y=0,width=1650,height=90)

        #-------------------------------Left Frame------------------------------------
        
        left_lbl=Label(self.root,bg="#033054",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=620)


#======================================================================================Left img==========================================================================

        self.left=ImageTk.PhotoImage(file="images/side.png")
        left=Label(self.root,image=self.left).place(x=170,y=130,height=600,width=500)


#=======================================================================================Frames===========================================================================

        login_frame=Label(self.root ,bd=0)
        login_frame.place(x=640,y=130,width=700,height=600)

        #-------------------------------Veriables------------------------------------

        self.var_email=StringVar()
        self.var_pass_=StringVar()

        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold") ,fg="#08A3D2").place(x=20,y=50)
        
        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold") ,fg="gray").place(x=20,y=160)
        
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray",textvariable=self.var_email)
        self.txt_email.place(x=20,y=200,width=350,height=35)
        
        pass_=Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold") ,fg="gray").place(x=20,y=280)
        
        self.txt_pass_=Entry(login_frame,font=("times new roman",15),bg="lightgray",show="*",textvariable=self.var_pass_)
        self.txt_pass_.place(x=20,y=320,width=350,height=35)

        btn_reg=Button(login_frame,command=self.register,text="Register new Account?",font=("times new roman",14) ,bd=0,fg="#08A3D2",cursor="hand2").place(x=20,y=370)

        btn_login=Button(login_frame,text="Log In",font=("times new roman",20,"bold"),fg="white",bg="#08A3D2",cursor="hand2",command=self.login).place(x=20,y=430,width=200,height=50)



#==============================================================================Functions=================================================================================

    def register(self):
        os.system("python register.py")
        self.root.destroy()
    
    def login(self):
        if self.var_email.get()=="" or self.var_pass_.get()=="":
            messagebox.showerror("Error","All Fields are reaquired",parent=self.root)
        
        else:
            try:
                con=sqlite3.connect(database="sms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.var_email.get(),self.var_pass_.get()))
                row=cur.fetchone()
                
                if row==None:
                    messagebox.showerror("Error","Invalid user name Password",parent=self.root)

                else:
                    con.close()
                    self.root.destroy()
                    os.system("python dashboard.py")

            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=loginclass(root)
    root.mainloop()