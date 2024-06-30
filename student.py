from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class studentclass:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1537x835+-8+-2")
        self.root.config(bg="white")
        self.root.focus_force()

#=================================================================logo========================================================================

        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")

#================================================================Title========================================================================

        
        title=Label(self.root,text="Sharma Computer Tutorial's \nManage Student Details",image=self.logo_dash,padx=10,compound=LEFT,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=90)

#==============================================================Veriables======================================================================

        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()

#================================================================Widgets======================================================================

        #-------------------------------------------------Row 1----------------------------------------------

        lbl_roll=Label(self.root,text="Roll no:",font=("goudy old style",15,'bold'),bg='white').place(x=50,y=110)

        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_roll.place(x=170,y=112,width=240,height=28)


        lbl_name=Label(self.root,text="Name:",font=("goudy old style",15,'bold'),bg='white').place( x=450,y=110)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=600,y=112,width=240,height=28)


        #-------------------------------------------------Row 2----------------------------------------------


        lbl_contact=Label(self.root,text="Contact:",font=("goudy old style",15,'bold'),bg='white').place( x=50,y=190)

        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=170,y=192 ,width=240,height=28)


        lbl_email=Label(self.root,text="Email:",font=("goudy old style",15,'bold'),bg='white').place(x=450,y=190)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=600,y=192 ,width=240,height=28)


        #-------------------------------------------------Row 3----------------------------------------------

        lbl_dob=Label(self.root,text="D.O.B:",font=("goudy old style",15,'bold'),bg='white').place(x=50,y=270)

        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=170,y=272,width=240,height=28)


        lbl_admission=Label(self.root,text="Admission Date",font=("goudy old style",15,'bold'),bg='white').place(x=445,y=270)

        txt_admission=Entry(self.root,textvariable=self.var_a_date,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=600,y=272,width=240,height=28)



        #-------------------------------------------------Row 4----------------------------------------------


        lbl_gender=Label(self.root,text="Gender:",font=("goudy old style",15,'bold'),bg='white').place(x=50,y=350)

        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=("goudy old style",15,'bold'),state="readonly",justify=CENTER)
        self.txt_gender.place(x=170,y=352,width=240,height=28)
        self.txt_gender.current(0)

        
        self.course_list=[]
        self.fetch_course()
        #Finction call for course list

        lbl_course=Label(self.root,text="Course:",font=("goudy old style",15,'bold'),bg='white').place(x=450,y=350)

        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",15,'bold'),state="readonly",justify=CENTER)
        self.txt_course.place(x=600,y=352,width=240,height=28)
        self.txt_course.set("Select")



        #-------------------------------------------------Row 5----------------------------------------------


        lbl_state=Label(self.root,text="State:",font=("goudy old style",15,'bold'),bg='white').place(x=50,y=430)

        txt_state=Entry(self.root,textvariable=self.var_state,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=170,y=432,width=200,height=28)
        

        lbl_city=Label(self.root,text="City:",font=("goudy old style",15,'bold'),bg='white').place(x=390,y=430)
        txt_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=450,y=432,width=150,height=28)

        
        lbl_pin=Label(self.root,text="Pin:",font=("goudy old style",15,'bold'),bg='white').place(x=620,y=430)
        txt_pin=Entry(self.root,textvariable=self.var_pin,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=680,y=432,width=160,height=28)
        


        #-------------------------------------------------Row 6----------------------------------------------

        
        lbl_address=Label(self.root,text="Address:",font=("goudy old style",15,'bold'),bg='white').place(x=50,y=500)
        
        self.txt_address=Text(self.root,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_address.place(x=170,y=502,width=670,height=150)


#==================================================================Buttons====================================================================

        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=55,y=690,width=180,height=50)

        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=250,y=690,width=180,height=50)

        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=450,y=690,width=180,height=50)

        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=650,y=690,width=190,height=50)


