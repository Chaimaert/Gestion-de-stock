from tkinter import *
import requests
import os

class Dashboard2:
    def __init__(self, window):
        self.window = window

        # Window Size and Placement
        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_height()
        app_width = 1340
        app_height = 690
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 160) - (app_height / 160)
        window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")



        # Navigating through windows
        homepage = Frame(window)
        dashboard_page = Frame(window)

        for frame in (homepage, dashboard_page):
            frame.grid(row=0, column=0, sticky='nsew')
        def show_frame(frame):
            frame.tkraise()


        show_frame(homepage)

        # ======================================== HOME PAGE =====================================================
        homepage.config(background='#eee')

        # ====== MENU BAR ==========
        # logoIcon = PhotoImage(file='Images/hyy.png')
        # Label(homepage, image=logoIcon, bg='grey', border=0).place(x=0, y=0)

        menuBar_line = Canvas(homepage, width=1500, height=1.5, bg="#B2AFAC", highlightthickness=0)
        menuBar_line.place(x=0, y=60)

        #home_bgImg = PhotoImage(file='Images/hyy.png')
        #Label(homepage, image=home_bgImg, bg='#ffffff').place(x=0, y=60)

        #brandIcon = PhotoImage(file='Images/hyy.png')
        #Label(homepage, image=brandIcon, bg='black').place(x=1085, y=83)

        # Make GET request to API to retrieve admin name
        response = requests.get('http://localhost:8000/api-token-auth/', headers={'Authorization': 'Bearer your-token'})
        if response.status_code == 200:
            admin_name = response.json()['username']
        else:
            admin_name = 'Unknown'  # or handle the error in a different way

        # --------------------------Update the text of admLabel with the admin name------------------------
        admLabel = Label(homepage, text=f'{admin_name}', font=('yu gothic ui', 18, 'bold'), fg='#ffc329', bg='#eee')
        admLabel.place(x=1150, y=11)

        heading = Label(homepage, text='© STOCK SYSTEM', bg='#eee', fg='black',
                        font=("yu gothic ui", 19, "bold"))
        heading.place(x=1150, y=90)

        # ========================================= HOME BUTTON =============================================
        # ========== Frame1 =================
        back = Frame(homepage, bg="#B2AFAC")
        back.place(x=58, y=10, width=100, height=50)

        home_button = Button(homepage, text='Home',border=0, bg='#eee', font=("", 16, "bold"), bd=0, fg='black',
                             cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        home_button.place(x=70, y=15)

        # ===================================== Products BUTTON ==============================================
        def product():
            window.withdraw()
            os.system("python products.py")
            window.destroy()

        product_button = Button(homepage, text='Products', border=0, bg='#eee', font=("", 16, "bold"), bd=0, fg='black',
                                cursor='hand2', activebackground='#fd6a36', activeforeground='white', command=product)
        product_button.place(x=170, y=15)

        # ======================================= Brands BUTTON ==============================================
        def brand():
            window.withdraw()
            os.system("python Brands.py")
            window.destroy()
        brand_button = Button(homepage, text='Brands', border=0, bg='#eee', font=("", 16, "bold"), bd=0, fg='black',
                                cursor='hand2', activebackground='#fd6a36', activeforeground='white', command=brand)
        brand_button.place(x=290, y=15)

        # ========== Customers BUTTON =======
        def customer():
            window.withdraw()
            os.system("python Customers.py")
            window.destroy()
        customer_button = Button(homepage, text='Customers', border=0, bg='#eee', font=("", 16, "bold"), bd=0,
                                 fg='black', cursor='hand2', activebackground='#fd6a36', activeforeground='white',
                                 command=customer)
        customer_button.place(x=390, y=15)

        # ================================= Admins BUTTON =============================
        admin_button = Button(homepage, text='Admin', border=0, bg='#eee', font=("", 16, "bold"), bd=0,
                                 fg='black',
                                 cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        admin_button.place(x=520, y=15)

        # ========================== Inventories BUTTON ================================
        inventory_button = Button(homepage, text='Inventories', border=0, bg='#eee', font=("", 16, "bold"), bd=0,
                                 fg='black',
                                 cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        inventory_button.place(x=620, y=15)


        # ================================ LOG OUT ======================================
        logout_button = Button(homepage, text='Logout',  border=0, bg='#eee', font=("", 16, "bold"), bd=0,
                                 fg='black',
                                 cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        logout_button.place(x=1250, y=15)

        # ==================== Frame1 =======================
        frame1 = Frame(homepage, bg="#42413D")
        frame1.place(x=50, y=90, width=310, height=220)

        total_people = Label(frame1, text='230', bg='#42413D', font=("", 25, "bold"))
        total_people.place(x=120, y=100)

        """totalPeopleImage = Image.open('Images/client.png')
        photo = ImageTk.PhotoImage(totalPeopleImage)
        logo = Label(frame1, image=photo, bg="#42413D")
        logo.image = photo
        logo.place(x=220, y=0)"""

        totalPeople_label = Label(frame1, text="Client", bg='#42413D', font=("", 18, "bold"),
                                  fg='white')
        totalPeople_label.place(x=10, y=25)

        # ================== Frame2 =====================
        frame2 = Frame(homepage, bg="#42413D")
        frame2.place(x=450, y=90, width=310, height=220)

        total_product = Label(frame2, text='230', bg='#42413D', font=("", 25, "bold"))
        total_product.place(x=120, y=100)

        """totalProductImage = Image.open('Images/package.png')
        photo = ImageTk.PhotoImage(totalProductImage)
        logo = Label(frame2, image=photo, bg="#42413D")
        logo.image = photo
        logo.place(x=220, y=0)"""

        totalProduct_label = Label(frame2, text="Products", bg='#42413D', font=("", 18, "bold"),
                                  fg='white')
        totalProduct_label.place(x=10, y=25)

        # ========== Frame3 =======
        frame3 = Frame(homepage, bg="#42413D")
        frame3.place(x=50, y=390, width=310, height=220)

        total_earning = Label(frame3, text="40,000.00", bg='#42413D', font=("", 25, "bold"))
        total_earning.place(x=90, y=100)

        #====================Image====================
        """totalEarningImage = Image.open('Images/earning.png')
        photo = ImageTk.PhotoImage(totalEarningImage)
        logo = Label(frame3, image=photo, bg="#42413D")
        logo.image = photo
        logo.place(x=220, y=0)
        """

        #====================Earnings====================

        totalEarning_label = Label(frame3, text="Total Earning", bg='#42413D', font=("", 18, "bold"),
                                   fg='white')
        totalEarning_label.place(x=10, y=25)

        # =================== Frame4 ========================
        frame4 = Frame(homepage, bg="#42413D")
        frame4.place(x=450, y=390, width=310, height=220)

        total_inventory = Label(frame4, text='230', bg='#42413D', font=("", 25, "bold"))
        total_inventory.place(x=120, y=100)

        """totalInventoryImage = Image.open('Images/inventory.png')
        photo = ImageTk.PhotoImage(totalInventoryImage)
        logo = Label(frame4, image=photo, bg="#42413D")
        logo.image = photo
        logo.place(x=220, y=0)"""


        totalInventory_label = Label(frame4, text="Inventories", bg='#42413D', font=("", 18, "bold"),
                                   fg='white')
        totalInventory_label.place(x=10, y=25)



def wind():
    window = Tk()
    Dashboard2(window)
    window.mainloop()


if __name__ == '__main__':
    wind()
