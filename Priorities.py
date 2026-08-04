import tkinter as tk # these are the librabries for the priorities page of the application
import csv # csv is imported because it saves to the csv file 
from tkinter import messagebox, ttk
import os # loads the built in modules to interact directly with the operating system
from datetime import datetime # date time accesses dtae ad time so it gets has the ability to calculate proximity to the date

PrDa = "Priority_database.csv" # the data base where the events are being saved to

def load_priorities_page(app, arrivalPage="main_menu"): # the connection between the main menu and this page
    app.configure(bg="#6ba1c7") # the background color of this page

    home_title = tk.Frame(app, bg="#6ba1c7") # same thing creating a frame for the home button and title
    home_title.pack(fill="x", padx=20, pady=10) # the padding

    def home_back(): # the button to go back to the main menu
        if arrivalPage == "main_menu": # basically is saying if home is clicked go to main menu
            app.main_menu()
        else:
            app.login_page() # if not go to login page

    home_click = tk.Button(home_title, text="home", font=("Calibri", 11, "bold"),
                           bg="#00ccd1", fg="white", command=home_back) # the creation of the button and assigns the command
    home_click.pack(side="left") # positioning

    FAQTitle = tk.Label(home_title, text="Priorites", font=("Calibri", 18, "bold"), bg="#6ba1c7", fg="#00636e") # background and font color of the title
    FAQTitle.pack(side="left", padx=20) # position and padding

    main1 = tk.Frame(app, bg="#6ba1c7") # creating a frame to hold the elements
    main1.pack(fill="both", expand=True, padx=20, pady=10) # padding for the frame

    left1 = tk.Frame(main1, bg="#6ba1c7") # pcreating of another frame to create the left side where the user inputs would be
    left1.pack(side="left", fill="y", padx=(0, 10)) # padding and positioning 

    right1 = tk.Frame(main1, bg="#6ba1c7") # background of this and creating the right side just like the lef side but this is the table the side with the display side
    right1.pack(fill="both", side="right", expand=True, padx=(10, 0)) # padding and positiong

    tk.Label(left1, text="task name:", font=("Calibri", 11, "bold"), bg="#6ba1c7", fg="#00636e").pack(anchor="w", pady=(10,2)) # positiing  and padding and creation of the label fot the rask name
    tentry= tk.Entry(left1, font=("Calibri", 11), width=22) # font of this lavel 
    tentry.pack(fill="x", pady=(0,10)) # padding

    tk.Label(left1, text="Diffculty(0-10):", font=("Calibri", 11, "bold"), bg="#6ba1c7", fg="#00636e").pack(anchor="w", pady=(0,2)) # positiong and padding of this label
    ddrop= ttk.Combobox(left1, values=[str(i) for i in range(1,11)], font=("Calibri", 11), state="readonly", width=20) # a combobox for the user to select how difficult they think a specific task is
    ddrop.pack(fill="x", pady=(0,10)) # padding and stretch
    ddrop.set("1") # sets the starting value to 1

    tk.Label(left1, text="Due date must be in (dd/mm/yy):", font=("Calibri", 11, "bold"), bg="#6ba1c7", fg="#00636e").pack(anchor="w", pady=(0,2)) # positiong and padding 
    date_entry= tk.Entry(left1, font=("Calibri", 11), width=22) # creating the date entry and an entry box for it
    date_entry.insert(0, "31/12/2026") # sets the due date to 31 december 2026
    date_entry.pack(fill="x", pady=(0,20)) # stretch and padding

    columns = ("task", "difficulty", "proximity", "priority", "raw_date") # the commands for the headers 
    priorityt = ttk.Treeview(right1, columns=columns, show="headings", selectmode="browse")

    priorityt.column("task", width=150, anchor="w")
    priorityt.column("difficulty", width=100, anchor="center")
    priorityt.column("proximity", width=100, anchor="center")
    priorityt.column("priority", width=100, anchor="center")
    priorityt.column("raw_date", width=0, stretch=False)
    priorityt.pack(fill="both", expand=True)

    def sort_by(col, reverse):
        dlist = []
        for k in priorityt.get_children(""):
            value = priorityt.set(k, col)
            value = float(value) if col in ["difficulty", "priority"] else (int(value.split()[0]) if col == "proximity" else value)
            dlist.append((value, k))
        dlist.sort(reverse=reverse)
        for index, (value, k) in enumerate(dlist):
            priorityt.move(k, "", index)
        priorityt.heading(col, command=lambda: sort_by(col, not reverse))
    for col, title in [("task", "Task name"), ("difficulty", "Difficulty score"), ("proximity", "Proximity (days)"), ("priority", "Priority score")]:
        priorityt.heading(col, text=f"{title}", command=lambda c=col: sort_by(c, False))
    
    def scalculations(date_str, diff_score):
        try:
            due_date = datetime.strptime(date_str.strip(), "%d/%m/%Y")
        except ValueError:
            return None, None
        
        daysrem = (due_date.date() - datetime.now().date()).days

        if daysrem <= 0:
            proximity = 10
            displayd = "0 (its overdue)" if daysrem < 0 else "0 (its due today)"
        else:
            displayd = str(daysrem)

            if daysrem <= 2:
                proximity = 10
            elif daysrem <= 5:
                proximity = 8
            elif daysrem <= 10:
                proximity = 6
            elif daysrem <= 20:
                proximity = 4
            else:
                proximity = 2
        prioritys = round((int(diff_score)* 0.5) + (proximity * 0.5), 1)
        return displayd, prioritys
    
    def csvrows():
        if not os.path.exists(PrDa): return []
        with open(PrDa, mode='r', newline='') as f: return list(csv.reader(f))[1:]

    def saverows(rows):
        with open(PrDa, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["task", "difficulty", "date"])
            writer.writerows(rows)
        readrows()
        clear()

    def readrows():
        for item in priorityt.get_children(): priorityt.delete(item)
        for row in csvrows():
            daysd, pscore = scalculations(row[2], row[1])
            if pscore is not None:
                priorityt.insert("", "end", values=(row[0], row[1], daysd, pscore, row[2]))

    def add_priority():
        t, df, dt = tentry.get().strip(), ddrop.get(), date_entry.get().strip()
        if not t or scalculations(dt, df)[1] is None:
            messagebox.showerror("Error 8", "yo got to check inputs. also you can onl yuse dd/mm/yy")
            return
        saverows(csvrows() + [[t, df, dt]])
    
    def modifyPriority(is_delete=False):
        selected = priorityt.selection()
        if not selected:
            messagebox.showerror("Error 9", "select one of the tasks to change")
            return
        
        rows = csvrows()
        index = priorityt.index(selected)

        if is_delete:
            rows.pop(index)
        else:
            t, df, dt = tentry.get().strip(), ddrop.get(), date_entry.get().strip()
            
            if not t or scalculations(dt, df)[1] is None:
                messagebox.showerror("Error 8", "you have got to check inputs. also you can only use dd/mm/yy")
                return
            
            rows[index] = [t, df, dt]

        saverows(rows)
    
    def onrow(event):
        selected = priorityt.selection()
        if not selected:
            return
            #values = priorityt.item(selected)["values"]
        
        itemd = priorityt.item(selected)
        values = itemd.get("values", [])
        
        if values and len(values) >= 5:
            tentry.delete(0, tk.END)
            tentry.insert(0, values[0])
            ddrop.set(values[1])
            
            date_entry.delete(0, tk.END)
            date_entry.insert(0, str(values[4]))

    def clear():
        tentry.delete(0, tk.END)
        ddrop.set("1")
        date_entry.delete(0, tk.END)
        date_entry.insert(0, "31/12/2026")
        priorityt.selection_remove(priorityt.selection())
    
    priorityt.bind("<<TreeviewSelect>>", onrow)

    tk.Button(left1, text="Add priority", font=("Calibri", 11, "bold"), bg="#00ccd1", fg="white", command=add_priority).pack(fill="x",pady=2)
    tk.Button(left1, text="Modify priority(make sure to select)", font=("Calibri", 11, "bold"), bg="#00ccd1", fg="white", command=lambda: modifyPriority(is_delete=False)).pack(fill="x",pady=2)
    tk.Button(left1, text="Delete priority(make sure to select)", font=("Calibri", 11, "bold"), bg="#00ccd1", fg="white", command=lambda: modifyPriority(is_delete=True)).pack(fill="x",pady=2)

    readrows()