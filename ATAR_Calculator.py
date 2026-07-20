import tkinter as tk
from tkinter import messagebox, ttk

def load_atar_page(app, arrivalPage="main_menu"):
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

    FAQTitle = tk.Label(home_title, text="ATAR Calculator", font=("Calibri", 18, "bold"), bg="#6ba1c7", fg="#00636e")
    FAQTitle.pack(side="left", padx=20)

    def scaled_score(subject, raw_score):

        if raw_score > 50:
            r = 50
        elif raw_score < 0:
            r = 0
        else:
            r = raw_score

        if subject == "Mathematical Methods":
            if r <= 20: return float(r+1)
            elif r <= 25: return 21 + ((r-20) * 1.4)
            elif r <= 30: return 28 + ((r-25) * 1.4)
            elif r <= 35: return 35 + ((r-30) * 1.2)
            elif r <= 40: return 41 + ((r-35) * 1)
            elif r <= 45: return 46 + ((r-40) * 0.6)
            else: return 49 + ((r-45) * 0.4)

        if subject == "Chemistry":
            if r <= 20: return float(r+2)
            elif r <= 25: return 22 + ((r-20) * 1.2)
            elif r <= 30: return 28 + ((r-25) * 1.2)
            elif r <= 35: return 34 + ((r-30) * 1)
            elif r <= 40: return 39 + ((r-35) * 1)
            elif r <= 45: return 44 + ((r-40) * 0.6)
            else: return 47 + ((r-45) * 0.6)

        if subject == "Physics":
            if r <= 20: return float(r)
            elif r <= 25: return 20 + ((r-20) * 1.2)
            elif r <= 30: return 26 + ((r-25) * 1.2)
            elif r <= 35: return 32 + ((r-30) * 1)
            elif r <= 40: return 37 + ((r-35) * 1)
            elif r <= 45: return 42 + ((r-40) * 1)
            else: return 47 + ((r-45) * 0.6)

        if subject == "English":
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

        if subject == "Buisness Management":
            if r <= 20: return float(r-3)
            elif r <= 25: return 17 + ((r-20) * 1)
            elif r <= 30: return 22 + ((r-25) * 1)
            elif r <= 35: return 27 + ((r-30) * 1)
            elif r <= 40: return 32 + ((r-35) * 1.2)
            elif r <= 45: return 38 + ((r-40) * 1.2)
            else: return 44 + ((r-45) * 1.2)

        if subject == "General Maths":
            if r <= 20: return float(r-2)
            elif r <= 25: return 18 + ((r-20) * 1)
            elif r <= 30: return 23 + ((r-25) * 1)
            elif r <= 35: return 28 + ((r-30) * 1)
            elif r <= 40: return 33 + ((r-35) * 1)
            elif r <= 45: return 38 + ((r-40) * 1.2)
            else: return 44 + ((r-45) * 1.2)

        if subject == "Biology":
            if r <= 20: return float(r-1)
            elif r <= 25: return 19 + ((r-20) * 1.2)
            elif r <= 30: return 25 + ((r-25) * 1.2)
            elif r <= 35: return 31 + ((r-30) * 1)
            elif r <= 40: return 36 + ((r-35) * 1)
            elif r <= 45: return 41 + ((r-40) * 1)
            else: return 46 + ((r-45) * 0.8)

        if subject == "Physical Education":
            if r <= 20: return float(r-3)
            elif r <= 25: return 17 + ((r-20) * 1)
            elif r <= 30: return 22 + ((r-25) * 1)
            elif r <= 35: return 27 + ((r-30) * 1.2)
            elif r <= 40: return 33 + ((r-35) * 1)
            elif r <= 45: return 38 + ((r-40) * 1.2)
            else: return 44 + ((r-45) * 1.2)

        return float(raw_score)

    def aggregate_to_atar(aggregate):
        if aggregate >= 208.08: return 99.90
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
        
    def calculate_atar():
        scaled_scores = []
        
        for subjectchoose, scorentry, scaledlbl in subject_rows:
            subject = subjectchoose.get()
            raw_text = scorentry.get().strip()

            if not raw_text:
                scaledlbl.config(text=" ")
                continue

            try:
                raw_score = int(raw_text)

                if not(0 <= raw_score <= 50):
                    messagebox.showerror("Error 10", "Scores gotto be integrs")
                    return
                
                scaled = scaled_score(subject, raw_score)
                scaled_scores.append(scaled)
                scaledlbl.config(text=f"Scaled: {scaled:.2f}")
            except ValueError:
                messagebox.showwarning("error 11", "same as 10. it has to be interger")
                return
        
        if not scaled_scores:
            messagebox.showwarning("error 12", "Please enter a score required for all them")
            return
            
        while len(scaled_scores) < 6:
            scaled_scores.append(0.0)

        scaled_scores.sort(reverse=True)

        top4 = sum(scaled_scores[0:4])
        bottom2 = sum(scaled_scores[4:6]) * 0.1
        total_aggregate = top4 + bottom2
        final_atar = aggregate_to_atar(total_aggregate)
        result_label.config(text=f"Aggregate: {total_aggregate:.2f} , Estimated ATAR: {final_atar:.2f}")

    formf = tk.Frame(app, bg="#6ba1c7")
    formf.pack(fill="both", expand=True, padx=40, pady=10)

    tk.Label(formf, text="select subject", font=("Calibri", 12, "bold"), bg="#6ba1c7", fg="white").grid(row=0, column=0, sticky="w", pady=5)
    tk.Label(formf, text="enter raw score (integer)", font=("Calibri", 12, "bold"), bg="#6ba1c7", fg="white").grid(row=0, column=1, sticky="w", padx=20, pady=5)
    tk.Label(formf, text="scaled result", font=("Calibri", 12, "bold"), bg="#6ba1c7", fg="white").grid(row=0, column=2, sticky="w", pady=5)

    subject_options = ["Mathematical Methods", "Chemistry", "English", "Physics", "Biology", "Software Dev", "Buisness Management", "Physical Education", "General Maths"]
    subject_rows = []

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