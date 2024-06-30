from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class courseclass:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1537x835+-8+-2")
        self.root.config(bg="white")
        self.root.focus_force()

#=================================================================logo========================================================================

        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")

#================================================================Title========================================================================

        
        title=Label(self.root,text="Sharma Computer Tutorial's \nManage Course Details",image=self.logo_dash,padx=10,compound=LEFT,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=90)

#==============================================================Veriables======================================================================

        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()

#================================================================Widgets======================================================================

        lbl_coursename=Label(self.root,text="Course Name:",font=("goudy old style",15,'bold'),bg='white').place(x=50,y=110)
        lbl_duration=Label(self.root,text="Duration:",font=("goudy old style",15,'bold'),bg='white').place(x=50,y=210)
        lbl_charges=Label(self.root,text="Charges:",font=("goudy old style",15,'bold'),bg='white').place(x=50,y=310)
        lbl_discription=Label(self.root,text="Discription:",font=("goudy old style",15,'bold'),bg='white').place(x=50,y=410)


        self.txt_coursename=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_coursename.place(x=220,y=112,width=300,height=28)

        txt_duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=220,y=212,width=300,height=28)
        txt_charges=Entry(self.root,textvariable=self.var_charges,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=220,y=312,width=300,height=28)

        self.txt_discription=Text(self.root,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_discription.place(x=220,y=410,width=590,height=140)


#==================================================================Buttons====================================================================

        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=55,y=570,width=180,height=50)

        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=250,y=570,width=180,height=50)

        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=450,y=570,width=180,height=50)

        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=650,y=570,width=180,height=50)


#===================================================================Search panal==============================================================
        self.var_search=StringVar()

        lbl_search_coursename=Label(self.root,text="Search by || Course Name",font=("goudy old style",15,'bold'),bg='white').place(x=850,y=100)
        txt_Search_coursename=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=1090,y=100,width=200)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=1310,y=100,width=120,height=28)

#====================================================================Content==================================================================

        self.c_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=850,y=160,width=675,height=460)

        scrolly=Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.c_frame,orient=HORIZONTAL)

        self.coursetable=ttk.Treeview(self.c_frame,columns=("cid","name","duration","charges","discription"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.coursetable.xview)
        scrolly.config(command=self.coursetable.yview)
        self.coursetable.heading("cid",text="Course ID")
        self.coursetable.heading("name",text="Name")
        self.coursetable.heading("duration",text="Duration")
        self.coursetable.heading("charges",text="Charges")
        self.coursetable.heading("discription",text="Discription")

        self.coursetable["show"]='headings'
        
        self.coursetable.column("cid",width=100)
        self.coursetable.column("name",width=100)
        self.coursetable.column("duration",width=100)
        self.coursetable.column("charges",width=100)
        self.coursetable.column("discription",width=150)

        self.coursetable.pack(fill=BOTH,expand=1)
        self.coursetable.bind("<ButtonRelease-1>",self.get_data)
        self.Show()

#================================================================Footer=======================================================================
        
        footer=Label(self.root,text="SMS\nStudent Management System",font=("goudy old style",12,),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

#================================================================Functions=======================================================================
    def clear(self):
        self.Show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_discription.delete("1.0",END)
        self.txt_coursename.config(state=NORMAL)

    def delete(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()   
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select course from list.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course deleted sucessfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")

    def get_data(self,ev):
        self.txt_coursename.config(state="readonly")
        r=self.coursetable.focus()
        content=self.coursetable.item(r)
        row=content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        #self.var_course.set(row[4])
        self.txt_discription.delete('1.0',END)
        self.txt_discription.insert(END,row[4])

    def add(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()   
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course Name already present.",parent=self.root)
                else:
                    cur.execute("insert into course (name ,duration, charges, description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_discription.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Added Sucessfully",parent=self.root)
                    self.Show()
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")


    def Show(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()   
        try:
             cur.execute("select * from course")
             rows=cur.fetchall()
             self.coursetable.delete(*self.coursetable.get_children())
             for row in rows:
                self.coursetable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")


    def search(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()   
        try:
             cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
             rows=cur.fetchall()
             self.coursetable.delete(*self.coursetable.get_children())
             for row in rows:
                self.coursetable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
        

    def update(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()   
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select course from list",parent=self.root)
                else:
                    cur.execute("update course set duration=?, charges=?, description=? where name=?",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_discription.get("1.0",END),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Updated Sucessfully",parent=self.root)
                    self.Show()
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")

if __name__=="__main__":
    root=Tk()
    obj=courseclass(root)
    root.mainloop()