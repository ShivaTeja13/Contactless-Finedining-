from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
###################finctions

def reset_password():
    if mailentry.get()=='':
        messagebox.showerror('Error','please enter the email adress to reset your password')
    else:
        con=pymysql.connect(host='localhost',user='root',password='1305',database='register')
        cur=con.cursor()
        cur.execute('select * from student where email=%s',mailentry.get())
        row=cur.fetchone()
        if row==None:
            messagebox.showerror('Error','Please enter the valid email address')
        else:
            con.close()
            def change_password():

                if securityquesCombo.get()=='select' or answerEntry.get()==''or newPassEntry.get()=='':
                    messagebox.showerror('Error','All fields are reequired')
                else:
                    con=pymysql.connect(host='localhost',user='root',password='1305',database='register')
                    cur=con.cursor()
                    cur.execute('select * from student where email=%s and question=%s and answer=%s',(mailentry.get(),securityquesCombo.get(),answerEntry.get()))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror('Error','security question or answer is incorrect',parent=root2)
                    else:
                        cur.execute('update student set password=%s where email=%s',(newPassEntry.get(),mailentry.get()))

                        con.commit()
                        con.close()
                        messagebox.showinfo('success','Passwrod is reset, please login with new password',parent=root2)
                        securityquesCombo.current(0)
                        answerEntry.delete(0,END)
                        newPassEntry.delete(0,END)
                        root2.destroy()





            root2=Toplevel()
            root2.title('Forgot Password')
            root2.geometry('470x560+400+60')
            root2.config(bg='white')
            root2.focus_force()
            root2.grab_set()
            forgetpassLabel=Label(root2,text='Forgot Password',font=('times new roman',22,'bold'),bg='white',fg='green')
            forgetpassLabel.place(x=128,y=10)
            securityqueslabel=Label(root2,text='Security Question',font=('times new roman ',19,'bold'),bg='white')
            securityqueslabel.place(x=68,y=220)

            securityquesCombo=ttk.Combobox(root2,font=('times new roman ',19),state='readonly',width=22)
            securityquesCombo['values']=('select','your first pet name?','your birth place name?','Your Best Friend Name?','Your favourite Teacher?','your Favorite Hobby?')
            securityquesCombo.place(x=60,y=260)
            securityquesCombo.current(0)

            answerLabel=Label(root2,text='Answer',font=('times new roman',19,'bold'),bg='white')
            answerLabel.place(x=60,y=310)
            answerEntry=Entry(root2,font=('times new roman',19),bg='white',width=18)
            answerEntry.place(x=60,y=350)

            newPassLabel = Label(root2, text='NEW PASSWORD', font=('times new roman', 19, 'bold'), bg='white')
            newPassLabel.place(x=60, y=400)
            newPassEntry = Entry(root2, font=('times new roman', 19), bg='white', width=18)
            newPassEntry.place(x=60, y=440)

            changepassButton=Button(root2,text='change password',font=('arial',17,'bold'),bg='green',fg='white',cursor='hand2',activebackground='green',activeforeground='white',command=change_password)
            changepassButton.place(x=130,y=500)




            root2.mainloop()







def register_window():
    window.destroy()
    import register

def signin():
    if mailentry.get()==''or passwordentry.get()=='':
        messagebox.showerror('error','ALL FIELDS ARE REQUIRED')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='1305', database='register')
            cur = con.cursor()
            cur.execute('select * from student where email=%s and password=%s', (mailentry.get(), passwordentry.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror('error', 'Invalid Email or Pasword')
            else:
                messagebox.showinfo('Success', 'Welcome')
                window.destroy()
                import menu
            con.close()
        except Exception as e:
            messagebox.showerror('error',f'Error is due to {e}')







#############gui############3
window=Tk()

window.geometry('900x600+50+50')
window.title('login page ')

bgloginimage= PhotoImage(file='loginbg.png')
bgloginLabel=Label(window,image=bgloginimage)
bgloginLabel.place(x=0,y=0)


frame=Frame(window,width=560,height=320,bg='white')
frame.place(x=180,y=140)

userimage=PhotoImage(file='user.png')
userimageLabel=Label(frame,image=userimage,bg='white')
userimageLabel.place(x=10,y=50)

mailLabel=Label(frame,text='EMAIL',font=('arial',22,'bold'),bg='white')
mailLabel.place(x=220, y=32)
mailentry = Entry(frame, font=('arial', 22,), bg='white', fg='black')
mailentry.place(x=220, y=70)

passwordLabel = Label(frame, text='Password', font=('arial', 22, 'bold'), bg='white', fg='black')
passwordLabel.place(x=220, y=120)
passwordentry = Entry(frame, font=('arial', 22,), bg='white', fg='black',show='*')
passwordentry.place(x=220, y=160)
regbutton = Button(frame, text='Register New Account?', font=('arial', 12,), bd=0, fg='gray20', bg='white',
                   cursor='hand2',
                   activebackground='white', activeforeground='gray20',command=register_window)
regbutton.place(x=220, y=200)

forgetbutton = Button(frame, text='Forget Password?', font=('arial', 12,), bd=0, fg='red', bg='white',
                      cursor='hand2',
                      activebackground='white', activeforeground='gray20',command=reset_password)
forgetbutton.place(x=410, y=200)
loginButton2=Button(frame,text='Login',font=('arial',18,'bold'),fg='white',bg='gray20',cursor='hand2',activeforeground='gray20',command=signin)
loginButton2.place(x=420,y=220)





window.mainloop()
