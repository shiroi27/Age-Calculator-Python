import tkinter as tk
from datetime import datetime
from tkinter import messagebox

def calculate_age():
    try:
        dob_text = dob_entry.get()
        time_text = time_entry.get()
        birth_str = f"{dob_text} {time_text}"
        birth_date = datetime.strptime(birth_str, "%d-%m-%Y %I:%M %p")
        now = datetime.now()

        if birth_date > now:
            messagebox.showerror("Invalid Date", "Date of birth cannot be in the future!")
            return

        delta = now - birth_date
        total_days = delta.days
        total_weeks = total_days // 7
        total_months = total_days // 30
        total_years = total_days // 365

        rem_months = (total_days % 365) // 30
        rem_weeks = ((total_days % 365) % 30) // 7
        rem_days = ((total_days % 365) % 30) % 7

        year_label.config(text=f"{total_years}")
        month_label.config(text=f"{rem_months}")
        week_label.config(text=f"{rem_weeks}")
        day_label.config(text=f"{rem_days}")
        asof_label.config(text=f"AS OF\n{now.strftime('%d-%m-%Y')}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid date and time (e.g., 13-08-1987, 5:30 PM).")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("650x550+500+200")
root.config(bg="#FFEC82")  

# Header
header = tk.Frame(root, bg="#3BF2FF", height=70)
header.pack(fill=tk.X)
title = tk.Label(header, text=" ~ AGE CALCULATOR ~ ", font=("Times New Roman", 32, "bold"), bg="#3BF2FF", fg="#000000")
title.pack(pady=15)

# Decorative line
line = tk.Frame(root, bg="#FF955C", height=7)
line.pack(fill=tk.X)

# Input Section
dob_frame = tk.Frame(root, bg="#FFEC82")
dob_frame.pack(pady=20)

tk.Label(dob_frame, text="DATE OF BIRTH", font=("Times New Roman", 21, "bold"), bg="#FFEC82", fg="#000000").pack()
dob_entry = tk.Entry(dob_frame, width=20, font=("Times New Roman", 17, "bold"))
dob_entry.pack(pady=5)

tk.Label(dob_frame, text="TIME OF BIRTH", font=("Times New Roman", 21, "bold"), bg="#FFEC82", fg="#000000").pack()
time_entry = tk.Entry(dob_frame, width=20, font=("Times New Roman", 17, "bold"))
time_entry.pack(pady=5)

# Calculate Button
calc_btn = tk.Button(root, text="Calculate Age", command=calculate_age, font=("Times New Roman", 21, "bold"), bg="#FFCA28"
, fg="#000000", width=18)
calc_btn.pack(pady=20)

# Result Display
result_frame = tk.Frame(root, bg="#FFEC82")
result_frame.pack(pady=10)

tk.Label(result_frame, text="YOU ARE", font=("Times New Roman", 19, "bold"), bg="#FFEC82", fg="#000000").pack()

top_row = tk.Frame(result_frame, bg="#FFEC82")
top_row.pack(pady=2)
year_label = tk.Label(top_row, text="0", font=("Times New Roman", 21, "bold"), bg="#FFEC82", fg="#000000")
year_label.pack(side=tk.LEFT)
tk.Label(top_row, text="Years", font=("Times New Roman", 21, "bold"), bg="#FFEC82", fg="#000000").pack(side=tk.LEFT, padx=10)

month_label = tk.Label(top_row, text="0", font=("Times New Roman", 21, "bold"), bg="#FFEC82", fg="#000000")
month_label.pack(side=tk.LEFT)
tk.Label(top_row, text="Months", font=("Times New Roman", 21, "bold"), bg="#FFEC82", fg="#000000").pack(side=tk.LEFT, padx=10)

bottom_row = tk.Frame(result_frame, bg="#FFEC82")
bottom_row.pack(pady=2)
week_label = tk.Label(bottom_row, text="0", font=("Times New Roman", 21, "bold"), bg="#FFEC82", fg="#000000")
week_label.pack(side=tk.LEFT)
tk.Label(bottom_row, text="Weeks", font=("Times New Roman", 21, "bold"), bg="#FFEC82", fg="#000000").pack(side=tk.LEFT, padx=10)

day_label = tk.Label(bottom_row, text="0", font=("Times New Roman", 21, "bold"), bg="#FFEC82", fg="#000000")
day_label.pack(side=tk.LEFT)
tk.Label(bottom_row, text="Days", font=("Times New Roman", 21, "bold"), bg="#FFEC82", fg="#000000").pack(side=tk.LEFT, padx=10)

asof_label = tk.Label(result_frame, text="", font=("Times New Roman", 21), bg="#FFEC82", fg="#000000")
asof_label.pack(pady=10)

root.mainloop()