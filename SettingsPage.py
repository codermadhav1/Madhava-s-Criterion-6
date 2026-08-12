import tkinter as tk # these are all the libraries that are used in this part of the application
import csv # tkineter for the gui and csv to read the user_data_file file for username and passwords
from tkinter import messagebox
# user_data_file stands for user database file for the passwords and usernames of this application
user_data_file = "users.csv"
# creating the link between the main menu and this part of the application so i defined it here so it loads after clicking the button in the top right of the maine menu
def load_settings_page(app, arrival_page="main_menu"):
    app.configure(bg="#6ba1c7") # backgroudn of this part

    home_title = tk.Frame(app, bg="#6ba1c7") # creating a container follows the same layout as the faqpage because it is the same except the title
    home_title.pack(fill="x", padx=20, pady=10)

    def home_back(): # same a faq page
        if arrival_page == "main_menu":
            app.main_menu()
        else:
            app.login_page()

    home_click = tk.Button(home_title, text="Home", font=("Calibri", 11, "bold"),
                           bg="#00ccd1", fg="white", command=home_back) # same as faqpage
    home_click.pack(side="left") # the position of this

    settings_title = tk.Label(home_title, text="Settings", font=("Calibri", 18, "bold"), bg="#6ba1c7", fg="#00636e")
    settings_title.pack(side="left", padx=20) # same as faq page python file except the title which is 'settings' for this one
    # the text next to the user entry box to change to a new username and its postion
    tk.Label(app, text="Change to new username:").pack(anchor="w", padx=20)
    user_update = tk.Entry(app) # update user name
    user_update.insert(0, app.current_user if app.current_user else "") # adds a user to the csv file
    user_update.pack(fill="x", padx=20, pady=5) # padding and strecth

    tk.Label(app, text="Change to new password:").pack(anchor="w", padx=20) # same but for password
    password_update = tk.Entry(app) # password update so the user can change their password here
    password_update.pack(fill="x", padx=20, pady=5) # size of textbox and padding

    def credential_update():# credential_update is the functions to asssign the new passowrd and username
        new_username = user_update.get().strip() # new_username is new username so it updates it 
        new_password = password_update.get().strip() # new_password is new password so it gets updated also

        if not new_username or not new_password: # if nothing is entered it will prompt the error message which can be used to put into the report form
            messagebox.showwarning("Error 3", "It is blank")
            return
        
        rows=[] # the csv file edtiong
        with open(user_data_file, mode='r', newline='') as file: # opening the csv file to append the username and password
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row) # depnds on username on password it changes both when a new is entered

        for row in rows:
            if row['username'] == app.current_user: # displays the new one next tie trying to change again
                row['username'] = new_username # sets the new username as the standard login credentials
                row['password'] = new_password # sets the new password as the standard login credentials
                break

        with open(user_data_file, mode='w', newline='') as file: # this opens in write mode to modfy the details
            writer = csv.writer(file)
            writer.writerow(["username", "password"])
            for row in rows:
                writer.writerow([row['username'], row['password']]) # it writes the new ones into these rows

        app.current_user = new_username # sets the current user logged in to the new username the user has created
        messagebox.showinfo("Great!",  "it has been changed now!") # success message
        app.main_menu() # calls main menu


    tk.Button(app, text="Save", command=credential_update, bg="#00ccd1", fg="white").pack(pady=10) # padding of the button and creates a save button that updates the credentaisl