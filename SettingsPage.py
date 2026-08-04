import tkinter as tk # these are all the libraries that are used in this part of the application
import csv # tkineter for the gui and csv to read the udf file for username and passwords
from tkinter import messagebox
# UDF stands for user database file for the passwords and usernames of this application
UDF = "users.csv"
# creating the link between the main menu and this part of the application so i defined it here so it loads after clicking the button in the top right of the maine menu
def load_settings_page(app, arrivalPage="main_menu"):
    app.configure(bg="#6ba1c7") # backgroudn of this part

    home_title = tk.Frame(app, bg="#6ba1c7") # creating a container follows the same layout as the faqpage because it is the same except the title
    home_title.pack(fill="x", padx=20, pady=10)

    def home_back(): # same a faq page
        if arrivalPage == "main_menu":
            app.main_menu()
        else:
            app.login_page()

    home_click = tk.Button(home_title, text="home", font=("Calibri", 11, "bold"),
                           bg="#00ccd1", fg="white", command=home_back) # same as faqpage
    home_click.pack(side="left") # the position of this

    FAQTitle = tk.Label(home_title, text="Settings", font=("Calibri", 18, "bold"), bg="#6ba1c7", fg="#00636e")
    FAQTitle.pack(side="left", padx=20) # same as faq page python file except the title which is 'settings' for this one
    # the text next to the user entry box to change to a new username and its postion
    tk.Label(app, text="Change to new username:").pack(anchor="w", padx=20)
    Uupdate = tk.Entry(app) # uupdate means user update
    Uupdate.insert(0, app.current_user if app.current_user else "") # adds a user to the csv file
    Uupdate.pack(fill="x", padx=20, pady=5) # padding and strecth

    tk.Label(app, text="Change to new password:").pack(anchor="w", padx=20) # same but for password
    pupdate = tk.Entry(app) # pupdate means password update so the user can change their password here
    pupdate.pack(fill="x", padx=20, pady=5) # size of textbox and padding

    def credupd():# credupd stands for credential update
        newu = Uupdate.get().strip() # newu is new username so it updates it 
        newp = pupdate.get().strip() # newp is new password so it gets updated also

        if not newu or not newp: # if nothing is entered it will prompt the error message which can be used to put into the report form
            messagebox.showwarning("Error 3", "It is blank")
            return
        
        rows=[] # the csv file edtiong
        with open(UDF, mode='r', newline='') as file: # opening the csv file to append the username and password
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row) # depnds on username on password it changes both when a new is entered

        for row in rows:
            if row['username'] == app.current_user: # displays the new one next tie trying to change again
                row['username'] = newu # sets the new username as the standard login credentials
                row['password'] = newp # sets the new password as the standard login credentials
                break

        with open(UDF, mode='w', newline='') as file: # this opens in write mode to modfy the details
            writer = csv.writer(file)
            writer.writerow(["username", "password"])
            for row in rows:
                writer.writerow([row['username'], row['password']]) # it writes the new ones into these rows

        app.current_user = newu # sets the current user logged in to the new username the user has created
        messagebox.showinfo("Great!",  "it has been changed now!") # success message
        app.main_menu() # calls main menu


    tk.Button(app, text="Save", command=credupd, bg="#00ccd1", fg="white").pack(pady=10) # padding of the button and creates a save button that updates the credentaisl