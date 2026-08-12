# This is all the librabries that are used in this application
import os
import csv
import tkinter as tk
from tkinter import messagebox
# UDF stands for user database file for the passwords and usernames of this application
user_data_file = "users.csv"
# basically means if the file or folder doesn not exists it will create the file with the username and password columns in the csv file
if not os.path.exists(user_data_file):
    with open(user_data_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["username", "password"])
# this is the calss that opens the login page & main menu and all the application that can be accessed through the main menu
class App(tk.Tk):
    def __init__(self): 
        super().__init__()
        self.title("Priority app") # The titel of the window that will appear in the top left along with the os
        self.geometry("500x450") # the size of the login page window and the creation of ascount
        self.configure(bg="#00636e") # The background color of the login page

        self.current_user = None # no one is logged data

        self.login_page() # calls the login page
# clean the window so that it is fresh every time i do enter the window
    def clean_open(self):
        for widget in self.winfo_children(): # completely clears or resets a specific section of the gui so frees memeory to speed up the processes
            widget.destroy()
    
    def login_page(self): # the login page being created so it appears first
        self.clean_open() # clears the elemetns of the gui

        self.configure(bg="#00636e") # background of the login page

        header_frame = tk.Frame(self, bg="#00636e") # basically the top part of the login page with the faq and logo's background
        header_frame.pack(fill="x", padx=10, pady=(5, 0)) # the layout of the top bar as it is seperate from the login pgae and its dimensions

        header_frame.grid_columnconfigure(0, weight=1) # basically the placeholders for the elemets so they share the same amount of the gui 
        header_frame.grid_columnconfigure(1, weight=1) # they are split evenly so they are perfect layout placheloders
        header_frame.grid_columnconfigure(2, weight=1)

        # new thing i found was this hasattr which is short for has attribute basically checks if an object contains a specific atrribute or method.
        if not hasattr(self, 'FAQ_icon'):
            try:
                self.FAQ_icon = tk.PhotoImage(file="FAQbutton.png") # the picture for the faq button
            except tk.TclError: #If it doesnt load it will automatically give an error message and show nothin
                self.FAQ_icon = None
        
        if not hasattr(self, 'logo'): # same thing as above but this time for the logo thats on the login page
            try:
                self.logo = tk.PhotoImage(file="logo.png") # the image file for the logo to appear on the login page
            except tk.TclError:
                self.logo = None # if it doesnt load same thing as the one for the faq icon it wont load and it will show error message

        if self.logo:
            logo_label = tk.Label(header_frame, image=self.logo, bg="#00636e") # a seperate frame for the logo and the background same as other
            logo_label.grid(row=0, column=1, pady=5) # the padding of this frame and size 

        FAQ_button = tk.Button(header_frame, image=self.FAQ_icon, font=("Calibri", 10,"bold"), bg="#00ccd1", fg="white",
                                     command=self.open_FAQ_file) # the btton for the faw button in the top right and the colors and action it will do
        FAQ_button.grid(row=0, column=2, sticky="e", pady=5) # the padding of the botton in top right took me some time this one and its padding
        
        label_title = tk.Label(self, text="Time to focus?", font=("Calibri", 25, "bold"), bg="#00636e", fg="#ffffff") # the title of the window and the color that is the title in the top middle of the screen
        label_title.pack(pady=(0, 5)) # padding of this adds whitespcce to top and bottom of title
        # the username title above the user entry for the username
        tk.Label(self, text="Username", font=("Calibri", 10), bg="#ffffff", fg="#000000").pack(anchor="w", padx=50) # alsong with the psotion of this label
        self.username = tk.Entry(self, font=("Calibri", 12),) # the user entry textbox so the user can enter their user name
        self.username.pack(fill="x", padx=50, pady=(2, 5)) # the padding of this box
        # the password title above the password entry
        tk.Label(self, text="Password", font=("Calibri", 10), bg="#ffffff", fg="#000000").pack(anchor="w", padx=50) # the creation of this password label and also the colors padding of it
        self.password = tk.Entry(self, font=("Calibri", 12), show="*") # creating the textbox of the password field added hashing which a fellow peer showed me how to make it hashed
        self.password.pack(fill="x", padx=50, pady=(2, 10)) # padding of the password box
        # this is for the login button and the creattion of it on the main menu page
        login_button = tk.Button(self, text="Login", font=("Calibri", 12, "bold"), bg="#00ccd1", fg="white",
                                command=self.handle_login)
        login_button.pack(fill="x", padx=50, pady=5) # the padding of the login button on the main menu page

        back_button = tk.Button(self, text="Create Account", font=("Calibri", 12, "bold"), bg="#00ccd1", fg="white",
                                command=self.CU_page) # the creation of the create user button and also the command which is further down
        back_button.pack(fill="x", padx=50, pady=5) # padding of the create user button and strecthes it

    def CU_page(self): # this is the page that opens when create account button is clicked cu stands for create username
        self.clean_open() # clears the elements if something else is sitll there
        label_title = tk.Label(self, text="Create an account here!", font=("Calibri", 25, "bold"), bg="#6ba1c7", fg="#b8c5ce") # the creation of the title of the top of the page
        label_title.pack(pady=(40,20)) # the padding of the title for the page

        tk.Label(self, text="Create an Username", font=("Calibri", 10), bg="#ffffff", fg="#000000").pack(anchor="w", padx=50) # the words beside the user entry field to enter a new userna,e
        self.username = tk.Entry(self, font=("Calibri", 12)) # the entry box next to create username: so the user can type their new username
        self.username.pack(fill="x", padx=50, pady=(5, 15)) # padding

        tk.Label(self, text="Create a Password", font=("Calibri", 10), bg="#ffffff", fg="#000000").pack(anchor="w", padx=50) # same thing as above but for password
        self.password = tk.Entry(self, font=("Calibri", 12),) # same as above but for passoerd
        self.password.pack(fill="x", padx=50, pady=(5, 20)) # padding of the entry 

        register = tk.Button(self, text="Sign Up", font=("Calibri", 12, "bold"), bg="#00ccd1", fg="white",
                                command=self.handle_register) # register button 
        register.pack(fill="x", padx=50, pady=10) # padding of the register button
        
        back_button = tk.Button(self, text="Already got one!", font=("Calibri", 12, "bold"), bg="#00ccd1", fg="white",
                                command=self.login_page) # the button to go back login page in case the user already has an account that they can use
        back_button.pack(fill="x", padx=50, pady=10) # padding of back button

    def main_menu(self): # the openinig of the main menu after the login page
        self.clean_open() # clears the page
        self.geometry("700x500") # size of the maine menu page
        self.configure(bg="#ffffff") # backgroudn of the main menu page


        try: # images for the various icons that are present
            self.FAQ_icon = tk.PhotoImage(file="FAQbutton.png") # faq icon
            self.Settings_icon = tk.PhotoImage(file="Settingsbutton.png") # settings icon
            self.priority_icon = tk.PhotoImage(file="Prioritiesbutton.png") # priorities icon
            self.atar_icon = tk.PhotoImage(file="ATARButton.png") # atar icon
            self.ue_icon = tk.PhotoImage(file="UEbutton.png") # upcoming events icon
        except tk.TclError: # error if the images arent in the correct place
            messagebox.showerror("Error 1: madhava has forgotten to put correct image files!") # this error can be entered in the error form in faq page
            return

        self.grid_columnconfigure(0, weight=1, uniform="main_feats") # creating a makeshift grid so the buttons dont mess up and get even spacing
        self.grid_columnconfigure(1, weight=1, uniform="main_feats")
        self.grid_columnconfigure(2, weight=1, uniform="main_feats")

        self.grid_rowconfigure(0, weight=0) # same thing but for the rows
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)

        top_bar = tk.Frame(self, bg="#ffffff") # the bar with the logo, welcom message settings button and faq button
        top_bar.grid(row=0, column=0, columnspan=3, sticky="ew", padx=20, pady=10) # the padding of this

        logo_welcome = tk.Frame(top_bar, bg="#ffffff") #the logo and welcome message container so they are together
        logo_welcome.pack(side="left", anchor="w") # position

        if self.logo: # the logo in the top left having the same background of the main menu
            mm_logo = tk.Label(top_bar, image=self.logo, bg="#ffffff") # cretion of this mm stands for main menu
            mm_logo.pack(side="left", padx=(0,10)) # padding

        welcome_message = f"Welcome, {self.current_user if self.current_user else 'Error 2'}!" # welcome message that willbe next to the logo and will give error if something breaks
        welcome_label = tk.Label(top_bar, text=welcome_message, font=("Calibri", 14, "bold"),
                                 bg="#ffffff", fg="#00636e") # the color and text creation
        welcome_label.pack(side="left") # the positon of this

        faq_sttg = tk.Frame(top_bar, bg="#ffffff") # faq and setting container
        faq_sttg.pack(side="right", anchor="e") # positioning
        settings_button = tk.Button(faq_sttg, image=self.Settings_icon, font=("Calibri", 10,"bold"), bg="#00ccd1", fg="white",
                                     command=self.open_settings_file) # creating the settings button only accesible in the main menu
        settings_button.pack(side="right", padx=(5, 0)) # the positon og it and padding

        FAQ_button = tk.Button(faq_sttg, image=self.FAQ_icon, font=("Calibri", 10,"bold"), bg="#00ccd1", fg="white",
                                     command=self.open_FAQ_file) # creating the faq button on the main menu
        FAQ_button.pack(side="right", padx=(5, 0)) # the padding

        # creating a button for all three features of the app so the user can use them
        priority_btn = tk.Button(self, image=self.priority_icon, text="\nPriorities", font=("Calibri", 14,"bold"), bg="#00ccd1", fg="white",
                                    activebackground="#00a3a6", activeforeground="white", compound="top", command=self.priorities) # here i use activeforegoud which is wehen it is clicked it will show that color
        priority_btn.grid(row=2, column=0, sticky="nsew", padx=20,  pady=20) # padding

        
        atar_btn = tk.Button(self, image=self.atar_icon, text="\nATAR Calculator", font=("Calibri", 14,"bold"), bg="#00ccd1", fg="white",
                                    activebackground="#00a3a6", activeforeground="white", compound="top", command=self.atar_calc)
        atar_btn.grid(row=2, column=1, sticky="nsew", padx=20,  pady=20) # padding

        
        upcoming_events_btn = tk.Button(self, image=self.ue_icon, text="\nUpcoming Events", font=("Calibri", 14,"bold"), bg="#00ccd1", fg="white",
                                    activebackground="#00a3a6", activeforeground="white", compound="top", command=self.events_page)
        upcoming_events_btn.grid(row=2, column=2, sticky="nsew", padx=20,  pady=20) # padding
        # logout button creation of it
        logout_button = tk.Button(self, text="Log out", font=("Calibri", 12, "bold"), bg="#00ccd1", fg="white",
                                activebackground="#00a3a6", activeforeground="white", command=self.handle_logout)
        logout_button.grid(row=3, column=0, sticky="nw", padx=20, pady=20) # padding
    # from here onwards it is making hte commands from the various button and various text entrys work
    def open_FAQ_file(self): # the if faq button is clicked this makes it go there
        self.clean_open() # clears anything that might be in the way
        import FAQPage # opens the faq page python file

        arrival_page = "main_menu" if self.current_user else "login" # this is so it is accessibile from the login page if user is not signed in or accesible from manin menu if logged in
        FAQPage.load_FAQ_page(self, arrival_page) # i make sure this is the case because before if faq page was in it could bypass login

    def open_settings_file(self): # this is command creation of what to do once the button is clicked in the main menu
        self.clean_open() # clears the memory and any wifget for speed which is a non functional requirement
        
        import SettingsPage # the python file will open if the setting button is clicked

        SettingsPage.load_settings_page(self) # displays it

    def priorities(self): # priorites command creation so when its button is clicked it leads to the gfile
        self.clean_open()

        import Priorities # the python file for this

        Priorities.load_priorities_page(self) # diaplays it

    def atar_calc(self): # same but for atar calculator function
        self.clean_open()

        import ATAR_Calculator

        ATAR_Calculator.load_atar_page(self)


    def events_page(self): # same aas last two but fro upcoming events
        self.clean_open()

        import UEPage

        UEPage.load_UE_Page(self)

    def handle_login(self):
        
        correct_username = self.username.get().strip()
        correct_password = self.password.get().strip()
        # input validation for the login
        if not correct_username or not correct_password:
            messagebox.showwarning("error 2", "wrong user or password or you have to enter everything") # error message 
        
        valid_user = False # i set it to false so if it is empty it wont let them through unless it is in the udf.csv file
        with open(user_data_file, mode='r') as file: # checks the file
            reader = csv.DictReader(file)
            for row in reader:
                if row ['username'] == correct_username and row['password'] == correct_password:
                    valid_user = True # if the username and password match those in that csv file it will allow the user through
                    break

        if valid_user:
            self.current_user = correct_username # this is so it saves it as the change username as well and also the welcome message is addressed to this name
            self.main_menu() # calling the main menu
        else:
            messagebox.showerror("something is wrong (error 2.5)", "Invalid username or password fix it to enter.") # i had to use 2.5 because i used 2 and 3 already before fixing it
            return
    
    def handle_register(self): # for the register page it changes the correct user name and password when the user updates their credentials
        correct_username = self.username.get().strip()
        correct_password = self.password.get().strip()
        # c stands for correct
        if not correct_username or not correct_password:
            messagebox.showwarning("Error 2.75","no blanks") # once again i used 2 and 3 already so i have to used 2.5 and 2.75
            return
        
        with open(user_data_file, mode='r') as file: # this is to read the udf file and opens in read mode to check if a username is alr in use
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == correct_username:
                    messagebox.showerror("invalid", "username already in use") # error message to tell user they cant have the same username as someone else
                    return
                
        with open(user_data_file, mode='a', newline='') as file: # same as above but this time for the successful account creation and saves it there
            writer = csv.writer(file) # creates a writer object that formats and writes into a csv file
            writer.writerow([correct_username, correct_password]) # puts its according as either the correct username or password

        messagebox.showinfo("success", "account created") # success message once the accound is created
        self.login_page() # calls the login page once account is created

    def handle_logout(self): # this is when the logout button is clikec
        self.clean_open() # clears cahce and speeds it up a bit by clearing extra widgets
        self.current_user = None # sets logged in user to no one
        self.geometry("500x450") # back to login page dimensions
        self.configure(bg="#00636e") # background color
        self.login_page() # calls login page
# the end of the main this and runs the loop its only at the bottom of this python file because i didnt require it for the other files
if __name__ == "__main__":
    app = App()
    app.mainloop()