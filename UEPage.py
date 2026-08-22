import tkinter as tk # these are the librabries used in the upcoming events section of the priority app.
import csv # it should also be noted that the upcoming events is basically the first version of the priorites but eventaully became a sepersate feature
from tkinter import messagebox, ttk
import os
from datetime import datetime # added during alpha testing as i advanced a feature of upcoming evnts

UE_Csv = "UE.csv" # UE_Csv is the csv file where the categories are svaed to

def load_UE_Page(app, arrival_page="main_menu"): # the connections between the main menu pae and this page
    app.configure(bg="#6ba1c7")  # the background color of this page

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

    ue_title = tk.Label(home_title, text="Upcoming Events", font=("Calibri", 18, "bold"), bg="#6ba1c7", fg="#00636e") # background and font color of the title
    ue_title.pack(side="left", padx=20) # position and padding
 # copied ths sectiom from the priorites section as it would benefit from a similar layout
    main_frame = tk.Frame(app, bg="#6ba1c7") # creating a frame to hold the elements
    main_frame.pack(fill="both", expand=True, padx=20, pady=10) # padding for the frame

    left_frame = tk.Frame(main_frame, bg="#6ba1c7") # pcreating of another frame to create the left side where the user inputs would be
    left_frame.pack(side="left", fill="y", padx=(10, 0)) # padding and positioning 

    right_frame = tk.Frame(main_frame, bg="#6ba1c7") # background of this and creating the right side just like the lef side but this is the table the side with the display side
    right_frame.pack(fill="both", side="right", expand=True, padx=(10, 0)) # padding and positiong
    # the labels are also positioned in a similar way to the prioties functon as upcoming events is basically a watered down version of the prirotiy feature
    tk.Label(left_frame, text="Event Name:", font=("Calibri", 11, "bold"), bg="#6ba1c7", fg="#00636e").pack(anchor="w", pady=(10,2)) # positiong and padding of this label
    user_update= tk.Entry(left_frame, font=("Calibri", 11), width=22) # an entry box for the user to input the name of the events
    user_update.pack(fill="x", pady=(0,10)) #  padding of this entry box

    tk.Label(left_frame, text="Event Date:", font=("Calibri", 11, "bold"), bg="#6ba1c7", fg="#00636e").pack(anchor="w", pady=(0,2)) # positiong and padding of this label
    date_update= tk.Entry(left_frame, font=("Calibri", 11), width=22) # the entry box for the date entry for this box
    date_update.pack(fill="x", pady=(0,20)) # padding of this entry box

    columns = ("title", "date") # the columns in the csv and the table that is required for the upcomoing events feature
    table_UE = ttk.Treeview(right_frame, columns=columns, show="headings") # the table that is present wth all the upcoming events
    table_UE.heading("title", text="Event Name") # the title of one of the columns in the table on the upcoming events tab;e
    table_UE.heading("date", text="Event Date") # the title of the other column in the table
    table_UE.column("title", width=220, anchor="w") # the width and the psoitiong of the title for the event name
    table_UE.column("date", width=120, anchor="center") # same as the one above but for the event date
    table_UE.pack(fill="both", expand=True) # the table will expand if the screen dimensions are changed

    def csv_table(): # the csv will be the database where these are saved to and will be visible in the table also
        for item in table_UE.get_children(): # what this does is it gets the children of the table and deletes them so that when the user adds a new event it will not be duplicated in the table
            table_UE.delete(item) # this delete the item
        
        if not os.path.exists(UE_Csv): # if the file isnt ther it will create the file
            with open(UE_Csv, mode='w', newline='') as file: # opens in write mode to write and save the upcoming events inputted by the user
                writer = csv.writer(file) # this prepares and writes headers into the csv file
                writer.writerow(["title", "date"]) # the headers for the csv file
            return

        today = datetime.now().date() # making it easier for what today is in a shorther format
        valid_rows = [] # creating an empty list
        
        with open(UE_Csv, mode='r', newline='') as file: # this is the opening of the file to be able to be see in the table
            reader = csv.DictReader(file) # converts each row into a dictionary
            for row in reader: # loops through the csv one file at a time
                try: # added during alpha testing
                    if not row.get("date"): # if in invalid format it skips over it
                        continue
                    event_date = datetime.strptime(row["date"], "%d/%m/%Y").date() # the event date grabbed from the csv file in the format of dd/mm/yyyy
                    if event_date >= today: # if the date is after today
                        valid_rows.append(row) # it will be added to the date row
                        table_UE.insert("", "end", values=(row["title"], row["date"])) # inseret new row into the table
                except ValueError:
                    continue

        with open(UE_Csv, mode='w', newline='') as file: # opens csv file in write mode
            writer = csv.writer(file) # creates a writer object
            writer.writerow(["title", "date"]) # writes the header row at the top of the csv file program
            for row in valid_rows:  # starts a loop
                writer.writerow([row["title"], row["date"]]) # writes unexpired events title and date in the csv file


    def save_csv_table(): # does the opposite of the last one as it takes the current data displayed in the table to the csv file
        with open(UE_Csv, mode='w', newline='') as file: # opens the csv file in write mode
            writer = csv.writer(file) # creates a write objet to format data into csv rows
            writer.writerow(["title", "date"]) # writes the first rows as the colums titles
            for item in table_UE.get_children(): # loops through the rows in the table
                 writer.writerow(table_UE.item(item)["values"]) # gets the text values from the table row and writes it into the csv file

    def add_event(): # the functon to create a new upcoming event
        title = user_update.get().strip() # grabs the text types in the input fiels and removes blank spaces for the titel entry box
        date = date_update.get().strip() # same thing as above but for the date entry box
        if not title or not date: # checks if the date or title box is empty
            messagebox.showerror("Error 4", "got to fill in both") # it will return an error message if it is empty
            return

        try: # added during alpha testing
           event_date = datetime.strptime(date, "%d/%m/%Y").date() # tries to read the text in the correct format of dd/mm/yyyy
        except ValueError: # if not in that format it throws this error which makes sure it is in correct format
            messagebox.showerror("Error 22", "date must be in DD/MM/YYYY format")
            return

        if event_date < datetime.now().date(): # added during alpha testing
            messagebox.showerror("error 24", "Cannot add events that have already have past dates.") # error message if the date trying to enter is before today
            return

        for item in table_UE.get_children(): # added during alpha testing this lines asks the table for a list of all the current rows and looks 1 by 1
            existing_event = table_UE.item(item)["values"][0] # this checks the data dictionary and uses the value at index 0 which is event name
            if existing_event.lower() == title.lower(): #this takes whatever the user has and switches it to lowercase and checks if they match if they do
                messagebox.showerror("Error 19", "Event has duplicate name as another event change it.") # it gives this error
                return 

        table_UE.insert("", "end", values=(title, date)) # if valid adds a brand new row at the bottom of the table
        save_csv_table() # runs the save function
        clear_input() #clears input ready for next input

    def update_event(): # the function to adjust an already exisiting event
        select_item = table_UE.selection() # select an item fromt he table
        if not select_item: # if nothing is selected
            messagebox.showerror("Error 5", "select something to change") # it will displasy this error message
            return
        title = user_update.get().strip() # same as before it grabs the text typed in the field and removes blanks sapces
        date = date_update.get().strip() # same as above but for date
        if not title or not date: # checks if it is empty or not
            messagebox.showerror("Error 6", "cannot be empty") # error messgae if it is empty
            return

        try: # added during alpha testing
           event_date = datetime.strptime(date, "%d/%m/%Y").date() # tries to read the text in the correct format of dd/mm/yyyy
        except ValueError: # if not in that format it throws this error to ensure it is in the correct formart
            messagebox.showerror("Error 23", "date must be in DD/MM/YYYY format")
            return

        if event_date < datetime.now().date(): # added during alpha testing
                    messagebox.showerror("error 25", "Cannot add events that have already have past dates.") # error message if the date trying to enter is before today
                    return

        for item in table_UE.get_children(): # added during alpha testing looks at the table and checks the current rows by looking at them 1 at a time
            if item == select_item[0]: # compares the row to the one being currently looked at against the exact row the user clicked to update
                continue 
            existing_event = table_UE.item(item)["values"][0] # pulls the event name from any other row to check agains it
            if existing_event.lower() == title.lower(): # performs the same lowercase string compariosn as the one in add event.
                messagebox.showerror("Error 20", "Another event already has this name so it has to be different.") # this error will occur if there is adjusting an event to another one with the same name
                return

        table_UE.item(select_item, values=(title, date)) # select and returns the tuple
        save_csv_table() # saves the changes to the csv file
        clear_input() # clears input ready for next input

    def delete_event(): # the function to delete a upcoming vent
        select_item = table_UE.selection() # the item that is selected from the table
        if not select_item: # an error messgae if nothing is selected to be delete
            messagebox.showerror("Error 7", "select to delete") # the error message
            return
        table_UE.delete(select_item) # deletes the selected items
        save_csv_table() # the save functions is called
        clear_input() # celars input for next delete or entry

    def clear_input(): # the clear input fields which are the two entry and the row selected currently get cleared
        user_update.delete(0, tk.END) # clear the entry field for title
        date_update.delete(0, tk.END) # clear the entry field for date
        table_UE.selection_remove(table_UE.selection()) # clears the selection from the table
    
    tk.Button(left_frame, text="Add Event", font=("Calibri", 11, "bold"), bg="#00ccd1", fg="white", command=add_event).pack(fill="x", pady=2) # creates the button to create an event and its padding
    tk.Button(left_frame, text="Adjust Event (Make Sure To Select!)", font=("Calibri", 11, "bold"), bg="#00ccd1", fg="white", command=update_event).pack(fill="x", pady=2) # creates the button to adjust an event and its padding
    tk.Button(left_frame, text="Delete Event (Make Sure To Select!)", font=("Calibri", 11, "bold"), bg="#00ccd1", fg="white", command=delete_event).pack(fill="x", pady=2) # creates the button to delete an event and its padding
    csv_table() # runs the csv table function which takes from csv to show in table