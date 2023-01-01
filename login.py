from tkinter import*
import tkinter as tk
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk    #pip install pillow
from tkinter import messagebox
import datetime 
import mysql.connector


from mysql.connector import connect, connection 



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1250x500+0+0")
        self.bg = ImageTk.PhotoImage(file=r"D:\Library Management System Project\Images\picture.jpg")

        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root,bg="black")
        frame.place(x=463,y=130,width=350,height=450)

        img1=Image.open(r"D:\Library Management System Project\Images\unnamed.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=580,y=130,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        # label
        Useremail=lbl=Label(frame,text=" User Email",font=("times new roman",15,"bold"),fg="white",bg="black")
        Useremail.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        Password=lbl=Label(frame,text=" Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        Password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.txtpass.place(x=40,y=250,width=270)
        
        ###################Icon Images################

        img2=Image.open(r"D:\Library Management System Project\Images\login_image.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=510,y=285,width=25,height=25)

        img3=Image.open(r"D:\Library Management System Project\Images\protected.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=510,y=355,width=25,height=25)

        # LoginButton

        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # RegisterButton

        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=340,width=160)

        # ForgotPasswordButton

        forgotpasswordbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpasswordbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error!","All Fields are Required")
        elif self.txtuser.get()=="Mitali" and self.txtpass.get()=="2602":
            messagebox.showinfo("Success...","Welcome")   
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="mitali260202",database="mitalidb1")    
            my_cursor=conn.cursor()
            my_cursor.execute("Select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                      ))

            row=my_cursor.fetchone()
           
            # print row
            if row==None:
                messagebox.showerror("Error!","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                        self.new_window=Toplevel(self.root) 
                        self.app=Library_Management_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()    

    # ========================================Reset Password====================================
    
    def reset_pass(self):
        if self.combo_securityQ.get()=="Select":
            messagebox.showerror("Error!","Select Security Question.",parent=self.root2)
        elif self.txt_securityA.get()=="":
            messagebox.showerror("Error!","Please Enter the Answer.",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error!","Please Enter the New Password.",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="mitali260202",database="mitalidb1")    
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_securityQ.get(),self.txt_securityA.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error!","Please enter correct Answer.",parent=self.root2)
            else:
                query=("Update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Success...","Your password has been reset, please login with new password.",parent=self.root2)
                self.root2.destroy()


    # ========================================Forgot Password Window====================================
      
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error!","Please enter the email address to reset password.")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="mitali260202",database="mitalidb1")    
            my_cursor=conn.cursor()  
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            print(row)

            if row==None:
                messagebox.showerror("Error!","Please enter the valid user email.")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot password")
                self.root2.geometry("340x450+610+170") 
                self.root2.config(bg="white")
                self.root2.focus_force()   
                self.root2.grab_set()
                l = Label(self.root2,text="Forgot password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)


                SecurityQ=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
                SecurityQ.place(x=50,y=80)

                self.combo_securityQ=ttk.Combobox(self.root2,font=("times new roman",15),state="readonly")
                self.combo_securityQ["values"]=("Select","Your Birth Place","Your Hobby","Your Favourite Subject")
                self.combo_securityQ.place(x=50,y=110,width=250)
                self.combo_securityQ.current(0)

        
                securityA=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                securityA.place(x=50,y=150)
                
                #securityA_entry

                self.txt_securityA=ttk.Entry(self.root2,font=("times new roman",15,))
                self.txt_securityA.place(x=50,y=180,width=250)


                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=220)
             
                #new_password_entry

                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15,))
                self.txt_new_password.place(x=50,y=250,width=250)

                resetbtn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                resetbtn.place(x=135,y=290)

            
               
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1250x500+0+0")

        # ==================Variables================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password=StringVar()
        self.var_confirmpassword=StringVar()
        self.var_check=IntVar()


        # ==================bg image=================
        self.bg = ImageTk.PhotoImage(file=r"D:\Library Management System Project\Images\bg_image.jpg")
        bg_lbl = Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # ==================left image================
        self.bg1 = ImageTk.PhotoImage(file=r"D:\Library Management System Project\Images\library_image.jpg")
        left_lbl = Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=80,width=390,height=500)

        # ==================main frame================
        frame=Frame(self.root,bg="white")
        frame.place(x=440,y=80,width=785,height=500)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        # =============label & entry===============

        # ------------------row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        lname_entry.place(x=370,y=130,width=250)

        # --------------------row2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        contact_entry.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        email_entry.place(x=370,y=200,width=250)

        # --------------------row3
        SecurityQ=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        SecurityQ.place(x=50,y=240)

        self.combo_securityQ=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15),state="readonly")
        self.combo_securityQ["values"]=("Select","Your Birth Place","Your Hobby","Your Favourite Subject")
        self.combo_securityQ.place(x=50,y=270,width=250)
        self.combo_securityQ.current(0)


        securityA=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        securityA.place(x=370,y=240)

        securityA_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        securityA_entry.place(x=370,y=270,width=250)

        # --------------------row4
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        password.place(x=50,y=310)

        password_entry=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15))
        password_entry.place(x=50,y=340,width=250)

        confirmpassword=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirmpassword.place(x=370,y=310)

        confirmpassword_entry=ttk.Entry(frame,textvariable=self.var_confirmpassword,font=("times new roman",15))
        confirmpassword_entry.place(x=370,y=340,width=250)

        # ==================Check Button====================
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=40,y=380)

        # ==================Button========================

        # Register Now Button

        img=Image.open(r"D:\Library Management System Project\Images\register-now-button1.jpg")
        img=img.resize((200,60),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=238,y=410,width=200)
       

        # ============Function Declaration============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error!","All Fields are Required.",parent=self.root)
        elif self.var_password.get()!=self.var_confirmpassword.get():
            messagebox.showerror("Error!","Password & Confirm Password Must Be Same.",parent=self.root)  
        elif self.var_check.get()==0:
            messagebox.showerror("Error!","Please Agree Our Terms & Conditions.",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="mitali260202",database="mitalidb1")    
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error!","User already exist, please try another email.",parent=self.root) 
            else:
                my_cursor.execute("Insert Into Register Values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                         self.var_fname.get(),
                                                                                         self.var_lname.get(),
                                                                                         self.var_contact.get(),
                                                                                         self.var_email.get(),
                                                                                         self.var_securityQ.get(),
                                                                                         self.var_securityA.get(),
                                                                                         self.var_password.get()
                                                                                         

                                                                                     ))         
            conn.commit()
            conn.close()

            messagebox.showinfo("Success...","Register Successfully.",parent=self.root)
    



