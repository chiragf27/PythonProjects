from tkinter import *
from tkinter import messagebox
import ast
import random
import json
import pyperclip

ENTRY_COLOR = "#FFFAFA"
BUTTON_COLOR = "#F0FFF0"

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
        # # ---------------------------- PASSWORD GENERATOR ------------------------------- #
        def generate_password():
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            n_letters = random.randint(8, 10)
            n_symbols = random.randint(2, 4)
            n_numbers = random.randint(2, 4)

            password_letters = [random.choice(letters) for _ in range(n_letters)]
            password_symbols = [random.choice(symbols) for _ in range(n_symbols)]
            password_numbers = [random.choice(numbers) for _ in range(n_numbers)]
            password_lists = password_letters + password_symbols + password_numbers

            random.shuffle(password_lists)
            password = "".join(password_lists)
            password_entry.insert(0, password)
            pyperclip.copy(password)
            messagebox.showinfo(title="Password", message="Password copied to clipboard")

        # ---------------------------- SAVE PASSWORD ------------------------------- #
        def save():
            website = website_entry.get()
            email = email_entry.get()
            password = password_entry.get()
            new_data = {
                website: {
                    "email": email,
                    "password": password
                }
            }

            if len(website) == 0 or len(password) == 0:
                messagebox.showinfo(title="Error", message=f"{username} Please don't leave any of the fields empty!")
            else:
                is_ok = messagebox.askokcancel(title=website,
                                               message=f"These are the details entered: \nEmail: {email} \nPassword: {password}\n Is is ok to save?")
                if is_ok:
                    try:
                        with open(f"{username}.json", "r") as data_file:
                            # read old data
                            data = json.load(data_file)
                    except FileNotFoundError:
                        with open(f"{username}.json", "w") as data_file:
                            json.dump(new_data, data_file, indent=4)
                    else:
                        # update old data with new data
                        data.update(new_data)
                        with open(f"{username}.json", "w") as data_file:
                            # saving updated data
                            json.dump(data, data_file, indent=4)
                    finally:
                        website_entry.delete(0, END)
                        password_entry.delete(0, END)
                        email_entry.delete(0, END)

        # ---------------------------- FIND PASSWORD ------------------------------- #
        def find_password():
            website = website_entry.get()
            try:
                with open(f"{username}.json") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                messagebox.showinfo(title="Error", message="No data file found! [Seems like you are using Password Manager for the first time, Add some passwords first]")
            else:
                if website in data:
                    email = data[website]["email"]
                    password = data[website]["password"]
                    messagebox.showinfo(title=f"Password for {website}",
                                        message=f"Email: {email}\nPassword: {password}")
                else:
                    messagebox.showinfo(title="Error", message=f"The details for the {website} are not saved")

        # ---------------------------- UI SETUP ------------------------------- #

        screen = Toplevel(root)
        screen.title("Password Manager")
        screen.geometry('670x450')
        screen.configure(bg="#fff")
        screen.resizable(False, False)

        logo_img = PhotoImage(file="password.png")
        Label(screen, image=logo_img, width=250, height=250, bg='white').place(x=215, y=5)

        frame = Frame(screen, width=500, height=200, bg='white')
        frame.place(x=90, y=230)

        website_label = Label(frame, text="Website:", fg="black", bg='white', font=('SF Pro Display', 11, 'bold'))
        website_label.place(x=20, y=15)

        email_label = Label(frame, text="Email/Username:", fg="black", bg='white', font=('SF Pro Display', 11, 'bold'))
        email_label.place(x=5, y=45)

        password_label = Label(frame, text="Password:", fg="black", bg='white', font=('SF Pro Display', 11, 'bold'))
        password_label.place(x=20, y=75)

        website_entry = Entry(frame, width=20, fg='black', border=2, bg=ENTRY_COLOR, font=('SF Pro Display', 11, 'bold'))
        website_entry.place(x=140, y=15)
        website_entry.focus()

        email_entry = Entry(frame, width=35, fg='black', border=2, bg=ENTRY_COLOR, font=('SF Pro Display', 11, 'bold'))
        email_entry.place(x=140, y=45)


        password_entry = Entry(frame, width=20, fg='black', border=2, bg=ENTRY_COLOR, font=('SF Pro Display', 11, 'bold'))
        password_entry.place(x=140, y=75)

        search_button = Button(frame, text="Search", highlightthickness=0, width=15, command=find_password, font=('SF Pro Display', 11), bg=BUTTON_COLOR).place(x=350, y=15)

        password_button = Button(frame, text="Generate Password", highlightthickness=0, command=generate_password, font=('SF Pro Display', 11), bg=BUTTON_COLOR).place(x=350, y=75)

        add_button = Button(frame, width=30, pady=5, text='Add', bg='#fff', fg='black', border=2, font=('SF Pro Display', 11), command=save).place(x=100, y=120)

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
           command=signup, borderwidth=0).place(x=35, y=250)

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

Button(frame, width=30, pady=7, text='Sign In', bg='#57a1f8', fg='white', border=0, font=('SF Pro Display', 11), command=signin, borderwidth=0).place(x=35, y=185)
label=Label(frame, text="Don't have an account?", fg='black', bg='white', font=('SF Pro Display', 11))
label.place(x=55, y=240)

sign_up = Button(frame, width=8, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a148', font=('SF Pro Display', 11), command=signup_cmd)
sign_up.place(x=218, y=237)

root.mainloop()