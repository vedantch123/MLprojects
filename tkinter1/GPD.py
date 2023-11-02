from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
import pymysql
def main():
    root=Tk()
    app=Login(root)
    root.mainloop()


class Login:
    def __init__(self,root):
        self.win=root
        self.win.geometry("1000x1000")

        self.win.title("coding with vedant")
        self.l1=Label(self.win,text="POLYTECHNIC STUDENT DATA",bd=6,font=("sans-seriff",30,"bold"),bg="lightgrey",relief=GROOVE)
        self.l1.pack(padx=3,pady=3)
        self.f1=Frame(self.win,bg="lightgrey",bd=6,relief=GROOVE)
        self.f1.place(x=210,y=150,width=600,height=450)

        self.login = Label(self.f1, text="LOGIN", bd=6, relief=GROOVE, anchor=CENTER, bg="lightgrey",
                           font=("sans-seriff", 25))
        self.login.pack(side=TOP, fill=X)

        self.label_frame=LabelFrame(self.f1,text="enter details",bd=6,font="sans-seriff,10")
        self.label_frame.pack(fill=BOTH,expand=True)

        self.l2=Label(self.label_frame,text="enter username",font=("sans-seriff,20"),bg="lightgrey")
        self.l2.grid(row=0,column=0,padx=2,pady=2)

        username=StringVar()
        password=StringVar()

        self.e1=Entry(self.label_frame,bd=6,font="sans-seriff,10",textvariable=username)
        self.e1.grid(row=0,column=1,padx=2,pady=2)

        self.l3=Label(self.label_frame,text="enter password",font="sans-seriff,20",bg="lightgrey")
        self.l3.grid(row=1,column=0,pady=2,padx=2)
        self.e2=Entry(self.label_frame,bd=6,font="sans-seriff,10",textvariable=password,show="*")
        self.e2.grid(row=1,column=1,padx=2,pady=2)







        def check_login():
            if username.get()=="v" and password.get()=="v":
                self.b3.config(state=ACTIVE)
            else:
                tmsg.showinfo("invalid username/password")
        def reset():
            username.set("")
            password.set("")
        def enter():
            root = Tk()
            app = Window2(root)
            root.mainloop()












        self.b1=LabelFrame(self.label_frame,text="options",bg='lightgrey',bd=6,relief=GROOVE,font=("sans-seriff 20"))
        self.b1.place(x=5,y=100,height=120,width=600)

        self.b2=Button(self.b1,text="login",bd=6,width=10,font="arial 15",command=check_login)
        self.b2.grid(row=0,column=0,padx=25,pady=5)
        self.b3=Button(self.b1,text="enter",bd=6,width=10,font="arial 15",command=enter)
        self.b3.grid(row=0,column=3,padx=25,pady=5)
        self.b3.config(state=DISABLED)
        self.b4=Button(self.b1,text="reset",bd=6,font="arial 15",width=10,command=reset)
        self.b4.grid(row=0,column=5,pady=5,padx=25)



