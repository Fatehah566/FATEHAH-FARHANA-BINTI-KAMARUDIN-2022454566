import tkinter as tk
from tkinter import ttk
import mysql.connector

# Link with MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="cat_treatment"
)

# Create cursor to execute SQL
mycursor = mydb.cursor()

# Calculation and database saving
def collect_data():
    treatment = type_of_treatment_combobox.get()
    disease = disease_entry.get()
    vaccine = vaccine_type_combobox.get()
    session = int(treatment_session_combobox.get())

    prices = {
        "Rabies FVRCP" : 90,
        "FelV VACCINE" : 85,
        "FHV-1" : 96,
        "ITRACONAZOLE" : 55,
        "TERBINAFINE" : 61,
        "FLUCONAZOLE" : 58,
    }

    total = (prices[vaccine] * session)


    output_label = tk.Label(root, text="")
    output_label.pack()
    output_label.config(text=f"Total teratment price: RM{total}")

    # To insert data in database
    sql = "INSERT INTO treatment_form(Type_of_Treatment, Disease, Vaccine_Type, Treatment_Session) VALUES(%s, %s, %s, %s)"
    val = (treatment, disease, vaccine, session)
    mycursor.execute(sql, val)
    mydb.commit()




root = tk.Tk()
root.title("Cat Treatment Form")
root.geometry("600x600")

frame = tk.Frame(root)
frame.pack()

#saving treatment information

treatment_information_frame = tk.LabelFrame(frame, text="Treatment Information")
treatment_information_frame.grid(row=0, padx=20, pady=10)

type_of_treatment_label = tk.Label(treatment_information_frame, text="Type of Treatment")
type_of_treatment_combobox = ttk.Combobox(treatment_information_frame, values=["Vaccine", "Fungus"])
type_of_treatment_label.grid(row=0, column=0)
type_of_treatment_combobox.grid(row=1, column=0)
type_of_treatment_combobox.set("Choose")
type_of_treatment_combobox["state"] = 'readonly'

disease_label = tk.Label(treatment_information_frame, text="Disease")
disease_label.grid(row=0, column=1)
disease_entry = tk.Entry(treatment_information_frame)
disease_entry.grid(row=1, column=1)


vaccine_type_label = tk.Label(treatment_information_frame, text="Vaccine Type")
vaccine_type_combobox = ttk.Combobox(treatment_information_frame, values=["Rabies FVRCP", "FelV VACCINE","FHV-1", "ITRACONAZOLE", 
                                                                          "TERBINAFINE", "FLUCONAZOLE"])
vaccine_type_label.grid(row=2, column=0)
vaccine_type_combobox.grid(row=3, column=0)
vaccine_type_combobox.set("Choose")
vaccine_type_combobox["state"] = 'readonly'

treatment_session = tk.Label(treatment_information_frame, text="Treatment Session")
treatment_session_combobox = ttk.Combobox(treatment_information_frame, values=["1", "2","3"])
treatment_session.grid(row=2, column=1)
treatment_session_combobox.grid(row=3, column=1)
treatment_session_combobox.set("Choose")
treatment_session_combobox["state"] = 'readonly+/'

for widget in treatment_information_frame.winfo_children():
    widget.grid(padx=10, pady=5)


# vaccine price
vaccine_price_text = tk.Text(root, height=20, width=38)
vaccine_price_text.pack(padx=40, pady=20)

# listing vaccine price list
vaccine_price_text.insert(tk.END, "Vaaccine & Prices :\n\n")
vaccine_price_text.insert(tk.END, "Rabies FVRCP : RM90.00\n\n")
vaccine_price_text.insert(tk.END, "FelV VACCINE : RM85.00\n\n")
vaccine_price_text.insert(tk.END, "FHV-1        : RM96.00\n\n")
vaccine_price_text.insert(tk.END, "ITRACONAZOLE : RM55.00\n\n")
vaccine_price_text.insert(tk.END, "TERBINAFINE  : RM61.00\n\n")
vaccine_price_text.insert(tk.END, "FLUCONAZOLE  : RM58.00\n\n")
vaccine_price_text.configure(state="disabled")

save_button = tk.Button(root, text="Calculate", command=collect_data)
save_button.pack(pady=10)






root.mainloop()
