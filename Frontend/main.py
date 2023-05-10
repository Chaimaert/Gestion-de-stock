from tkinter import *
from tkinter import messagebox
import requests
from dashboard import Dashboard2

root = Tk()
root.title('InventoryManagement System - Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

def signin(window=None):
    username = user.get()
    password = code.get()

    # Check if either username or password is empty
    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return

    response = requests.post('http://localhost:8000/api-token-auth/', data={'username': username, 'password': password})
    if response.status_code == 200:

        # open the dashboard window
        import dashboard
        window = Tk()
        Dashboard2(window)
        root.mainloop()
    else:
        messagebox.showerror("Invalid", "Invalid username or Password")
def forgot_password():
    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win.title('Forgot Password')
    win.configure(background='#f8f8f8')
    win.resizable(0, 0)

    # ====== Email ====================
    email_entry2 = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
    email_entry2.place(x=40, y=30, width=256, height=34)
    email_entry2.config(highlightbackground="black", highlightcolor="black")
    email_label2 = Label(win, text='• Email', fg="#89898b", bg='#f8f8f8',
                         font=("yu gothic ui", 11, 'bold'))
    email_label2.place(x=40, y=0)

    # ======== New Password ==================
    new_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
    new_password_entry.place(x=40, y=110, width=256, height=34)
    new_password_entry.config(highlightbackground="black", highlightcolor="black")
    new_password_label = Label(win, text='• New Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
    new_password_label.place(x=40, y=80)

    # ==========Confirm Password ==================
    confirm_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
    confirm_password_entry.place(x=40, y=190, width=256, height=34)
    confirm_password_entry.config(highlightbackground="black", highlightcolor="black")
    confirm_password_label = Label(win, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                                   font=("yu gothic ui", 11, 'bold'))
    confirm_password_label.place(x=40, y=160)

    # ======= Update password Button ============
    update_pass = Button(win, fg='#202020', text='Update Password', bg='#FFD500', font=("yu gothic ui bold", 14),
                         cursor='hand2', activebackground='#1b87d2')
    update_pass.place(x=40, y=240, width=256, height=50)

design_frame4 = Listbox(bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame4.place(x=676, y=106)

def hide():
    closeeyeButton.config(file="Images/closeeye.png")
    code.config(show='*')
    eyeButton.config(command=show)

def show():
    closeeyeButton.config(file="Images/openeye.png")
    code.config(show='')
    eyeButton.config(command=hide)

def signup_page():
    root.destroy()
    import Signup

"""------------------Image------------------------"""
img = PhotoImage(file="Images/logo.png")
Label(root, image=img, bg='grey', border=0).place(x=50, y=80)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign In', fg="#3B3B3B", bg="white", font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=120, y=3)

"""-----------------Username------------------------"""
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=50, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black",).place(x=45, y=107)

"""-----------------password-----------------------"""
def on_enter(e):
    code.delete(0, 'end')
def on_leave(e):
    name = code.get()
    if name == '':
        user.insert(0, 'Password')
code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
code.place(x=50, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black",).place(x=45, y=177)
closeeyeButton= PhotoImage(file="Images/closeeye.png")
eyeButton = Button(root, image=closeeyeButton, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=795, y=220)

"""--------------------Forgot Button------------------------"""
forgetButton = Checkbutton(text='Forgot Password ?', bd=0, bg='white', activebackground='white',
                           cursor='hand2', fg="#202020", font=("Microsoft YaHei UI Light", 9),
                           command=forgot_password)
forgetButton.place(x=720, y=255)

forgotPassword = Button(design_frame4, text='Forgot password', font=("yu gothic ui", 8, "bold underline"), bg='#f8f8f8',
                        borderwidth=0, activebackground='#f8f8f8', cursor="hand2")
forgotPassword.place(x=290, y=290)

""""--------------------Buttons-----------------------------"""
Login = Button(frame, width=20, pady=7, text='Sign in', bg='#FFD500', fg='white', border=0, command=signin).place(x=125, y=230)
label = Label(frame, text="Don't have an account ?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
label.place(x=95, y=280)

sign_up = Button(frame, width=6, text="Sign up", border=0, bg="white", cursor="hand2", fg="#FFD500", command=signup_page)
sign_up.place(x=240, y=280)



root.mainloop()