class Library_Management_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1250x500+0+0")

        # ==================================Variable==================================

        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.surname_var=StringVar()
        self.address_var=StringVar()
        self.postcode_var=StringVar()
        self.mobileno_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.actualprice_var=StringVar()

        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="purple",bd=20,relief=RIDGE,font=("times new roman",35,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open(r"D:\Library Management System Project\Images\Book logo.jpg")
        img1=img1.resize((70,60),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=157,y=20)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=108,width=1280,height=350)

        # ==================================DataFrameLeft==================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="red",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=780,height=310)

        lblMember=Label(DataFrameLeft,text="MemberType:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblPRN_NO=Label(DataFrameLeft,text="PRN No:",bg="powder blue",font=("arial",12,"bold"),padx=2)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,textvariable=self.prn_var,font=("arial",13,"bold"),width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,text="ID No:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,textvariable=self.id_var,font=("arial",13,"bold"),width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,text="FirstName:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("arial",13,"bold"),width=29)
        txtFirstName.grid(row=3,column=1)

        lblSurName=Label(DataFrameLeft,text="SurName:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblSurName.grid(row=4,column=0,sticky=W)
        txtSurName=Entry(DataFrameLeft,textvariable=self.surname_var,font=("arial",13,"bold"),width=29)
        txtSurName.grid(row=4,column=1)
        
        lblAddress=Label(DataFrameLeft,text="Address:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=5,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft,textvariable=self.address_var,font=("arial",13,"bold"),width=29)
        txtAddress.grid(row=5,column=1)

        lblPostCode=Label(DataFrameLeft,text="Post Code:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblPostCode.grid(row=6,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,textvariable=self.postcode_var,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=6,column=1)

        lblMobileNo=Label(DataFrameLeft,text="Mobile No:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobileNo.grid(row=7,column=0,sticky=W)
        txtMobileNo=Entry(DataFrameLeft,textvariable=self.mobileno_var,font=("arial",13,"bold"),width=29)
        txtMobileNo.grid(row=7,column=1)

        lblBookID=Label(DataFrameLeft,text="Book ID:",bg="powder blue",font=("arial",12,"bold"),padx=2)
        lblBookID.grid(row=0,column=2,sticky=W)
        txtBookID=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("arial",12,"bold"),width=29)
        txtBookID.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,text="BookTitle:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("arial",12,"bold"),width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,text="AuthorName:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,textvariable=self.author_var,font=("arial",12,"bold"),width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,text="DateBorrowed:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("arial",12,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,text="DateDue:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("arial",12,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)

        lblLateReturnFine=Label(DataFrameLeft,text="LateReturnFine:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=5,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,textvariable=self.latereturnfine_var,font=("arial",12,"bold"),width=29)
        txtLateReturnFine.grid(row=5,column=3)

        lblDateOverDue=Label(DataFrameLeft,text="DateOverDue:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateOverDue.grid(row=6,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,textvariable=self.dateoverdue_var,font=("arial",12,"bold"),width=29)
        txtDateOverDue.grid(row=6,column=3)

        lblActualPrice=Label(DataFrameLeft,text="ActualPrice:",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=7,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,textvariable=self.actualprice_var,font=("arial",12,"bold"),width=29)
        txtActualPrice.grid(row=7,column=3)

        # ==================================Data Frame Right==================================

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",bd=12,fg="red",relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=780,y=5,width=450,height=310)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=23,height=14,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['1) Python Tutorial','2) Machine Techno','3) My Python','4) Secrete Rahasya','5) Intro to Python','6) Joss Ellif Guru','7) Python 3.6',
                   '8) Pandas for Everyone','9) Machine Learning','10) Deep Learning','11) Head First Book','12) Python CookBook','13) The Algorithm',
                   '14) Python Programming','15) Intelligent Project Using Python','16) Data Science & Machine Learning','17) Computer Vision',
                   '18) Data Structure','19) DOS Guide']
        def showSelectBook(event=""):
            value=listBox.get(listBox.curselection())
            x=value
            if(x=="1) Python Tutorial"):
                self.bookid_var.set("BKID2020")
                self.booktitle_var.set("Python Tutorial")
                self.author_var.set("Guido van Rossum")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.570")

            elif(x=="2) Machine Techno"):
                self.bookid_var.set("BKID3564")
                self.booktitle_var.set("Machine Techno")
                self.author_var.set("John Doss")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.720")

            elif(x=="3) My Python"):
                self.bookid_var.set("BKID6487")
                self.booktitle_var.set("My Python")
                self.author_var.set("Paul Barry")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.430")

            elif(x=="4) Secrete Rahasya"):
                self.bookid_var.set("BKID2626")
                self.booktitle_var.set("Secrete Rahasya")
                self.author_var.set("George MCcarthy")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.590")

            elif(x=="5) Intro to Python"):
                self.bookid_var.set("BKID8083")
                self.booktitle_var.set("Intro to Python")
                self.author_var.set("Zed A. Shaw")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.810")

            elif(x=="6) Joss Ellif Guru"):
                self.bookid_var.set("BKID3454")
                self.booktitle_var.set("Joss Ellif Guru")
                self.author_var.set("Sarah Guido")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.350")

            elif(x=="7) Python 3.6"):
                self.bookid_var.set("BKID8545")
                self.booktitle_var.set("Python 3.6")
                self.author_var.set("John M. Zelle")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.650")

            elif(x=="8) Pandas for Everyone"):
                self.bookid_var.set("BKID1058")
                self.booktitle_var.set("Pandas for Everyone")
                self.author_var.set("Brian Jones")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.250")

            elif(x=="9) Machine Learning"):
                self.bookid_var.set("BKID0040")
                self.booktitle_var.set("Machine Learning")
                self.author_var.set("Eric Matthes")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.500")

            elif(x=="10) Deep Learning"):
                self.bookid_var.set("BKID6480")
                self.booktitle_var.set("Deep Learning")
                self.author_var.set("Andreas Muller")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.435")

            elif(x=="11) Head First Book"):
                self.bookid_var.set("BKID9889")
                self.booktitle_var.set("Head First Book")
                self.author_var.set("Luciano Ramalho")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.820")

            elif(x=="12) Python CookBook"):
                self.bookid_var.set("BKID5050")
                self.booktitle_var.set("Python CookBook")
                self.author_var.set("Mark Lutz")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.610")

            elif(x=="13) The Algorithm"):
                self.bookid_var.set("BKID1230")
                self.booktitle_var.set("The Algorithm")
                self.author_var.set("David Beazley")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.310")

            elif(x=="14) Python Programming"):
                self.bookid_var.set("BKID9753")
                self.booktitle_var.set("Python Programming")
                self.author_var.set("Brian Jones")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.780")

            elif(x=="15) Intelligent Project Using Python"):
                self.bookid_var.set("BKID8834")
                self.booktitle_var.set("Intelligent Project Using Python")
                self.author_var.set("Alex Martell")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.240")

            elif(x=="16) Data Science & Machine Learning"):
                self.bookid_var.set("BKID5533")
                self.booktitle_var.set("Data Science & Machine Learning")
                self.author_var.set("Richard Halterman's")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.450")

            elif(x=="17) Computer Vision"):
                self.bookid_var.set("BKID5030")
                self.booktitle_var.set("Computer Vision")
                self.author_var.set("Brian Draper")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.300")

            elif(x=="18) Data Structure"):
                self.bookid_var.set("BKID7893")
                self.booktitle_var.set("Data Structure")
                self.author_var.set("Michael T. Goodrich")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.700")

            elif(x=="19) DOS Guide"):
                self.bookid_var.set("BKID3333")
                self.booktitle_var.set("DOS Guide")
                self.author_var.set("Peter Norton")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("Rs.690")

        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=14)
        listBox.bind("<<ListboxSelect>>",showSelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        # ==================================Buttons Frame==================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=457,width=1280,height=60)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)

        # ==================================Information Frame==================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=515,width=1280,height=143)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1220,height=120)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","idno","firstname",
                                                            "surname","address","postcode","mobileno",
                                                            "bookid","booktitle","authorname","dateborrowed",
                                                            "datedue","latereturnfine","dateoverdue","actualprice"),
                                                            xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="MemberType")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("idno",text="ID No")
        self.library_table.heading("firstname",text="FirstName")
        self.library_table.heading("surname",text="SurName")
        self.library_table.heading("address",text="Address")
        self.library_table.heading("postcode",text="Post Code")
        self.library_table.heading("mobileno",text="Mobile No")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="BookTitle")
        self.library_table.heading("authorname",text="AuthorName")
        self.library_table.heading("dateborrowed",text="DateBorrowed")
        self.library_table.heading("datedue",text="DateDue")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("actualprice",text="ActualPrice")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("idno",width=100)
        self.library_table.column("firstname",width=100)        
        self.library_table.column("surname",width=100)
        self.library_table.column("address",width=100)
        self.library_table.column("postcode",width=100)
        self.library_table.column("mobileno",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("authorname",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("actualprice",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

        

    def add_data(self):
        connection=mysql.connector.connect(host="localhost",username="root",password="mitali260202",database="mitalidb1")
        my_cursor=connection.cursor()
        my_cursor.execute("Insert Into Library Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.member_var.get(),
                                                                                                            self.prn_var.get(),
                                                                                                            self.id_var.get(),
                                                                                                            self.firstname_var.get(),
                                                                                                            self.surname_var.get(),
                                                                                                            self.address_var.get(),
                                                                                                            self.postcode_var.get(),
                                                                                                            self.mobileno_var.get(),
                                                                                                            self.bookid_var.get(),
                                                                                                            self.booktitle_var.get(),
                                                                                                            self.author_var.get(),
                                                                                                            self.dateborrowed_var.get(),
                                                                                                            self.datedue_var.get(),
                                                                                                            self.latereturnfine_var.get(),
                                                                                                            self.dateoverdue_var.get(),
                                                                                                            self.actualprice_var.get(),
                                                                                                        ))
        connection.commit(),
        self.fetch_data()
        connection.close(),
        
        messagebox.showinfo("Success...","Member Has Been Inserted Successfully.",parent=self.root)

    def update(self):
        connection=mysql.connector.connect(host="localhost",username="root",password="mitali260202",database="mitalidb1")
        my_cursor=connection.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,Firstname=%s,Surname=%s,Address=%s,PostCode=%s,MobileNo=%s,BookID=%s,BookTitle=%s,AuthorName=%s,DateBorrowed=%s,DateDue=%s,LateReturnFine=%s,DateOverDue=%s,ActualPrice=%s where PRN_NO=%s",(
                                                                                                            self.member_var.get(),
                                                                                                            self.id_var.get(),
                                                                                                            self.firstname_var.get(),
                                                                                                            self.surname_var.get(),
                                                                                                            self.address_var.get(),
                                                                                                            self.postcode_var.get(),
                                                                                                            self.mobileno_var.get(),
                                                                                                            self.bookid_var.get(),
                                                                                                            self.booktitle_var.get(),
                                                                                                            self.author_var.get(),
                                                                                                            self.dateborrowed_var.get(),
                                                                                                            self.datedue_var.get(),
                                                                                                            self.latereturnfine_var.get(),
                                                                                                            self.dateoverdue_var.get(),
                                                                                                            self.actualprice_var.get(),
                                                                                                            self.prn_var.get(),
                                                                                       ))
        connection.commit(),
        self.fetch_data()
        self.reset()
        connection.close(),

        messagebox.showinfo("Success...","Member has been Updated",parent=self.root)


    def fetch_data(self):
        connection=mysql.connector.connect(host="localhost",username="root",password="mitali260202",database="mitalidb1")
        my_cursor=connection.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
                connection.commit()
            connection.close()
            my_cursor.close()

    def get_cursor(self,event=""):         
        cursor_row=self.library_table.focus()   
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.surname_var.set(row[4]),
        self.address_var.set(row[5]),
        self.postcode_var.set(row[6]),
        self.mobileno_var.set(row[7]),
        self.bookid_var.set(row[8]),
        self.booktitle_var.set(row[9]),
        self.author_var.set(row[10]),
        self.dateborrowed_var.set(row[11]),
        self.datedue_var.set(row[12]),
        self.latereturnfine_var.set(row[13]),
        self.dateoverdue_var.set(row[14]),
        self.actualprice_var.set(row[15])


    def showData(self):
        self.txtBox.insert(END,"MemberType :  "+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN NO :  "+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID NO :  "+ self.id_var.get() + "\n")
        self.txtBox.insert(END,"FirstName :  "+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"SurName :  "+ self.surname_var.get() + "\n")
        self.txtBox.insert(END,"Address :  "+ self.address_var.get() + "\n")
        self.txtBox.insert(END,"Post Code :  "+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile No :  "+ self.mobileno_var.get() + "\n")
        self.txtBox.insert(END,"Book ID :  "+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"BookTitle :  "+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"AuthorName :  "+ self.author_var.get() + "\n")
        self.txtBox.insert(END,"DateBorrowed:  "+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"DateDue :  "+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"LateReturnFine :  "+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END,"DateOverDue :  "+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"ActualPrice :  "+ self.actualprice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.surname_var.set(""),
        self.address_var.set(""),
        self.postcode_var.set(""),
        self.mobileno_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.actualprice_var.set("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit",parent=self.root)
        if iExit>0:
            self.root.destroy()
            return
    def delete(self):
        if self.prn_var.get=="" or self.id_var.get()=="":
            messagebox.showerror("Error!","First Select the Member",parent=self.root)
        else:
            connection=mysql.connector.connect(host="localhost",username="root",password="mitali260202",database="mitalidb1")
            my_cursor=connection.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            connection.commit()
            self.fetch_data()
            self.reset()
            connection.close()

            messagebox.showinfo("Success...","Member has been Deleted",parent=self.root)

if __name__ == "__main__":
          main()

        
