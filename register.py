from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk    
from tkinter import messagebox
import mysql.connector
from mysql.connector import connect, connection



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

        securitA_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        securitA_entry.place(x=370,y=270,width=250)

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

        # ==================Buttons========================
        img=Image.open(r"D:\Library Management System Project\Images\register-now-button1.jpg")
        img=img.resize((200,60),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=20,y=410,width=200)

        img1=Image.open(r"D:\Library Management System Project\Images\login_now_button.jpg")
        img1=img1.resize((200,90),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=330,y=420,width=200)

        # ============Function Declaration============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields are Required.")
        elif self.var_password.get()!=self.var_confirmpassword.get():
            messagebox.showerror("Error","Password & Confirm Password Must Be Same.")  
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms & Conditions.")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="mitali260202",database="mitalidb1")    
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, please try another email.") 
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

            messagebox.showinfo("Success","Register Successfully.")


if __name__ == "__main__":
    root=Tk()        
    app=Register(root)
    root.mainloop()
        