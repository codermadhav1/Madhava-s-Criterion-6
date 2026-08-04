import tkinter as tk # imports tkinter to create the gui and its elemetns
import webbrowser # imports webbrowser becuase i need to put a loink to the error form and gather feedback

def load_FAQ_page(app, arrivalPage="main_menu"): # this is the configuration of the build of this feature
    app.configure(bg="#6ba1c7") # backhground of this

    home_title = tk.Frame(app, bg="#6ba1c7") # creates a frame for the back to home button and the title container
    home_title.pack(fill="x", padx=20, pady=10) # padding

    def home_back(): # take the user back to main menu unless if something breaks in which will go back to loign page
        if arrivalPage == "main_menu":
            app.main_menu()
        else:
            app.login_page()

    home_click = tk.Button(home_title, text="home", font=("Calibri", 11, "bold"),
                           bg="#00ccd1", fg="white", command=home_back) # creating the back home button
    home_click.pack(side="left") # position of this button

    FAQTitle = tk.Label(home_title, text="Frequently Asked Questions", font=("Calibri", 18, "bold"), bg="#6ba1c7", fg="#00636e") # title of this function appearing at the top
    FAQTitle.pack(side="left", padx=20) # positioning & padding

    contents = tk.Frame(app, bg="#6ba1c7") # creating a frame to hold all the question and answers in the faq page
    contents.pack(fill="both", expand=True, padx=20, pady=20) # positioning
    # question1 all questions and answers follow the same layout
    q1 = tk.Label(contents, text="Q1. How do i report an error or request for help or give feedback/comment?", font=("Calibri", 12, 'bold'), bg="#ffffff", fg="#000000")
    q1.pack(anchor="w", pady=(10,2)) # padding
    # answer 1
    a1 = tk.Label(contents, text="A1. Click here", font=("Calibri", 12, "underline"), bg="#ffffff", fg="#0000ee")
    a1.pack(anchor="w", pady=(10,2))
    # this is where webrbwoser library was used in order to do this i had to search up how to use this because i couldnt us a link in tkinter
    def open_link(event):
        webbrowser.open_new("https://forms.cloud.microsoft/r/LLKHYbE2qG") # this link takes to the error and feed bacl form

    a1.bind("<Button-1>", open_link) # something i had to include according to the library guide
    # question 2
    q2 = tk.Label(contents, text="Q2. What is the main purpose?", font=("Calibri", 12, 'bold'), bg="#ffffff", fg="#000000")
    q2.pack(anchor="w", pady=(10,2))
    # answer 2
    a2 = tk.Label(contents, text="A2. To calculate priorties and ATAR and view upcoming events", font=("Calibri", 12,), bg="#ffffff", fg="#000000")
    a2.pack(anchor="w", pady=(10,2))
    # question 3
    q3 = tk.Label(contents, text="Q3. I have forgotten my username or password?", font=("Calibri", 12, 'bold'), bg="#ffffff", fg="#000000")
    q3.pack(anchor="w", pady=(10,2))
    # answer 3
    a3 = tk.Label(contents, text="A3. Use the link above - madhava will guide you", font=("Calibri", 12,), bg="#ffffff", fg="#000000")
    a3.pack(anchor="w", pady=(10,2))
    # question 4
    q4 = tk.Label(contents, text="Q4. I don't like my username or password i want to change it ", font=("Calibri", 12, 'bold'), bg="#ffffff", fg="#000000")
    q4.pack(anchor="w", pady=(10,2))
    # answer 4
    a3 = tk.Label(contents, text="A4. Go to settings", font=("Calibri", 12,), bg="#ffffff", fg="#000000")
    a3.pack(anchor="w", pady=(10,2))