#===================================================================Search panal==============================================================
        self.var_search=StringVar()

        lbl_search_roll=Label(self.root,text="Search by || Roll no",font=("goudy old style",15,'bold'),bg='white').place(x=890,y=110)
        txt_Search_roll=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=1100,y=112,width=220)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=1350,y=112,width=150,height=28)

#====================================================================Content==================================================================

        self.c_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=880,y=160,width=650,height=580)

        scrolly=Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.c_frame,orient=HORIZONTAL)

        self.coursetable=ttk.Treeview(self.c_frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.coursetable.xview)
        scrolly.config(command=self.coursetable.yview)

        self.coursetable.heading("roll",text="Roll No")
        self.coursetable.heading("name",text="Name")
        self.coursetable.heading("email",text="E-Mail")
        self.coursetable.heading("gender",text="Gender")
        self.coursetable.heading("dob",text="D.O.B")
        self.coursetable.heading("contact",text="Contact")
        self.coursetable.heading("admission",text="Admission")
        self.coursetable.heading("course",text="Course")
        self.coursetable.heading("state",text="State")
        self.coursetable.heading("city",text="City")
        self.coursetable.heading("pin",text="Pin")
        self.coursetable.heading("address",text="Address")

        self.coursetable["show"]='headings'
        
        self.coursetable.column("roll",width=50)
        self.coursetable.column("name",width=130)
        self.coursetable.column("email",width=150)
        self.coursetable.column("gender",width=60)
        self.coursetable.column("dob",width=80)
        self.coursetable.column("contact",width=100)
        self.coursetable.column("admission",width=100)
        self.coursetable.column("course",width=100)
        self.coursetable.column("state",width=100)
        self.coursetable.column("city",width=100)
        self.coursetable.column("pin",width=100)
        self.coursetable.column("address",width=150)
        

        self.coursetable.pack(fill=BOTH,expand=1)
        self.coursetable.bind("<ButtonRelease-1>",self.get_data)
        self.Show()

#================================================================Footer=======================================================================
        
        footer=Label(self.root,text="SMS\nStudent Management System",font=("goudy old style",12,),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

#================================================================Functions=======================================================================
    def clear(self):
        self.Show()
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_a_date.set(""),
        self.var_course.set("Select"),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.txt_address.delete("1.0",END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")

    def delete(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()   
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll Number Name should be required",parent=self.root)
            else:
                cur.execute("select * from Student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select Student from list.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted sucessfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")

    def get_data(self,ev):
        self.txt_roll.config(state="readonly")
        r=self.coursetable.focus()
        content=self.coursetable.item(r)
        row=content["values"]
        self.var_roll.set(row [0]),
        self.var_name.set(row [1]),
        self.var_email.set(row [2]),
        self.var_gender.set(row [3]),
        self.var_dob.set(row [4]),
        self.var_contact.set(row [5]),
        self.var_a_date.set(row [6]),
        self.var_course.set(row [7]),
        self.var_state.set(row [8]),
        self.var_city.set(row [9]),
        self.var_pin.set(row [10]),
        self.txt_address.delete("1.0",END),
        self.txt_address.insert(END,row[11])
         

    def add(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()   
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll Number should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll Number already present.",parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Added Sucessfully",parent=self.root)
                    self.Show()
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def Show(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()   
        try:
             cur.execute("select * from student")
             rows=cur.fetchall()
             self.coursetable.delete(*self.coursetable.get_children())
             for row in rows:
                self.coursetable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")


    def fetch_course(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()   
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def search(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()   
        try:
            cur.execute("select * from student where roll=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=None:
                self.coursetable.delete(*self.coursetable.get_children())
                self.coursetable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
        

    def update(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()   
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll number should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select student from list",parent=self.root)
                else:
                    cur.execute("update student set name=? ,email=? ,gender=? ,dob=? ,contact=? ,admission=? ,course=? ,state=? ,city=? ,pin=? ,address=?  where roll=?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                        self.var_roll.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Updated Sucessfully",parent=self.root)
                    self.Show()
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")

if __name__=="__main__":
    root=Tk()
    obj=studentclass(root)
    root.mainloop()