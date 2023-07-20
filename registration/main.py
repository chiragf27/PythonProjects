from tkinter import *
from tkinter import messagebox
import ast

root = Tk()
root.title('Login Form - SignIn')
root.geometry('915x450+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

def signin():
    username = user.get()
    password = code.get()

    file=open('data.txt', 'r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()



    if username in r.keys() and password == r[username]:
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('915x430+300+200')
        screen.config(bg="white")

        Label(screen, text="Hello World", bg="#fff", font=('SF Pro Display', 23, 'bold')).pack(expand=False)

        screen.mainloop()

    else:
        messagebox.showerror("Invalid", "Invalid Username or Password")

#############################################################
def signup_cmd():
    window = Toplevel(root)
    window.title("Login Form - SignUp")
    window.geometry('915x450+300+200')
    window.configure(bg="#fff")
    window.resizable(False, False)


    def signup():
        username = user.get()
        password = code.get()
        confirm_password = confirm_code.get()

        if password == confirm_password:
            try:
                file = open('data.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username: password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open('data.txt', 'w')
                w = file.write(str(r))

                messagebox.showinfo('Sign Up', 'Successfully signed up')
                window.destroy()

            except:
                file = open('data.txt', 'w')
                pp = str({'Username': 'password'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror("Invalid", "Both Password should match")


    def sign():
        window.destroy()


    img = PhotoImage(file="signup.png")
    Label(window, image=img, border=0, bg='white').place(x=50, y=90)

    frame = Frame(window, width=350, height=390, bg='white')
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign Up', fg="black", bg='white', font=('SF Pro Display', 23, 'bold'))
    heading.place(x=125, y=5)


    def on_enter(e):
        user.delete(0, 'end')


    def on_leave(e):
        name = user.get()
        if name == ' ':
            user.insert(0, 'Username')


    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('SF Pro Display', 11, 'bold'))
    user.place(x=30, y=83)
    user.insert(0, "Username")
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black', ).place(x=25, y=107)


    def on_enter(e):
        code.delete(0, 'end')


    def on_leave(e):
        name = code.get()
        if name == ' ':
            code.insert(0, 'Password')


    code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('SF Pro Display', 11))
    code.place(x=30, y=133)
    code.insert(0, "Password")
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusIn>', on_enter)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=157)


    def on_enter(e):
        confirm_code.delete(0, 'end')


    def on_leave(e):
        name = confirm_code.get()
        if name == ' ':
            confirm_code.insert(0, 'Confirm Password')


    confirm_code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('SF Pro Display', 11))
    confirm_code.place(x=30, y=183)
    confirm_code.insert(0, "Confirm Password")
    confirm_code.bind('<FocusIn>', on_enter)
    confirm_code.bind('<FocusIn>', on_enter)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=207)

    Button(frame, width=30, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, font=('SF Pro Display', 11),
           command=signup).place(x=35, y=250)

    label = Label(frame, text="Already have an account?", fg='black', bg='white', font=('SF Pro Display', 11))
    label.place(x=40, y=300)

    sign_up = Button(frame, width=8, text='Sign In', border=0, bg='white', cursor='hand2', fg='#57a148',
                     font=('SF Pro Display', 11), command=sign)
    sign_up.place(x=218, y=297)

    window.mainloop()
##############################################################

img = PhotoImage(file='signin.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)
heading=Label(frame, text='Sign In', fg='black', bg='white', font=('SF Pro Display', 23, 'bold'))
heading.place(x=125, y=5)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name==' ':
        user.insert(0, 'Username')

user=Entry(frame, width=25, fg='black', border=0, bg="white", font=('SF Pro Display', 11))
user.place(x=30, y=83)
user.insert(0, "Username")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name==' ':
        code.insert(0, 'Password')

code=Entry(frame, width=25, fg='black', border=0, bg="white", font=('SF Pro Display', 11))
code.place(x=30, y=133)
code.insert(0, "Password")
code.bind('<FocusIn>', on_enter)
code.bind('<FocusIn>', on_enter)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=157)

Button(frame, width=30, pady=7, text='Sign In', bg='#57a1f8', fg='white', border=0, font=('SF Pro Display', 11), command=signin).place(x=35, y=185)
label=Label(frame, text="Don't have an account?", fg='black', bg='white', font=('SF Pro Display', 11))
label.place(x=55, y=240)

sign_up = Button(frame, width=8, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a148', font=('SF Pro Display', 11), command=signup_cmd)
sign_up.place(x=218, y=237)

root.mainloop()