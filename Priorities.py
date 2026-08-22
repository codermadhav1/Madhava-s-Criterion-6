import tkinter as tk # these are the librabries for the priorities page of the application
import csv # csv is imported because it saves to the csv file 
from tkinter import messagebox, ttk
import os # loads the built in modules to interact directly with the operating system
from datetime import datetime # date time accesses dtae ad time so it gets has the ability to calculate proximity to the date

priority_database = "Priority_database.csv" # the data base where the events are being saved to

def load_priorities_page(app, arrival_page="main_menu"): # the connection between the main menu and this page
    app.configure(bg="#6ba1c7") # the background color of this page

    home_title = tk.Frame(app, bg="#6ba1c7") # same thing creating a frame for the home button and title
    home_title.pack(fill="x", padx=20, pady=10) # the padding

    def home_back(): # the button to go back to the main menu
        if arrival_page == "main_menu": # basically is saying if home is clicked go to main menu
            app.main_menu()
        else:
            app.login_page() # if not go to login page

    home_click = tk.Button(home_title, text="Home", font=("Calibri", 11, "bold"),
                           bg="#00ccd1", fg="white", command=home_back) # the creation of the button and assigns the command
    home_click.pack(side="left") # positioning

    priority_title = tk.Label(home_title, text="Priorites", font=("Calibri", 18, "bold"), bg="#6ba1c7", fg="#00636e") # background and font color of the title
    priority_title.pack(side="left", padx=20) # position and padding

    main_frame = tk.Frame(app, bg="#6ba1c7") # creating a frame to hold the elements
    main_frame.pack(fill="both", expand=True, padx=20, pady=10) # padding for the frame

    left_frame = tk.Frame(main_frame, bg="#6ba1c7") # pcreating of another frame to create the left side where the user inputs would be
    left_frame.pack(side="left", fill="y", padx=(0, 10)) # padding and positioning 

    right_frame = tk.Frame(main_frame, bg="#6ba1c7") # background of this and creating the right side just like the lef side but this is the table the side with the display side
    right_frame.pack(fill="both", side="right", expand=True, padx=(10, 0)) # padding and positiong

    tk.Label(left_frame, text="Task Name:", font=("Calibri", 11, "bold"), bg="#6ba1c7", fg="#00636e").pack(anchor="w", pady=(10,2)) # positiing  and padding and creation of the label fot the rask name
    task_entry= tk.Entry(left_frame, font=("Calibri", 11), width=22) # font of this lavel 
    task_entry.pack(fill="x", pady=(0,10)) # padding

    tk.Label(left_frame, text="Difficulty (0-10):", font=("Calibri", 11, "bold"), bg="#6ba1c7", fg="#00636e").pack(anchor="w", pady=(0,2)) # positiong and padding of this label
    difficulty_dropbox= ttk.Combobox(left_frame, values=[str(i) for i in range(1,11)], font=("Calibri", 11), state="readonly", width=20) # a combobox for the user to select how difficult they think a specific task is
    difficulty_dropbox.pack(fill="x", pady=(0,10)) # padding and stretch
    difficulty_dropbox.set("1") # sets the starting value to 1

    tk.Label(left_frame, text="Due Date (DD/MM/YYYY):", font=("Calibri", 11, "bold"), bg="#6ba1c7", fg="#00636e").pack(anchor="w", pady=(0,2)) # positiong and padding 
    date_entry= tk.Entry(left_frame, font=("Calibri", 11), width=22) # creating the date entry and an entry box for it
    date_entry.insert(0, "31/12/2026") # sets the due date to 31 december 2026
    date_entry.pack(fill="x", pady=(0,20)) # stretch and padding

    columns = ("task", "difficulty", "proximity", "priority", "raw_date") # the commands for the headers in the table
    priority_table = ttk.Treeview(right_frame, columns=columns, show="headings", selectmode="browse") # creating the table to display the 5 headrs above

    priority_table.column("task", width=100, anchor="w") # the width of the task header and the position + title
    priority_table.column("difficulty", width=100, anchor="center") #  the width of the task header and the position + title
    priority_table.column("proximity", width=100, anchor="center") # the width of the task header and the position + title
    priority_table.column("priority", width=100, anchor="center") # the width of the task header and the position + title
    priority_table.column("raw_date", width=0, stretch=False) # which is non existent because i dont want people to see this one
    priority_table.pack(fill="both", expand=True) # the stretch and is allowed to expand when i fullscreen the gui

    def sort_by(col, reverse):# this is creatung the sort by highest to lowest for all the headings so the user can click it and it will sort it
        data_list = [] # this is creating an initially empty list
        for k in priority_table.get_children(""): # a for loop to iterate through the items of this table
            value = priority_table.set(k, col) # represents the call and reoresetbs to set to the priority
            value = float(value) if col in ["difficulty", "priority"] else (int(value.split()[0]) if col == "proximity" else value) # making it sort by these columns
            data_list.append((value, k)) # groups the variables as a tuple and makes it into an immutable pair
        data_list.sort(reverse=reverse) # this is the way to sort them if it is false it will sort ascending and the opposite if it is true
        for index, (value, k) in enumerate(data_list): # a loop through a collection whilst tracking the index number
            priority_table.move(k, "", index) #to move the elements in relation to their value & index
        priority_table.heading(col, command=lambda: sort_by(col, not reverse)) # doing the same but the opposite of above which is the opposite of reverse
    for col, title in [("task", "Task Name"), ("difficulty", "Difficulty Score"), ("proximity", "Days Remaining"), ("priority", "Priority Score")]: # title of each of the colimmsn
        priority_table.heading(col, text=f"{title}", command=lambda c=col: sort_by(c, False)) # for each of them it will sort by column and title
    
    def score_calculations(date_string, difficulty_score): #priority score calculations
        try:
            due_date = datetime.strptime(date_string.strip(), "%d/%m/%Y") # this is the way to convert a string into a date object using the strptime method and the format of the date
        except ValueError: # this is the erorr message that doesnt return any errors
            return None, None
        
        days_remaining = (due_date.date() - datetime.now().date()).days # this is the calculation for proximity to a particular due date

        if days_remaining <= 0: # setting a rule that if the days remaing till simething is 0 that means it gets the highest proxmity score
            proximity = 10
            displays_days_remaining = "0 (its overdue)" if days_remaining < 0 else "0 (its due today)" # message if days remaining is less than 0 days or today
        else:
            displays_days_remaining = str(days_remaining) # sets the dayrems for any deadline larger than 0

            if days_remaining <= 2: # if less thean 2 days also 10 score
                proximity = 10 
            elif days_remaining <= 5: # if less than5  but greater than 2 8 score
                proximity = 8
            elif days_remaining <= 10: # if greater than 5 but less than 10 it gets 6 score
                proximity = 6
            elif days_remaining <= 20: # if greater than 10 but less than 20 it gets 6
                proximity = 4
            else:
                proximity = 2 # gets this score if greater than 20
        priority_score = round((int(difficulty_score)* 0.5) + (proximity * 0.5), 1) # formula to calculate priority score to 1 dp
        return displays_days_remaining, priority_score # returns these two valyes
    
    def csv_rows(): # the creation of the csv files bit to save the priroties
        if not os.path.exists(priority_database): return [] # returns a list and creates it if id isnt found
        with open(priority_database, mode='r', newline='') as f: return list(csv.reader(f))[1:]

    def save_rows(rows): # saves the data from the calculated priroties to the csv file
        with open(priority_database, mode='w', newline='') as f: # opens in write mode to make the changes
            writer = csv.writer(f) #creates a writer object that converts data into delimited strings
            writer.writerow(["task", "difficulty", "date"]) # the headings of the csv file
            writer.writerows(rows) # the rows can be written all at once thriugh this way
        read_rows() # calls the read rows and clear function
        clear()

    def read_rows(): # creates the read rows so the csv can save and show the user their priorites
        for item in priority_table.get_children(): priority_table.delete(item) # deltes child items from the parent widget which is the table
        for row in csv_rows(): # lopps through the row of csv_rows aka the data from the csv file
            date_distance, priority_insert = score_calculations(row[2], row[1]) # used to calculate days and scores
            if priority_insert is not None: # validation used to make sure no empty or invalid scores are added to the table
                priority_table.insert("", "end", values=(row[0], row[1], date_distance, priority_insert, row[2]))  # calls the insert method for adding and the the tupels that contains the data dsiplayed

    def add_priority(): # adding a priority function
        task_title, difficulty_title, date_title = task_entry.get().strip(), difficulty_dropbox.get(), date_entry.get().strip() # makes these all to unpack the tuples, and clean errors
        if not task_title or score_calculations(date_title, difficulty_title)[1] is None: # error message creation
            messagebox.showerror("Error 8", "you have got to check inputs. also you can only use dd/mm/yy") # the error message 
            return

        existing_rows = csv_rows() # added during alpha testing basically to presevent from 2 tasks to have the same name
        if any(row[0].strip().lower() == task_title.lower() for row in existing_rows):
            messagebox.showerror("Error 16", "cant have the same name as another task")
            return


        save_rows(csv_rows() + [[task_title, difficulty_title, date_title]]) # saves the changes
    
    def modify_priority(is_delete=False): # the function to modify an already created priority
        selected = priority_table.selection() # the selected priority to adjust in the table must be selectred in order for it to work
        if not selected: # an error message if none of the created priorites are not selectred
            messagebox.showerror("Error 9", "select one of the tasks to change") # error message
            return
        
        rows = csv_rows() # defines the rows and the index to make it less writing code across this bit of the application
        index = priority_table.index(selected)

        if is_delete: # delete the task
            rows.pop(index) # pops/deletes it
        else: 
            task_title, difficulty_title, date_title = task_entry.get().strip(), difficulty_dropbox.get(), date_entry.get().strip() # if not it will also do it this way which is assigning user input from 3 different gui elements
            
            if not task_title or score_calculations(date_title, difficulty_title)[1] is None: # an error message creation
                messagebox.showerror("Error 8", "you have got to check inputs. also you can only use dd/mm/yy") # the actual error message
                return

            for i, row in enumerate(rows): # added during alpha testing to prevent from having 2 tasks from having the same name.
                if i != index and row[0].strip().lower() == task_title.lower():
                    messagebox.showerror("Error 17", "Cant have the smae name as another task!")
                    return
            
            rows[index] = [task_title, difficulty_title, date_title] # assigning rows index to these variables

        save_rows(rows) # saves the rows based on the changes
    
    def onrow(event): #the selected row code
        selected = priority_table.selection()
        if not selected:
            return
        
        
        select_item = priority_table.item(selected) # this is the item that is selected in the table and it will be used to get the values of the selected row
        values = select_item.get("values", []) # it gets the values of the selected row and if there are no values it will return an empty list
        
        if values and len(values) >= 5: # this is a validation to make sure that the values are not empty and that there are at least 5 values in the list
            task_entry.delete(0, tk.END)
            task_entry.insert(0, values[0])
            difficulty_dropbox.set(values[1])
            
            date_entry.delete(0, tk.END) # same but for the entry of the date from above
            date_entry.insert(0, str(values[4]))

    def clear(): # clear function for wherever clear is used in this file
        task_entry.delete(0, tk.END)
        difficulty_dropbox.set("1")
        date_entry.delete(0, tk.END)
        date_entry.insert(0, "31/12/2026")
        priority_table.selection_remove(priority_table.selection())
    
    priority_table.bind("<<TreeviewSelect>>", onrow) # this is the binding of the table to the onrow function so when a row is selected it will call the onrow function

    tk.Button(left_frame, text="Add Priority", font=("Calibri", 11, "bold"), bg="#00ccd1", fg="white", command=add_priority).pack(fill="x",pady=2) # creates the buttons for add, modify and delte priorities and their respective padding and commands
    tk.Button(left_frame, text="Modify Priority (Make Sure To Select!)", font=("Calibri", 11, "bold"), bg="#00ccd1", fg="white", command=lambda: modify_priority(is_delete=False)).pack(fill="x",pady=2)
    tk.Button(left_frame, text="Delete Priority (Make Sure To Select!)", font=("Calibri", 11, "bold"), bg="#00ccd1", fg="white", command=lambda: modify_priority(is_delete=True)).pack(fill="x",pady=2)

    read_rows() # calls read rows from the csv file to show it once the user opens the feature with great efficiency