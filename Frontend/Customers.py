from tkinter import *
import tkinter as tk
import requests
import os
from tkinter import messagebox
from tkinter import filedialog

class CustomerPage:
    def __init__(self, customer_page):
        self.customer_page = customer_page

        # Window Size and Placement
        customer_page.rowconfigure(0, weight=1)
        customer_page.columnconfigure(0, weight=1)
        screen_width = customer_page.winfo_screenwidth()
        screen_height = customer_page.winfo_height()
        app_width = 1366
        app_height = 750
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 160) - (app_height / 160)
        customer_page.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        customer_page.title("Stock Management System - Customer")

        # Navigating through windows
        homepage = Frame(customer_page)
        dashboard_page = Frame(customer_page)

        for frame in (homepage, dashboard_page):
            frame.grid(row=0, column=0, sticky='nsew')

        def show_frame(frame):
            frame.tkraise()

        show_frame(homepage)

        # ============================== HOME PAGE ========================================================
        homepage.config(background='#eee')

        # ====== MENU BAR ==========
        # logoIcon = PhotoImage(file='Images/hyy.png')
        # Label(homepage, image=logoIcon, bg='grey', border=0).place(x=0, y=0)

        menuBar_line = Canvas(homepage, width=1500, height=1.5, bg="#6C757D", highlightthickness=0)
        menuBar_line.place(x=0, y=60)

        # home_bgImg = PhotoImage(file='Images/hyy.png')
        # Label(homepage, image=home_bgImg, bg='#ffffff').place(x=0, y=60)

        # brandIcon = PhotoImage(file='Images/hyy.png')
        # Label(homepage, image=brandIcon, bg='black').place(x=1085, y=83)

        # Make GET request to API to retrieve admin name
        response = requests.get('http://localhost:8000/api-token-auth/', headers={'Authorization': 'Bearer your-token'})
        if response.status_code == 200:
            admin_name = response.json()['name']
        else:
            admin_name = 'Unknown'  # or handle the error in a different way

        # Update the text of admLabel with the admin name
        admLabel = Label(homepage, text=f'{admin_name}', font=('yu gothic ui', 18, 'bold'), fg='#ffc329', bg='#eee')
        admLabel.place(x=1120, y=13)

        heading = Label(homepage, text='© STOCK SYSTEM', bg='#eee', fg='#FFC300',
                        font=("yu gothic ui", 19, "italic"))
        heading.place(x=1140, y=650)

        # ========== HOME BUTTON ======================
        # ============ Frame1 ==========

        home_button = Button(homepage, text='Home', border=0, bg='#eee', font=("", 16, "bold"), bd=0, fg='black',
                             cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        home_button.place(x=70, y=15)

        # ========== PRODUCTS BUTTON ===================

        product_button = Button(homepage, text='Products', border=0, bg='#eee', font=("", 16, "bold"), bd=0, fg='black',
                                cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        product_button.place(x=170, y=15)

        # ========== Brands BUTTON =======
        brand_button = Button(homepage, text='Brands', border=0, bg='#eee', font=("", 16, "bold"), bd=0, fg='black',
                              cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        brand_button.place(x=290, y=15)

        # ========== Customers BUTTON =======
        back = Frame(homepage, bg="#B2AFAC")
        back.place(x=389, y=10, width=125, height=50)
        customer_button = Button(homepage, text='Customers', border=0, bg='#eee', font=("", 16, "bold"), bd=0,
                                 fg='black',
                                 cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        customer_button.place(x=390, y=15)

        # ========== Admins BUTTON =======
        admin_button = Button(homepage, text='Admin', border=0, bg='#eee', font=("", 16, "bold"), bd=0,
                              fg='black',
                              cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        admin_button.place(x=520, y=15)

        # ========== Inventories BUTTON =======
        inventory_button = Button(homepage, text='Inventories', border=0, bg='#eee', font=("", 16, "bold"), bd=0,
                                  fg='black',
                                  cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        inventory_button.place(x=620, y=15)

        # ========== LOG OUT =======
        logout_button = Button(homepage, text='Logout', border=0, bg='#eee', font=("", 16, "bold"), bd=0,
                               fg='black',
                               cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        logout_button.place(x=1250, y=15)

        #Set the title of the window
        title_label = tk.Label(homepage, text='List of Customers', bg='#eee', fg='black', font=("yu gothic ui", 19, "italic"))
        title_label.place(x=500, y=90)

        # ========== ADD CUSTOMER =======
        frame1 = Frame(homepage, bg="#6C757D")
        frame1.place(x=0, y=70, width=400, height=1000)

        frame1_title = Label(frame1, text='Add Customer', bg='#6C757D', font=("yu gothic ui", 25, "bold"))
        frame1_title.place(x=80, y=20)

        # ========== ADD CUSTOMER Name =======
        frame1_name = Label(frame1, text='Full name :', bg='#6C757D', font=("yu gothic ui", 15, "bold"))
        frame1_name.place(x=20, y=90)
        frame1_entry = Entry(frame1, bg="#6C757D")
        frame1_entry.place(x=155, y=100)

        # ========== ADD CUSTOMER Email =======
        frame1_name = Label(frame1, text='Email :', bg='#6C757D', font=("yu gothic ui", 15, "bold"))
        frame1_name.place(x=20, y=140)
        frame1_entry = Entry(frame1, bg="#6C757D")
        frame1_entry.place(x=150, y=149)

        # ========== ADD CUSTOMER Phone =======
        frame1_name = Label(frame1, text='Phone :', bg='#6C757D', font=("yu gothic ui", 15, "bold"))
        frame1_name.place(x=20, y=190)
        frame1_entry = Entry(frame1, bg="#6C757D")
        frame1_entry.place(x=150, y=199)

        # ========== ADD CUSTOMER Adresse =======
        frame1_name = Label(frame1, text='Adresse :', bg='#6C757D', font=("yu gothic ui", 15, "bold"))
        frame1_name.place(x=20, y=240)
        frame1_entry = Entry(frame1, bg="#6C757D")
        frame1_entry.place(x=150, y=252)

        # ========== ADD CUSTOMER Button =======
        frame1_button = Button(frame1, text='Submit', bg='#6C757D', font=("yu gothic ui", 15, "italic"))
        frame1_button.place(x=70, y=320, height=40, width=200)


        # create a Listbox widget
        customer_listbox = Listbox(homepage, width=90, height=15, font=("yu gothic ui", 12))
        customer_listbox.place(x=450, y=135)

        # fetch customer data from the API
        response = requests.get('http://127.0.0.1:8000/api/Customer/')
        print(response.json)
        #customers = response.json()

        # iterate through the customers and add each one to the Listbox
        """for customer in customers:
            name = customer['user_name']
            email = customer['email']
            phone = customer['phone_num']
            address = customer['address']
            # concatenate the customer data into a single string
            customer_data = f"{name} | {email} | {phone} | {address}"
            # add the customer data to the Listbox
            customer_listbox.insert(END, customer_data)"""



def page():
    window = Tk()
    CustomerPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()