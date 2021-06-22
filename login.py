from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.focus_force()

        #=========== BG Image =====================
        self.bgImage=ImageTk.PhotoImage(file="images/bg.jpg")
        bgImage=Label(self.root,image=self.bgImage).place(x=250,y=0,relwidth=1,relheight=1)

        #=========== BG Image =====================
        self.left=ImageTk.PhotoImage(file="images/log.jpg")
        left=Label(self.root,image=self.left,bg="Black").place(x=80,y=100,width=400,height=500)

        #======================= Register frame =====================
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="LOGIN HERE",font=("times new roman",20,"bold"),bg="white",fg="#08A3D2").place(x=50,y=80)

        #================ Entry Field
        self.var_email=StringVar()
        self.var_password=StringVar()
        email=Label(frame1,text="EMAIL ADDRESS",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=150)
        self.txt_email=Entry(frame1,textvariable=self.var_email, font=("times new roman",15),bg="lightyellow")
        self.txt_email.place(x=50,y=180,width=350,height=30)

        password=Label(frame1,text="PASSWORD",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=250)
        self.txt_password=Entry(frame1,textvariable=self.var_password,font=("times new roman",15),bg="lightyellow")
        self.txt_password.place(x=50,y=280,width=350,height=30)

        btn_forgot=Button(frame1,text="forgot password?",font=("times new roman",15,"bold"),bd=0,bg="white",fg="#B00857",cursor="hand2",command=self.forgot_pass_window).place(x=50,y=350)

        btn_login=Button(frame1,text="Login",font=("times new roman",20,"bold"),bg="#B00857",fg="white",cursor="hand2",command=self.login).place(x=50,y=400,width=200,height=40)
        btn_register=Button(self.root,text="Register",font=("times new roman",20,"bold"),bg="grey",bd=0,cursor="hand2",command=self.register_win).place(x=200,y=460,width=150,height=40)

    def register_win(self):
        # self.root.destroy()
        from register import Register
        self.new_win = Toplevel(self.root)
        self.new_obj = Register(self.new_win)

    def login(self):
        if(self.txt_email.get()=="" or self.txt_password.get()==""):
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()
                # print(row)
                if row==None:
                    messagebox.showerror("Error", "Invalid username/password", parent=self.root)
                else:
                    messagebox.showinfo("success","welcome",parent=self.root)
                    self.clear()
                    # self.login_sucess()
                    from dashboard import RMS
                    self.new_win = Toplevel(self.root)
                    self.new_obj = RMS(self.new_win)
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)

    def clear(self):
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)

    def forgot_pass(self):
        if(self.cmb_ques.get()=="select" or self.txt_answer.get()=="" or self.txt_npassword.get()==""):
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="employee")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s and question=%s and answer=%s", (self.txt_email.get(),self.cmb_ques.get(),self.txt_answer.get()))
                row = cur.fetchone()
                # print(row)
                if row == None:
                    messagebox.showerror("Error", "please select the correct Security question / Enter answer",parent=self.root2)
                else:
                    cur.execute("update employee set password=%s where email=%s ",(self.txt_npassword.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("seccess","your password has been reset, please login with new password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)

    def reset(self):
        self.cmb_ques.current(0)
        self.txt_npassword.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_email.delete(0,END)

    def forgot_pass_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","please enter email address to reset your password",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",self.txt_email.get())
                row=cur.fetchone()
                # print(row)
                if row==None:
                    messagebox.showerror("Error", "please enter valid email address to reset your password",parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forgot password")
                    self.root2.geometry("400x400+450+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t = Label(self.root2, text="Forgot Password", font=("times new roman", 20, "bold"), bg="white",fg="red").place(x=0, y=10, relwidth=1)

                    question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"),bg="white", fg="grey").place(x=70, y=80)
                    self.cmb_ques = ttk.Combobox(self.root2, font=("times new roman", 15), state='readonly',justify=CENTER)
                    self.cmb_ques['values'] = (
                    "select", "your first pet name?", "your birth place", "your nickname", "your best friend name")
                    self.cmb_ques.place(x=70, y=110, width=250)
                    self.cmb_ques.current(0)

                    answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="white",fg="grey").place(x=70, y=150)
                    self.txt_answer = Entry(self.root2, font=("times new roman", 15), bg="lightyellow")
                    self.txt_answer.place(x=70, y=180, width=250)

                    npassword = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white",fg="grey").place(x=70, y=230)
                    self.txt_npassword = Entry(self.root2, font=("times new roman", 15), bg="lightyellow")
                    self.txt_npassword.place(x=70, y=260, width=250)

                    btn_change = Button(self.root2, text="Reset Password", font=("times new roman", 20, "bold"),bg="green", fg="white", cursor="hand2",command=self.forgot_pass).place(x=90, y=320, width=200,height=50)
                    # self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)


    # def login_success(self):
    #     # self.root.destroy()
    #     import dashboard
    #     from dashboard import RMS
    #     self.new_win = Toplevel(self.root)
    #     self.new_obj = RMS(self.new_win)

if __name__=="__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()