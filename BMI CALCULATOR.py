from tkinter import *

def calculate():
    weight = float(w_entry.get())
    height = float(h_entry.get())

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        result = "Underweight"
    elif bmi < 25:
        result = "Normal"
    elif bmi < 30:
        result = "Overweight"
    else:
        result = "Obese"

    output.config(text="BMI = " + str(round(bmi,2)) + "\n" + result)

root = Tk()
root.title("BMI Calculator")
root.geometry("350x350")

Label(root, text="BMI Calculator", font=("Arial",18,"bold")).pack(pady=10)

Label(root, text="Enter Weight (kg)").pack()
w_entry = Entry(root)
w_entry.pack()

Label(root, text="Enter Height (m)").pack()
h_entry = Entry(root)
h_entry.pack()

Button(root, text="Calculate", command=calculate).pack(pady=10)

output = Label(root, text="", font=("Arial",14))
output.pack()

root.mainloop()