class Window2:

    def __init__(self,root):
        self.win=root
        self.win.geometry("1000x1000")
        self.win.title("student data")
        self.l9 = Label(self.win, text="POLYTECHNIC STUDENT DATA", bd=6, font=("sans-seriff", 30, "bold"),
                        bg="lightgrey", relief=GROOVE,justify=CENTER)
        self.l9.place(x=200,y=25)

        self.f5=LabelFrame(self.win,text="details",bg="lightgrey",font="sans-seriff 10",bd=6,relief=GROOVE)
        self.f5.place(x=20,y=100,width=400,height=700)
        self.e8 = Label(self.f5, text="enter details", bd=6, relief=GROOVE, anchor=CENTER, bg="lightgrey",
                          font=("sans-seriff", 25))
        self.e8.place()

        def add():
            self.addmission_no = self.enr_enter.get()
            self.student_name = self.e9.get()
            self.father_name = self.e10.get()
            self.date_of_birth = self.date_entry.get()
            self.phone_no = self.mobile_entry.get()
            self.courses = self.combo.get()
            self.address = self.entry_add.get()

            if self.addmission_no == "" or self.student_name == "":
                print("success")

            else:
                con = pymysql.connect(host="localhost", user="root", password="", db="student5")
                cursor = con.cursor()
                cursor.execute(
                    "insert into vedant values('" + self.addmission_no + "','" + self.student_name + "','" + self.father_name + "','" + self.date_of_birth + "','" + self.phone_no + "','" + self.courses + "','" + self.address + "')")
                cursor.execute("commit")
                self.enr_enter.delete(0, END)
                self.e9.delete(0, END)
                self.e10.delete(0, END)
                self.date_entry.delete(0, END)
                self.mobile_entry.delete(0, END)
                self.combo.delete(0, END)
                self.entry_add.delete(0, END)
                fetchall()



                con.close()
        def fetchall():
            con = pymysql.connect(host="localhost", user="root", password="", db="student5")
            cursor = con.cursor()
            cursor.execute("select * from vedant")
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.student.delete(*self.student.get_children())

                for row in rows:
                  self.student.insert('', END, values=row)
                con.commit()


        def reset():
            self.enr_enter.delete(0,END)
            self.e9.delete(0,END)
            self.e10.delete(0,END)
            self.date_entry.delete(0,END)
            self.mobile_entry.delete(0,END)

            self.entry_add.delete(0,END)
        def update():
            self.addmission_no_n=self.enr_enter.get()

            self.student_name_n = self.e9.get()
            self.father_name_f = self.e10.get()
            self.date_of_birth_d = self.date_entry.get()
            self.phone_no_p = self.mobile_entry.get()
            self.courses_c = self.combo.get()
            self.address_a = self.entry_add.get()
            #if  self.student_name=="" or self.father_name == "" or self.date_of_birth =="" or self.courses =="" or self.address =="":
                #print("update status")

            con = pymysql.connect(host="localhost", user="root", password="", db="student5")
            cursor = con.cursor()
            cursor.execute("UPDATE vedant set student_name='"+self.student_name_n+"',father_name='"+self.father_name_f+"',date_of_birth='"+self.date_of_birth_d+"',phone_no='"+self.phone_no_p+"',courses='"+self.courses_c+"',address='"+self.address_a+"'where addmission_no='"+self.addmission_no_n+"'")
            cursor.execute("commit")
            con.commit()
            self.enr_enter.delete(0, END)
            self.e9.delete(0, END)
            self.e10.delete(0, END)
            self.date_entry.delete(0, END)
            self.mobile_entry.delete(0, END)
            self.combo.delete(0, END)
            self.entry_add.delete(0, END)
            fetchall()


            con.close()


        def delete():

            self.addmission_no_n = self.enr_enter.get()
            con = pymysql.connect(host="localhost", user="root", password="", db="student5")
            cursor = con.cursor()
            cursor.execute("delete from vedant where addmission_no='"+self.addmission_no_n+"'")
            cursor.execute("commit")
            con.commit()
            self.enr_enter.delete(0, END)
            self.e9.delete(0, END)
            self.e10.delete(0, END)
            self.date_entry.delete(0, END)
            self.mobile_entry.delete(0, END)
            self.combo.delete(0, END)
            self.entry_add.delete(0, END)
            fetchall()



            con.close()


        def search():
            self.addmission_no_n = self.enr_enter.get()
            self.addmission_no = self.enr_enter.get()
            self.student_name = self.e9.get()
            self.date_of_birth = self.date_entry.get()
            con = pymysql.connect(host="localhost", user="root", password="", db="student5")
            cursor = con.cursor()
            cursor.execute("select * from vedant where "+str(self.search_var.get()) + "Like addmission_no='"+self.addmission_no_n+"'" +str(self.txt_search.get()) + "addmission_no='"+self.addmission_no_n+"'")

            rows=cursor.fetchall()
            for row in rows:
                self.e9.insert(0,row[1])


            con.commit()
            con.close()












        self.addmission_no= Label(self.f5, text="addmission_no", bg="lightgrey", bd=6, font="sans-seriff 20")
        self.addmission_no.grid(padx=2, pady=2, row=0, column=0)
        self.enr_enter = Entry(self.f5, bd=6, font="sans-seriff 10")
        self.enr_enter.grid(padx=2, pady=2, row=0, column=1)

        self.student_name=Label(self.f5,text="student_name",bd=6,bg="lightgrey",font="sans-seriff 20")
        self.student_name.grid(row=1,column=0,padx=2,pady=2)
        self.e9=Entry(self.f5,font="sans-seriff 10",bd=6)
        self.e9.grid(pady=2,padx=2,row=1,column=1)


        self.father_name = Label(self.f5, text="father_name", bd=6, bg="lightgrey", font="sans-seriff 20")
        self.father_name.grid(row=2, column=0, padx=2, pady=2)
        self.e10 = Entry(self.f5, font="sans-seriff 10", bd=6)
        self.e10.grid(pady=2, padx=2, row=2, column=1)


        self.date_of_birth=Label(self.f5,text="date_of_birth",bd=6,bg="lightgrey",font="sans-seriff 20")
        self.date_of_birth.grid(padx=2,pady=2,row=3,column=0)
        self.date_entry=Entry(self.f5,font="sans-seriff 10",bd=6)
        self.date_entry.grid(pady=2,padx=2,row=3,column=1)


        self.phone_no=Label(self.f5,text="phone_no",bd=6,bg="lightgrey",font="sans-seriff 20")
        self.phone_no.grid(padx=2,pady=2,row=4,column=0)
        self.mobile_entry=Entry(self.f5,bd=6,font="sans-seriff 10")
        self.mobile_entry.grid(pady=2,padx=2,row=4,column=1)








        self.course=Label(self.f5,text="courses",bd=6,bg="lightgrey",font="sans-seriff 20")
        self.course.grid(pady=2,padx=2,row=5,column=0)
        #self.course_entry=Entry(self.f5,bd=4,font="sans-seriff 10")
        #self.course_entry.grid(padx=2,pady=2,row=4,column=1)
        self.combo = ttk.Combobox(self.f5, font=("sans-seriff 10"), width=20,height=5,state="readonly")
        self.combo["value"]=("PGDCA","WD","HNW","DS")
        self.combo.current(0)






        self.combo.grid(row=5,column=1,padx=2,pady=2)




        self.address=Label(self.f5,text="address",bd=6,bg="lightgrey",font="sans-seriff 20")
        self.address.grid(pady=2,padx=2,row=6,column=0)
        self.entry_add=Entry(self.f5,bd=4,font="sans-seriff 10")
        self.entry_add.grid(padx=2,pady=2,row=6,column=1)







        self.add=LabelFrame(self.f5,text="Term & conditions",bd=6,bg="lightgrey",font="sans-seriff 10")
        self.add.place(x=15,width=350,y=400,height=150)
        self.check=Checkbutton(self.add,text="i accept the term & policyorcondition",bd=6,bg="lightgrey",font="sans-seriff 10")
        self.check.grid(padx=2,pady=2,row=1,column=0)
        self.check1=Checkbutton(self.add,text="i am 18 and above in term&condition",bd=6,bg="lightgrey",font="sans-seriff 10")
        self.check1.grid(pady=2,padx=2,row=2,column=0)

        self.frame=LabelFrame(self.f5,text="details",bd=6,bg="lightgrey",font="sans-seriff 10")
        self.frame.place(x=15,width=350,y=500,height=150)

        

        self.badd=Button(self.frame,text="ADD",bd=6,bg="lightgrey",font="sans-seriff 10",width=10,command=add)
        self.badd.grid(padx=20,pady=5,row=0,column=0)

        self.reset=Button(self.frame,text="reset",bd=6,bg="lightgrey",font="sans-seriff 10",width=10,command=reset)
        self.reset.grid(padx=20,pady=5,row=0,column=4)

        self.update=Button(self.frame,text="update",bd=6,bg="lightgrey",font="sans-seriff 10",width=10,command=update)
        self.update.grid(row=3,column=0,padx=20,pady=5)

        self.delete=Button(self.frame,text="delete",bd=6,bg="lightgrey",font="sans-seriff 10",width=10,command=delete)
        self.delete.grid(pady=5,padx=20,row=3,column=4)

        self.details=LabelFrame(self.win,text="details",bd=6,bg="lightgrey",font="sans-seriff 10")
        self.details.place(x=420,y=100,width=600,height=700)

        self.search_var=StringVar()
        self.search=Label(self.details,text="searchby",bg="lightgrey",bd=6,font="sans-seriff 20")
        self.search.grid(pady=2,padx=2,row=0,column=0)
        # self.search=Label(self.f5,text="search by",bd=6,bg="light grey",font="sans-seriff 20")
        # self.search.grid(pady=2,padx=2,row=6,column=0)
        self.combo=ttk.Combobox(self.details,font=("sans-seriff 10"),width=10,state="readonly",textvariable=self.search_var)
        self.combo["values"]=("addmission_no","date_of_birth","student_name")
        #self.combo["values"]=("name")
        #self.combo["values"]=("DOB")
        self.combo.grid(row=0,column=2,padx=2,pady=2)

        self.txt_search=StringVar()
        self.search1=Entry(self.details,bd=6,font="sans-seriff 10",textvariable=self.txt_search)
        self.search1.grid(pady=2,padx=2,row=0,column=3)
        self.searchbutton=Button(self.details,text="search",bg="lightgrey",bd=6,font="sans-seriff 10",command=search)
        self.searchbutton.grid(padx=2,pady=2,row=0,column=4)

        self.frame1=Frame(self.details,bd=6,relief=RIDGE,bg="crimson")
        self.frame1.place(x=60,y=70,width=500,height=600)

        self.scroll=Scrollbar(self.frame1,orient=HORIZONTAL)
        self.scroll1=Scrollbar(self.frame1,orient=VERTICAL)
        self.student=ttk.Treeview(self.frame1,columns=("addmission_no","student_name","father_name","date_of_birth","phone_no","courses","address"),xscrollcommand=self.scroll.set,yscrollcommand=self.scroll1.set)
        self.scroll.pack(side=BOTTOM,fill=X)
        self.scroll1.pack(side=RIGHT,fill=Y)
        self.scroll.config(command=self.student.xview)
        self.scroll1.config(command=self.student.yview)

        self.student.heading("addmission_no",text="addmission_no")
        self.student.heading("student_name",text="student_name")
        self.student.heading("father_name",text="father_name")
        self.student.heading("date_of_birth",text="date_of_birth")
        self.student.heading("phone_no",text="phone_no")
        self.student.heading("courses",text="courses")


        self.student.heading("address",text="address")

        self.student["show"]="headings"
        self.student.column("addmission_no",width=100)
        self.student.column("student_name",width=100)
        self.student.column("father_name",width=100)
        self.student.column("date_of_birth",width=100)
        self.student.column("phone_no",width=100)
        self.student.column("courses",width=100)
        self.student.column("address",width=100)

        self.student.pack(fill=BOTH,expand=1)

if __name__=="__main__":

    main()