import tkinter as tk
import webbrowser

def load_FAQ_page(app, arrivalPage="main_menu"):
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

    FAQTitle = tk.Label(home_title, text="Frequently Asked Questions", font=("Calibri", 18, "bold"), bg="#6ba1c7", fg="#00636e")
    FAQTitle.pack(side="left", padx=20)

    contents = tk.Frame(app, bg="#6ba1c7")
    contents.pack(fill="both", expand=True, padx=20, pady=20)

    q1 = tk.Label(contents, text="Q1. How do i report an error or request for help or give feedback/comment?", font=("Calibri", 12, 'bold'), bg="#ffffff", fg="#000000")
    q1.pack(anchor="w", pady=(10,2))
    
    a1 = tk.Label(contents, text="A1. Click here", font=("Calibri", 12, "underline"), bg="#ffffff", fg="#0000ee")
    a1.pack(anchor="w", pady=(10,2))

    def open_link(event):
        webbrowser.open_new("https://forms.cloud.microsoft/r/LLKHYbE2qG")

    a1.bind("<Button-1>", open_link)

    q2 = tk.Label(contents, text="Q2. What is the main purpose?", font=("Calibri", 12, 'bold'), bg="#ffffff", fg="#000000")
    q2.pack(anchor="w", pady=(10,2))

    a2 = tk.Label(contents, text="A2. To calculate priorties and ATAR and view upcoming events", font=("Calibri", 12,), bg="#ffffff", fg="#000000")
    a2.pack(anchor="w", pady=(10,2))

    q3 = tk.Label(contents, text="Q3. I have forgotten my username or password?", font=("Calibri", 12, 'bold'), bg="#ffffff", fg="#000000")
    q3.pack(anchor="w", pady=(10,2))

    a3 = tk.Label(contents, text="A3. Use the link above - madhava will guide you", font=("Calibri", 12,), bg="#ffffff", fg="#000000")
    a3.pack(anchor="w", pady=(10,2))

    q4 = tk.Label(contents, text="Q4. I don't like my username or password i want to change it ", font=("Calibri", 12, 'bold'), bg="#ffffff", fg="#000000")
    q4.pack(anchor="w", pady=(10,2))

    a3 = tk.Label(contents, text="A4. Go to settings", font=("Calibri", 12,), bg="#ffffff", fg="#000000")
    a3.pack(anchor="w", pady=(10,2))
