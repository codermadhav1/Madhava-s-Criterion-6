import tkinter as tk
import csv
from tkinter import messagebox, ttk
import os

UpEv = "UE.csv"

def load_UE_Page(app, arrivalPage="main_menu"):
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

    FAQTitle = tk.Label(home_title, text="Upcoming Events", font=("Calibri", 18, "bold"), bg="#6ba1c7", fg="#00636e")
    FAQTitle.pack(side="left", padx=20)

    main1 = tk.Frame(app, bg="#6ba1c7")
    main1.pack(fill="both", expand=True, padx=20, pady=10)

    left1 = tk.Frame(main1, bg="#6ba1c7")
    left1.pack(side="left", fill="y", padx=(10, 0))

    right1 = tk.Frame(main1, bg="#6ba1c7")
    right1.pack(fill="both", side="right", expand=True, padx=(10, 0))

    tk.Label(left1, text="Name of the event?", font=("Calibri", 11, "bold"), bg="#6ba1c7", fg="#00636e").pack(anchor="w", pady=(10,2))
    userUpd= tk.Entry(left1, font=("Calibri", 11), width=22)
    userUpd.pack(fill="x", pady=(0,10))

    tk.Label(left1, text="date of the event?", font=("Calibri", 11, "bold"), bg="#6ba1c7", fg="#00636e").pack(anchor="w", pady=(0,2))
    dUpd= tk.Entry(left1, font=("Calibri", 11), width=22)
    dUpd.pack(fill="x", pady=(0,20))

    columns = ("title", "date")
    table_UE = ttk.Treeview(right1, columns=columns, show="headings")
    table_UE.heading("title", text="Event name")
    table_UE.heading("date", text="Event date")
    table_UE.column("title", width=220, anchor="w")
    table_UE.column("date", width=120, anchor="center")
    table_UE.pack(fill="both", expand=True)

    def csv_table():
        for item in table_UE.get_children():
            table_UE.delete(item)
        
        if not os.path.exists(UpEv):
            with open(UpEv, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["title", "date"])
            return
        
        with open(UpEv, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                table_UE.insert("", "end", values=(row["title"], row["date"]))

    def save_csv_table():
        with open(UpEv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["title", "date"])
            for item in table_UE.get_children():
                 writer.writerow(table_UE.item(item)["values"])

    def add_event():
        title = userUpd.get().strip()
        date = dUpd.get().strip()
        if not title or not date:
            messagebox.showerror("Error 4", "got to fill in both")
            return
        table_UE.insert("", "end", values=(title, date))
        save_csv_table()
        clear_input()

    def upd_event():
        select_item = table_UE.selection()
        if not select_item:
            messagebox.showerror("Error 5", "select something to change")
            return
        title = userUpd.get().strip()
        date = dUpd.get().strip()
        if not title or not date:
            messagebox.showerror("Error 6", "cannot be empty")
            return
        table_UE.item(select_item, values=(title, date))
        save_csv_table()
        clear_input()

    def del_event():
        select_item = table_UE.selection()
        if not select_item:
            messagebox.showerror("Error 7", "select to delete")
            return
        table_UE.delete(select_item)
        save_csv_table()
        clear_input()

    def rselect(event):
         select_item = table_UE.selection()
         if select_item:
             values = table_UE.item(select_item)["values"]
             userUpd.delete(0, tk.END)
             userUpd.insert(0, values[0])
             dUpd.delete(0, tk.END)
             dUpd.insert(0, values[1])

    def clear_input():
        userUpd.delete(0, tk.END)
        dUpd.delete(0, tk.END)
        table_UE.selection_remove(table_UE.selection())
    
    tk.Button(left1, text="Add event", font=("Calibri", 11, "bold"), bg="#00ccd1", fg="white", command=add_event).pack(fill="x", pady=2)
    tk.Button(left1, text="adjust event (make sure it selected)", font=("Calibri", 11, "bold"), bg="#00ccd1", fg="white", command=upd_event).pack(fill="x", pady=2)
    tk.Button(left1, text="delete event (make sure it selected)", font=("Calibri", 11, "bold"), bg="#00ccd1", fg="white", command=del_event).pack(fill="x", pady=2)
    csv_table()