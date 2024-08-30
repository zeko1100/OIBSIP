import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

# Define file for data storage
DATA_FILE = 'bmi_data.csv'

# Initialize the data file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'Weight', 'Height', 'BMI', 'Category', 'Date'])

# Function to calculate BMI
def calculate_bmi(weight, height):
    try:
        weight = float(weight)
        height = float(height)
        bmi = weight / (height / 100) ** 2
        category = categorize_bmi(bmi)
        return round(bmi, 2), category
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for weight and height.")
        return None, None

# Function to categorize BMI
def categorize_bmi(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal weight'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obesity'

# Function to save data
def save_data(username, weight, height, bmi, category):
    with open(DATA_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, weight, height, bmi, category, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

# Function to display historical data
def display_history(username):
    data = []
    with open(DATA_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row[0] == username:
                data.append(row)

    if not data:
        messagebox.showinfo("No Data", f"No data found for user: {username}")
        return

    history_window = tk.Toplevel(root)
    history_window.title(f"{username}'s BMI History")
    tree = ttk.Treeview(history_window, columns=("Date", "Weight", "Height", "BMI", "Category"), show='headings')
    tree.heading("Date", text="Date")
    tree.heading("Weight", text="Weight (kg)")
    tree.heading("Height", text="Height (cm)")
    tree.heading("BMI", text="BMI")
    tree.heading("Category", text="Category")
    tree.pack(fill=tk.BOTH, expand=True)

    for entry in data:
        tree.insert('', 'end', values=(entry[5], entry[1], entry[2], entry[3], entry[4]))

# Function to plot BMI trend
def plot_bmi_trend(username):
    dates = []
    bmis = []
    with open(DATA_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row[0] == username:
                dates.append(datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S'))
                bmis.append(float(row[3]))

    if not dates:
        messagebox.showinfo("No Data", f"No data found for user: {username}")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(dates, bmis, marker='o')
    plt.title(f"BMI Trend for {username}")
    plt.xlabel('Date')
    plt.ylabel('BMI')
    plt.grid(True)
    plt.show()

# Main Application Window
root = tk.Tk()
root.title("BMI Calculator")

# Input Fields
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Height (cm):").grid(row=2, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1, padx=10, pady=10)

# Calculate and Display BMI
def calculate_and_display():
    username = username_entry.get()
    weight = weight_entry.get()
    height = height_entry.get()

    if not username or not weight or not height:
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return

    bmi, category = calculate_bmi(weight, height)
    if bmi is not None:
        result_label.config(text=f"BMI: {bmi} ({category})")
        save_data(username, weight, height, bmi, category)

tk.Button(root, text="Calculate BMI", command=calculate_and_display).grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# View History Button
tk.Button(root, text="View History", command=lambda: display_history(username_entry.get())).grid(row=5, column=0, columnspan=2, pady=10)

# Plot Trend Button
tk.Button(root, text="Plot BMI Trend", command=lambda: plot_bmi_trend(username_entry.get())).grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
