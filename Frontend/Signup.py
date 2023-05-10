from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("InventoryManagement System - Sign Up")
window.geometry('925x500+300+200')
window.configure(bg="#fff")
window.resizable(False, False)
def login_page():
    window.destroy()
    import main
def signin():
    username = user.get()
    password = code.get()
    c_password = confirm_password.get()
    mail = email.get()

    if username != '' and password != '' and c_password != '' and mail != '' :
        messagebox.showerror("Invalid", "Refill the blanks please")

#------------------Image------------------------

img = PhotoImage(file="Images/logo.png")
Label(window, image=img, bg='grey', border=0).place(x=50, y=90)
frame = Frame(window, width=350, height=390, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign Up', fg="#3B3B3B", bg="white", font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=120, y=0)

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
eyeButton = Button(window, bd=0, bg='white', activebackground='white', cursor='hand2')
eyeButton.place(x=795, y=220)

"""-----------------Confirm password-----------------------"""
def on_enter(e):
    confirm_password.delete(0, 'end')
def on_leave(e):
    if confirm_password.get() == '':
        confirm_password.insert(0, 'Confirm Password')

confirm_password = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
confirm_password.place(x=44, y=210)
confirm_password.insert(0, ' Confirm Password')
confirm_password.bind('<FocusIn>', on_enter)
confirm_password.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black",).place(x=45, y=240)

eButton2 = Button(window, bd=0, bg='white', activebackground='white', cursor='hand2')
eButton2.place(x=795, y=280)

"""-----------------Email------------------------"""
def on_enter(e):
    email.delete(0, 'end')
def on_leave(e):
    mail = email.get()
    if email == '':
        mail.insert(0, 'Email')

email = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
email.place(x=50, y=275)
email.insert(0, 'Email')
email.bind('<FocusIn>', on_enter)
email.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black",).place(x=45, y=300)

""""--------------------Buttons------------------------"""
Button(frame, width=39, pady=7, text='Sign Up', bg='#FFD500', fg='white', border=0, command=signin).place(x=55, y=330)
label = Label(frame, text=" I have an account ! ", fg="black",bg="white", font=("Microsoft YaHei UI Light", 9))
label.place(x=95, y=370)

sign_in = Button(frame, width=6, text="Sign in", border=0, bg="white", cursor="hand2", fg="#FFD500", command=login_page)
sign_in.place(x=220, y=370)



window.mainloop()