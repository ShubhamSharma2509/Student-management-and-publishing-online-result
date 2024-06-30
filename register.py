from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
 
class Registerclass:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Register to Student Management System")
        self.root.geometry("1537x835+-8+-2")
        self.root.config(bg="#033054")
        self.root.focus_force()         


#=================================================================logo========================================================================

        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")

#================================================================Title========================================================================
        
        title=Label(self.root,text="Sharma Computer Tutorial's \nStudent Management Dashboard",image=self.logo_dash,padx=10,compound=LEFT,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=90)


#====================================Left img==========================

        self.left=ImageTk.PhotoImage(file="images/side.png")
        left=Label(self.root,image=self.left).place(x=170,y=130,height=600,width=500)

#====================================Registration Frame==========================

        frame1=Frame(self.root)
        frame1.place(x=640,y=130,width=700,height=600)

#====================================Title==========================

        title=Label(frame1,text="REGESTER HERE",font=("times new roman",20,"bold"),fg="green").place(x=210,y=30)

#====================================Contents==========================

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_question=StringVar()
        self.var_answer=StringVar()
        self.var_password=StringVar()
        self.var_cpassword=StringVar()
        
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),fg="gray").place(x=50,y=100)

        txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_fname).place(x=50,y=130,width=250)
         
        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),fg="gray").place(x=370,y=100)

        txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_lname).place(x=370,y=130,width=250)


        contact=Label(frame1,text="Contact No",font=("times new roman",15,"bold"),fg="gray").place(x=50,y=180)

        txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_contact).place(x=50,y=210,width=250)
         
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),fg="gray").place(x=370,y=180)

        txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_email).place(x=370,y=210,width=250)


        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),fg="gray").place(x=50,y=260)

        cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER,textvariable=self.var_question)
        cmb_quest['values']=("Select","Your First Teacher Name","Your Birth Place","Your Best Friend Name")
        cmb_quest.place(x=50,y=290,width=250)
        cmb_quest.current(0)
         
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),fg="gray").place(x=370,y=260)

        txt_amswer=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_answer).place(x=370,y=290,width=250)


        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),fg="gray").place(x=50,y=340)

        txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_password).place(x=50,y=370,width=250)
         
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),fg="gray").place(x=340,y=340)

        txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_cpassword).place(x=370,y=370,width=250)


#===============================Check box========================================
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree the terms and condition",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",10)).place(x=50,y=430)

#===============================Reguster Button========================================

        self.btn_img=ImageTk.PhotoImage(file="images/register.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=200,y=480,height=40)

        btn_login=Button(self.root,text="Sign In",font=("times new roman",20),bd=1,cursor="hand2",command=self.login).place(x=330,y=550,width=180)
 

#===============================Functions========================================

    def login(self):
        os.system("python login.py")
        self.root.destroy()

    def clear(self):
        self.var_fname.set(""),
        self.var_lname.set(""),
        self.var_contact.set(""),
        self.var_email.set(""),
        self.var_question.set("Select"),
        self.var_answer.set(""),
        self.var_password.set(""),
        self.var_cpassword.set("")

    def register_data(self):

        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_question.get()=="Select" or self.var_contact.get()=="" or self.var_answer.get()=="" or self.var_password.get()=="" or self.var_cpassword.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
            
        #self.var_lname.get()

        elif self.var_password.get()!=self.var_cpassword.get():
            messagebox.showerror("Error","Password and Confirm Password should be same ",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our terms andd condition",parent=self.root)
            
        else:
            try:
                con=sqlite3.connect(database="sms.db")
                cur=con.cursor()
                cur.execute("select *  from employee where email=?",(self.var_email.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already Exist ",parent=self.root)
                else:
                        cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",
                                    (
                                self.var_fname.get(),
                                self.var_lname.get(),
                                self.var_contact.get(),
                                self.var_email.get(),
                                self.var_question.get(),
                                self.var_answer.get(),
                                self.var_password.get()
                                    ))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Sucess","Registered Successfully\n\n You Can Now Login.")
                        self.clear()
                        os.system("python login.py")
                        self.root.destroy()
                                 
            except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)


        
if __name__=="__main__":
    root=Tk()
    obj=Registerclass(root)
    root.mainloop()