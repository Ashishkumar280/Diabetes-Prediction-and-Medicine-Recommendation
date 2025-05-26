import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Load diabetes data from CSV
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        messagebox.showerror("File Error", f"Could not load file: {e}")
        return None

# Example Diabetes Medication Lookup Table
medicine_table = {
    "Type 1 Diabetes": ["Insulin"],
    "Type 2 Diabetes": ["Metformin", "Sulfonylureas", "DPP-4 Inhibitors", "SGLT2 Inhibitors", "Insulin (if advanced)"],
    "Gestational Diabetes": ["Insulin (preferred)", "Metformin (if insulin not suitable)"],
    "Pre-Diabetes": ["Lifestyle changes", "Metformin (in some cases)"],
    "Non-Diabetic": ["No medication needed. Focus on lifestyle management."]
}

# Function to recommend medicine
def recommend_medicine(predicted_diabetes_type, glucose_level):
    if predicted_diabetes_type == "Non-Diabetic":
        return medicine_table["Non-Diabetic"]
    elif predicted_diabetes_type == "Pre-Diabetes":
        return medicine_table["Pre-Diabetes"]
    elif predicted_diabetes_type == "Type 1 Diabetes":
        return medicine_table["Type 1 Diabetes"]
    elif predicted_diabetes_type == "Type 2 Diabetes":
        if glucose_level >= 200:
            return ["Insulin"] + medicine_table["Type 2 Diabetes"]
        return ["Metformin"] + ["Sulfonylureas (if needed)"]
    elif predicted_diabetes_type == "Gestational Diabetes":
        return medicine_table["Gestational Diabetes"]
    return ["Consult a doctor for tailored recommendations"]

# Function to handle the form submission
def submit():
    try:
        pregnancies = int(entry_pregnancies.get())
        glucose = float(entry_glucose.get())
        blood_pressure = float(entry_blood_pressure.get())
        skin_thickness = float(entry_skin_thickness.get())
        insulin = float(entry_insulin.get())
        bmi = float(entry_bmi.get())
        diabetes_pedigree = float(entry_diabetes_pedigree.get())
        age = int(entry_age.get())

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values in all fields.")
        return

    # Prediction Logic
    if pregnancies > 0 and 140 <= glucose < 200:
        diabetes_type = "Gestational Diabetes"
    elif glucose < 100:
        diabetes_type = "Non-Diabetic"
    elif 100 <= glucose < 126:
        diabetes_type = "Pre-Diabetes"
    elif 126 <= glucose < 200:
        diabetes_type = "Type 2 Diabetes"
    else:
        if diabetes_pedigree > 0.5:
            diabetes_type = "Type 1 Diabetes"
        else:
            diabetes_type = "Type 2 Diabetes"

    # Recommend medicine based on prediction
    medicine_recommendations = recommend_medicine(diabetes_type, glucose)

    # Output Results
    messagebox.showinfo("Results", f"Diabetes Type: {diabetes_type}\nRecommended Medicines: {', '.join(medicine_recommendations)}")

# Function to handle cancellation and exit the program
def cancel():
    root.destroy()  # Close the application

# Set up the main window
root = tk.Tk()
root.title("Diabetes Prediction Input")
root.geometry("400x300")  # Set window size
root.configure(bg='#f7f7f7')  # Set background color

# Load data from CSV file
data = load_data('diabetes.csv')

# Create input fields with labels and customize appearance
label_style = {'bg': '#f7f7f7', 'font': ('Helvetica', 10)}
entry_style = {'font': ('Helvetica', 10), 'bg': '#e8e8e8'}

tk.Label(root, text="Pregnancies (Enter 0 if not applicable):", **label_style).grid(row=0, column=0, padx=10, pady=5)
entry_pregnancies = tk.Entry(root, **entry_style)
entry_pregnancies.grid(row=0, column=1)

tk.Label(root, text="Glucose level (mg/dL):", **label_style).grid(row=1, column=0, padx=10, pady=5)
entry_glucose = tk.Entry(root, **entry_style)
entry_glucose.grid(row=1, column=1)

tk.Label(root, text="Blood Pressure (mm Hg):", **label_style).grid(row=2, column=0, padx=10, pady=5)
entry_blood_pressure = tk.Entry(root, **entry_style)
entry_blood_pressure.grid(row=2, column=1)

tk.Label(root, text="Skin Thickness (mm):", **label_style).grid(row=3, column=0, padx=10, pady=5)
entry_skin_thickness = tk.Entry(root, **entry_style)
entry_skin_thickness.grid(row=3, column=1)

tk.Label(root, text="Insulin level (µU/mL):", **label_style).grid(row=4, column=0, padx=10, pady=5)
entry_insulin = tk.Entry(root, **entry_style)
entry_insulin.grid(row=4, column=1)

tk.Label(root, text="BMI (kg/m²):", **label_style).grid(row=5, column=0, padx=10, pady=5)
entry_bmi = tk.Entry(root, **entry_style)
entry_bmi.grid(row=5, column=1)

tk.Label(root, text="Diabetes Pedigree Function (e.g., 0.5):", **label_style).grid(row=6, column=0, padx=10, pady=5)
entry_diabetes_pedigree = tk.Entry(root, **entry_style)
entry_diabetes_pedigree.grid(row=6, column=1)

tk.Label(root, text="Age (years):", **label_style).grid(row=7, column=0, padx=10, pady=5)
entry_age = tk.Entry(root, **entry_style)
entry_age.grid(row=7, column=1)

# Add submit and cancel buttons with enhanced styles
submit_button = tk.Button(root, text="Submit", command=submit,
                           bg='lightgreen', font=('Helvetica', 12), relief='raised')
submit_button.grid(row=8, column=0)

cancel_button = tk.Button(root, text="Cancel", command=cancel,
                          bg='lightcoral', font=('Helvetica', 12), relief='raised')
cancel_button.grid(row=8, column=1)

# Run the tkinter main loop
root.mainloop()