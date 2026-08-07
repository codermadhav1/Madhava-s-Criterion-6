import tkinter as tk # the librabries required for the atar calcvulator just these two which is to enter the atars and calculate based on the entered values
from tkinter import messagebox, ttk # the messaeboix is required for messages that will come as pop ups
# the layout code is same as the priorties, faq page, settings and upcimng events page
def load_atar_page(app, arrivalPage="main_menu"): # the connection between the main menu and this page
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

    FAQTitle = tk.Label(home_title, text="ATAR Calculator", font=("Calibri", 18, "bold"), bg="#6ba1c7", fg="#00636e") # background and font color of the title
    FAQTitle.pack(side="left", padx=20) # position and padding

    def scaled_score(subject, raw_score): # the calculations required for the scaled and raw study score

        if raw_score > 50: # the max user settable score is 50 so if something else higher is entered it will set as 50
            r = 50 # sets as 50
        elif raw_score < 0: # if a user enters less than 0 raw it will register as 0
            r = 0 # sets as 0
        else:
            r = raw_score # this sets the raw score if anything between 0-50 is entered
        # all the calculations are the same and from the scaling report so refer to the maths methods one as it makes it easier and i dont have to manually type out every formula
        if subject == "Mathematical Methods": # the calculations for maths methods the subject
            if r <= 20: return float(r+1) # this calculation makes it so if a person types a score less than 20 it adds 1 o the raw score because the starting score is sclaed by 1
            elif r <= 25: return 21 + ((r-20) * 1.4) # this is the same method calculation calculations i will explain 1 bit from eavery formula the <= means if the score is lessthan or equal to this score use this formula
            elif r <= 30: return 28 + ((r-25) * 1.4) # the 28 represents the scaled study of 25 from the scaling report
            elif r <= 35: return 35 + ((r-30) * 1.2) # the r-30 represents the raw score - the previous benchmark to calculate the scaling report for a score of 35 in this example
            elif r <= 40: return 41 + ((r-35) * 1) # the * 1 is the gradient so for this one it would be (46-41)/(45-40)
            elif r <= 45: return 46 + ((r-40) * 0.6) # using the gradient excel documents the atar gradient calc the gradient can calculated
            else: return 49 + ((r-45) * 0.4) # the reason why the last one is different is because it is the last one so it will just use the scaled score of 45 which is 49 only because if we were to use 50 the score would be higher than the report so it is just 49+ the gradient score

        if subject == "Chemistry": # refer to maths methods for how to get calculations
            if r <= 20: return float(r+2)
            elif r <= 25: return 22 + ((r-20) * 1.2)
            elif r <= 30: return 28 + ((r-25) * 1.2)
            elif r <= 35: return 34 + ((r-30) * 1)
            elif r <= 40: return 39 + ((r-35) * 1)
            elif r <= 45: return 44 + ((r-40) * 0.6)
            else: return 47 + ((r-45) * 0.6)

        if subject == "Physics": # refer to maths methods for how to get calculations
            if r <= 20: return float(r)
            elif r <= 25: return 20 + ((r-20) * 1.2)
            elif r <= 30: return 26 + ((r-25) * 1.2)
            elif r <= 35: return 32 + ((r-30) * 1)
            elif r <= 40: return 37 + ((r-35) * 1)
            elif r <= 45: return 42 + ((r-40) * 1)
            else: return 47 + ((r-45) * 0.6)

        if subject == "English": # refer to maths methods for how to get calculations
            if r <= 20: return float(r-3)
            elif r <= 25: return 17 + ((r-20) * 1)
            elif r <= 30: return 22 + ((r-25) * 1.2)
            elif r <= 35: return 28 + ((r-30) * 1)
            elif r <= 40: return 33 + ((r-35) * 1.2)
            elif r <= 45: return 39 + ((r-40) * 1.2)
            else: return 45 + ((r-45) * 1)

        if subject == "Software Dev":
            if r <= 20: return float(r-3)
            elif r <= 25: return 17 + ((r-20) * 1)
            elif r <= 30: return 22 + ((r-25) * 1.2)
            elif r <= 35: return 28 + ((r-30) * 1)
            elif r <= 40: return 33 + ((r-35) * 1.2)
            elif r <= 45: return 39 + ((r-40) * 1.2)
            else: return 45 + ((r-45) * 1)

        if subject == "Buisness Management": # refer to maths methods for how to get calculations
            if r <= 20: return float(r-3)
            elif r <= 25: return 17 + ((r-20) * 1)
            elif r <= 30: return 22 + ((r-25) * 1)
            elif r <= 35: return 27 + ((r-30) * 1)
            elif r <= 40: return 32 + ((r-35) * 1.2)
            elif r <= 45: return 38 + ((r-40) * 1.2)
            else: return 44 + ((r-45) * 1.2)

        if subject == "General Maths": # refer to maths methods for how to get calculations
            if r <= 20: return float(r-2)
            elif r <= 25: return 18 + ((r-20) * 1)
            elif r <= 30: return 23 + ((r-25) * 1)
            elif r <= 35: return 28 + ((r-30) * 1)
            elif r <= 40: return 33 + ((r-35) * 1)
            elif r <= 45: return 38 + ((r-40) * 1.2)
            else: return 44 + ((r-45) * 1.2)

        if subject == "Biology": # refer to maths methods for how to get calculations
            if r <= 20: return float(r-1)
            elif r <= 25: return 19 + ((r-20) * 1.2)
            elif r <= 30: return 25 + ((r-25) * 1.2)
            elif r <= 35: return 31 + ((r-30) * 1)
            elif r <= 40: return 36 + ((r-35) * 1)
            elif r <= 45: return 41 + ((r-40) * 1)
            else: return 46 + ((r-45) * 0.8)

        if subject == "Physical Education": # refer to maths methods for how to get calculations
            if r <= 20: return float(r-3)
            elif r <= 25: return 17 + ((r-20) * 1)
            elif r <= 30: return 22 + ((r-25) * 1)
            elif r <= 35: return 27 + ((r-30) * 1.2)
            elif r <= 40: return 33 + ((r-35) * 1)
            elif r <= 45: return 38 + ((r-40) * 1.2)
            else: return 44 + ((r-45) * 1.2)

        return float(raw_score) # this is the default return if the subject is not found it will just return the raw score as a float

    def aggregate_to_atar(aggregate): # this is converting the sum of the top 4 plus .1 of the bottom 2 and is called the aggregate in VCE the aggregate is used to find the equivalent atar tis is sourcd from the scaling report
        if aggregate >= 208.08: return 99.90 # for example if a person has an aggregate of 208.08 or above it will return as the atar of 99.90 i wont do for all but the general gist should be understood
        elif aggregate >= 204.33: return 99.80
        elif aggregate >= 201.93: return 99.70
        elif aggregate >= 199.91: return 99.60
        elif aggregate >= 198.20: return 99.50
        elif aggregate >= 194.80: return 99.25
        elif aggregate >= 192.10: return 99.00
        elif aggregate >= 187.53: return 98.50
        elif aggregate >= 183.81: return 98.00
        elif aggregate >= 180.84: return 97.50
        elif aggregate >= 178.10: return 97.00
        elif aggregate >= 173.56: return 96.00
        elif aggregate >= 169.85: return 95.00
        elif aggregate >= 166.49: return 94.00
        elif aggregate >= 163.30: return 93.00
        elif aggregate >= 160.53: return 92.00
        elif aggregate >= 157.79: return 91.00
        elif aggregate >= 155.19: return 90.00
        elif aggregate >= 150.51: return 88.00
        elif aggregate >= 146.36: return 86.00  
        elif aggregate >= 144.45: return 85.00
        elif aggregate >= 142.52: return 84.00
        elif aggregate >= 139.00: return 82.00
        elif aggregate >= 135.65: return 80.00
        elif aggregate >= 132.22: return 78.00
        elif aggregate >= 129.18: return 76.00
        elif aggregate >= 127.68: return 75.00
        elif aggregate >= 126.21: return 74.00
        elif aggregate >= 123.27: return 72.00
        elif aggregate >= 120.42: return 70.00
        elif aggregate >= 117.73: return 68.00
        elif aggregate >= 114.99: return 66.00
        elif aggregate >= 113.64: return 65.00
        elif aggregate >= 112.34: return 64.00
        elif aggregate >= 109.74: return 62.00
        elif aggregate >= 107.03: return 60.00
        elif aggregate >= 100.64: return 55.00
        elif aggregate >= 94.06: return 50.00
        elif aggregate >= 87.44: return 45.00
        else: return 40.00
        
    def calculate_atar():# this is the main function to calculate the atar score from the scaled subject scores
        scaled_scores = [] # creates an empty variable list
        
        for subjectchoose, scorentry, scaledlbl in subject_rows: # grabbing the inputs and the subjects that were chosen from the combobox
            subject = subjectchoose.get()
            raw_text = scorentry.get().strip()

            if not raw_text: # if raw text is empty or false it will clear the visible text of that box and replace it with a space
                scaledlbl.config(text=" ")
                continue # continue is to continue with the loop

            try: # if that were to not work it will try this which is what the manin goal is any way
                raw_score = int(raw_text)

                if not(0 <= raw_score <= 50): # this is a validation techniques to ensure that the user entered score is between 0 and 50 
                    messagebox.showerror("Error 10", "Scores only from 0-50") # error message that will display
                    return
                
                scaled = scaled_score(subject, raw_score) # scaled is the scaled scores from the subjects that were chosen and the rawscore inputted byt the user
                scaled_scores.append(scaled) # adds the scaled result to  the list
                scaledlbl.config(text=f"Scaled: {scaled:.2f}") # scaled score displays right next to the entry box
            except ValueError: # creation of error message
                messagebox.showwarning("error 11", "same as 10. it has to be interger") # error message
                return
        
        if not scaled_scores: # if there is a missing scaled score or incorrect input
            messagebox.showwarning("error 12", "Please enter a score required for all them") # it will show this error message
            return
            
        while len(scaled_scores) < 6: # if less than 6 sccaled scores it will add 0.0 to the end of the list to have 6 to calculate as there would be an error otherwise
            scaled_scores.append(0.0)

        scaled_scores.sort(reverse=True) # sorts the scaled scores from highest to lowest

        top4 = sum(scaled_scores[0:4]) # the top 4 being the top 4 scaled scores and get 100% of the scores added to the aggregate
        bottom2 = sum(scaled_scores[4:6]) * 0.1 # the bottom 2 only account for 0.1 of each of themir scores
        total_aggregate = top4 + bottom2 # aggreagte is calculated by adding these two variables
        final_atar = aggregate_to_atar(total_aggregate) # converts the aggreagate to atar to display it in the next message
        result_label.config(text=f"Aggregate: {total_aggregate:.2f} , Estimated ATAR: {final_atar:.2f}") # the message that will show with the calculated aggregate and the estimated atar

    formf = tk.Frame(app, bg="#6ba1c7") # the formf stands for form fill with the 2 inputs labels required from the user and the frame created for it
    formf.pack(fill="both", expand=True, padx=40, pady=10) # the padding and of the frame and also will stretch accordingly if requred

    tk.Label(formf, text="select subject", font=("Calibri", 12, "bold"), bg="#6ba1c7", fg="white").grid(row=0, column=0, sticky="w", pady=5) # the label for which subject to choose and also the positioning and padding
    tk.Label(formf, text="enter raw score (integer)", font=("Calibri", 12, "bold"), bg="#6ba1c7", fg="white").grid(row=0, column=1, sticky="w", padx=20, pady=5) # the label for the entry of the intended raw socre and its positiong and padding
    tk.Label(formf, text="scaled result", font=("Calibri", 12, "bold"), bg="#6ba1c7", fg="white").grid(row=0, column=2, sticky="w", pady=5) # the label with the title of scaled result which is the raw score plus the scaling

    subject_options = ["Mathematical Methods", "Chemistry", "English", "Physics", "Biology", "Software Dev", "Buisness Management", "Physical Education", "General Maths"] # the subjects to choose from i couldnt add more because it is a long and boring thing to do so i kept it to the main ones
    subject_rows = [] # assings it as a empty list

    for i in range(6):
        subjectchoose = tk.StringVar()
        subdrop = ttk.Combobox(formf, textvariable=subjectchoose, values= subject_options, state="readonly", width=25)
        subdrop.grid(row=i+1, column=0, pady=6, sticky="w")
        subdrop.current(i if i < len(subject_options) else 0)

        score_ent = tk.Entry(formf, font=("Calibri", 11, "bold"), width=10)
        score_ent.grid(row=i+1, column=1, padx=20, pady=6, sticky="w")
        score_ent.insert(0, "30")

        scaledlbl = tk.Label(formf, font=("Calibri", 11, "bold"), bg="#6ba1c7", fg= "#00ccd1")
        scaledlbl.grid(row=i+1, column=2, sticky="w")

        subject_rows.append((subjectchoose, score_ent, scaledlbl))

    calcbtn = tk.Button(formf, text="calculate ATAR", font=("Calibri", 12, "bold"), bg="#00636e", fg="white", padx=15, pady=5, command=calculate_atar)
    calcbtn.grid(row=7, column=0, columnspan=3, pady=20)

    result_label = tk.Label(formf, text="enter scores and click calculate", font=("Calibri", 14, "bold"), bg="#6ba1c7", fg="#00636e")
    result_label.grid(row=8, column=0, columnspan=3, pady=5)    