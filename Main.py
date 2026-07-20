# This is all the librabries that are used in this application
import os
import csv
import tkinter as tk
from tkinter import messagebox
# UDF stands for user database file for the passwords and usernames of this application
UDF = "users.csv"
# basically means if the file or folder doesn not exists it will create the file with the username and password columns in the 
if not os.path.exists(UDF):
    with open(UDF, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["username", "password"])

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Priority app")
        self.geometry("500x450")
        self.configure(bg="#00636e")

        self.current_user = None

        self.login_page()

    def clean_open(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    def login_page(self):
        self.clean_open()

        self.configure(bg="#00636e")

        header_frame = tk.Frame(self, bg="#00636e")
        header_frame.pack(fill="x", padx=10, pady=(5, 0))

        header_frame.grid_columnconfigure(0, weight=1)
        header_frame.grid_columnconfigure(1, weight=1)
        header_frame.grid_columnconfigure(2, weight=1)

        # new thing i found was this hasattr which is short for has attribute basically checks if an object contains a specific atrribute or method.
        if not hasattr(self, 'FAQ_icon'):
            try:
                self.FAQ_icon = tk.PhotoImage(file="FAQbutton.png")
            except tk.TclError:
                self.FAQ_icon = None
        
        if not hasattr(self, 'logo'):
            try:
                self.logo = tk.PhotoImage(file="logo.png")
            except tk.TclError:
                self.logo = None

        if self.logo:
            logo_label = tk.Label(header_frame, image=self.logo, bg="#00636e")
            logo_label.grid(row=0, column=1, pady=5)

        FAQ_button = tk.Button(header_frame, image=self.FAQ_icon, font=("Calibri", 10,"bold"), bg="#00ccd1", fg="white",
                                     command=self.open_FAQ_file)
        FAQ_button.grid(row=0, column=2, sticky="e", pady=5)        
        
        label_title = tk.Label(self, text="Time to focus?", font=("Calibri", 25, "bold"), bg="#00636e", fg="#ffffff")
        label_title.pack(pady=(0, 5))
        
        tk.Label(self, text="Username", font=("Calibri", 10), bg="#ffffff", fg="#000000").pack(anchor="w", padx=50)
        self.username = tk.Entry(self, font=("Calibri", 12),)
        self.username.pack(fill="x", padx=50, pady=(2, 5))

        tk.Label(self, text="Password", font=("Calibri", 10), bg="#ffffff", fg="#000000").pack(anchor="w", padx=50)
        self.password = tk.Entry(self, font=("Calibri", 12),)
        self.password.pack(fill="x", padx=50, pady=(2, 10))

        login_button = tk.Button(self, text="Login", font=("Calibri", 12, "bold"), bg="#00ccd1", fg="white",
                                command=self.handle_login)
        login_button.pack(fill="x", padx=50, pady=5)

        #CU_button stands for the create user button
        CU_Button = tk.Button(self, text="Create Account", font=("Calibri", 12, "bold"), bg="#00ccd1", fg="white",
                                command=self.CU_page)
        CU_Button.pack(fill="x", padx=50, pady=5)

    def CU_page(self):
        self.clean_open()
        label_title = tk.Label(self, text="Create an acoount here!", font=("Calibri", 25, "bold"), bg="#6ba1c7", fg="#b8c5ce")
        label_title.pack(pady=(40,20))

        tk.Label(self, text="Create an Username", font=("Calibri", 10), bg="#ffffff", fg="#000000").pack(anchor="w", padx=50)
        self.username = tk.Entry(self, font=("Calibri", 12))
        self.username.pack(fill="x", padx=50, pady=(5, 15))

        tk.Label(self, text="Create a Password", font=("Calibri", 10), bg="#ffffff", fg="#000000").pack(anchor="w", padx=50)
        self.password = tk.Entry(self, font=("Calibri", 12),)
        self.password.pack(fill="x", padx=50, pady=(5, 20))

        register = tk.Button(self, text="Sign Up", font=("Calibri", 12, "bold"), bg="#00ccd1", fg="white",
                                command=self.handle_register)
        register.pack(fill="x", padx=50, pady=10)

        CU_Button = tk.Button(self, text="Already got one!", font=("Calibri", 12, "bold"), bg="#00ccd1", fg="white",
                                command=self.login_page)
        CU_Button.pack(fill="x", padx=50, pady=10)

    def main_menu(self):
        self.clean_open()
        self.geometry("700x500")
        self.configure(bg="#ffffff")


        try:
            self.FAQ_icon = tk.PhotoImage(file="FAQbutton.png")
            self.Settings_icon = tk.PhotoImage(file="Settingsbutton.png")
            self.picon = tk.PhotoImage(file="Prioritiesbutton.png")
            self.aicon = tk.PhotoImage(file="ATARButton.png")
            self.UEicon = tk.PhotoImage(file="UEbutton.png")
        except tk.TclError:
            messagebox.showerror("Error 1: madhava has forgotten to put correct image files!")
            return

        self.grid_columnconfigure(0, weight=1, uniform="main_feats")
        self.grid_columnconfigure(1, weight=1, uniform="main_feats")
        self.grid_columnconfigure(2, weight=1, uniform="main_feats")

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)

        top_bar = tk.Frame(self, bg="#ffffff")
        top_bar.grid(row=0, column=0, columnspan=3, sticky="ew", padx=20, pady=10)

        logo_welcome = tk.Frame(top_bar, bg="#ffffff")
        logo_welcome.pack(side="left", anchor="w")

        if self.logo:
            mm_logo = tk.Label(top_bar, image=self.logo, bg="#ffffff")
            mm_logo.pack(side="left", padx=(0,10))

        welcome_message = f"Welcome, {self.current_user if self.current_user else 'Error 2'}!"
        welcome_label = tk.Label(top_bar, text=welcome_message, font=("Calibri", 14, "bold"),
                                 bg="#ffffff", fg="#00636e")
        welcome_label.pack(side="left")

        faq_sttg = tk.Frame(top_bar, bg="#ffffff")
        faq_sttg.pack(side="right", anchor="e")
        settings_button = tk.Button(faq_sttg, image=self.Settings_icon, font=("Calibri", 10,"bold"), bg="#00ccd1", fg="white",
                                     command=self.open_settings_file)
        settings_button.pack(side="right", padx=(5, 0))

        FAQ_button = tk.Button(faq_sttg, image=self.FAQ_icon, font=("Calibri", 10,"bold"), bg="#00ccd1", fg="white",
                                     command=self.open_FAQ_file)
        FAQ_button.pack(side="right", padx=(5, 0))

        # pbtn stands for priority button just to simplify it i made it like this
        pbtn = tk.Button(self, image=self.picon, text="\nPriorities", font=("Calibri", 14,"bold"), bg="#00ccd1", fg="white",
                                    activebackground="#00a3a6", activeforeground="white", compound="top", command=self.priorities)
        pbtn.grid(row=2, column=0, sticky="nsew", padx=20,  pady=20)

        #abtn stands for ATAR Calculator butotn for the same reason as above
        abtn = tk.Button(self, image=self.aicon, text="\nATAR Calculator", font=("Calibri", 14,"bold"), bg="#00ccd1", fg="white",
                                    activebackground="#00a3a6", activeforeground="white", compound="top", command=self.atar_calc)
        abtn.grid(row=2, column=1, sticky="nsew", padx=20,  pady=20)

        # UEbtn stands for upcoming events for a reason i think is quite well known.
        UEbtn = tk.Button(self, image=self.UEicon, text="\nUpcoming Events", font=("Calibri", 14,"bold"), bg="#00ccd1", fg="white",
                                    activebackground="#00a3a6", activeforeground="white", compound="top", command=self.events_p)
        UEbtn.grid(row=2, column=2, sticky="nsew", padx=20,  pady=20)

        logout_button = tk.Button(self, text="Log out", font=("Calibri", 12, "bold"), bg="#00ccd1", fg="white",
                                activebackground="#00a3a6", activeforeground="white", command=self.handle_logout)
        logout_button.grid(row=3, column=0, sticky="nw", padx=20, pady=20)

    def open_FAQ_file(self):
        self.clean_open()
        import FAQPage

        arrivalPage = "main_menu" if self.current_user else "login"
        FAQPage.load_FAQ_page(self, arrivalPage)

    def open_settings_file(self):
        self.clean_open()
        
        import SettingsPage

        SettingsPage.load_settings_page(self)

    def priorities(self):
        self.clean_open()

        import Priorities

        Priorities.load_priorities_page(self)

    def atar_calc(self):
        self.clean_open()

        import ATAR_Calculator

        ATAR_Calculator.load_atar_page(self)


    def events_p(self):
        self.clean_open()

        import UEPage

        UEPage.load_UE_Page(self)

    def handle_login(self):
        # the c stands for correct
        cusername = self.username.get().strip()
        cpassword = self.password.get().strip()

        if not cusername or not cpassword:
            messagebox.showwarning("error", "wrong you have to enter everything")
            return
        
        valid_user = False
        with open(UDF, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row ['username'] == cusername and row['password'] == cpassword:
                    valid_user = True
                    break

        if valid_user:
            self.current_user = cusername
            self.main_menu()
        else:
            messagebox.showerror("Wrong something", "Invalid username or password fix it to enter.")
    
    def handle_register(self):
        cusername = self.username.get().strip()
        cpassword = self.password.get().strip()

        if not cusername or not cpassword:
            messagebox.showwarning("Error","no blanks")
            return
        
        with open(UDF, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == cusername:
                    messagebox.showerror("invalid", "username already in use")
                    return
                
        with open(UDF, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([cusername, cpassword])

        messagebox.showinfo("success", "account created")
        self.login_page()

    def handle_logout(self):
        self.clean_open()
        self.current_user = None
        self.geometry("500x450")
        self.configure(bg="#00636e")
        self.login_page()

if __name__ == "__main__":
    app = App()
    app.mainloop()