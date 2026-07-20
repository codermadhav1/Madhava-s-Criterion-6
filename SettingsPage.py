import tkinter as tk
import csv
from tkinter import messagebox

UDF = "users.csv"

def load_settings_page(app, arrivalPage="main_menu"):
    app.configure(bg="#6ba1c7")

    home_title = tk.Frame(app, bg="#6ba1c7")
    home_title.pack(fill="x", padx=20, pady=10)

    def home_back():
        if arrivalPage == "main_menu":
            app.main_menu()
        else:
            app.login_page()

    home_click = tk.Button(home_title, text="home", font=("Calibri", 11, "bold"),
                           bg="#00ccd1", fg="white", command=home_back)
    home_click.pack(side="left")

    FAQTitle = tk.Label(home_title, text="Settings", font=("Calibri", 18, "bold"), bg="#6ba1c7", fg="#00636e")
    FAQTitle.pack(side="left", padx=20)

    tk.Label(app, text="Change to new username:").pack(anchor="w", padx=20)
    Uupdate = tk.Entry(app)
    Uupdate.insert(0, app.current_user if app.current_user else "")
    Uupdate.pack(fill="x", padx=20, pady=5)

    tk.Label(app, text="Change to new password:").pack(anchor="w", padx=20)
    pupdate = tk.Entry(app)
    pupdate.pack(fill="x", padx=20, pady=5)

    def credupd():
        newu = Uupdate.get().strip()
        newp = pupdate.get().strip()

        if not newu or not newp:
            messagebox.showwarning("Error 3", "It is blank")
            return
        
        rows=[]
        with open(UDF, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)

        for row in rows:
            if row['username'] == app.current_user:
                row['username'] = newu
                row['password'] = newp
                break

        with open(UDF, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])
            for row in rows:
                writer.writerow([row['username'], row['password']])

        app.current_user = newu
        messagebox.showinfo("Great",  "it has been changed now!")
        app.main_menu()


    tk.Button(app, text="Save", command=credupd, bg="#00ccd1", fg="white").pack(pady=10)