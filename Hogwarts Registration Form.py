# Use updated lackages
from tkinter import *
# Give a root file
root = Tk()
# Create a window with width and height
root.geometry("500x300")
# Create a submitted function
def submitted():
    print("Welcome to Hogwarts")
# Create a heading, row and column
Label(root, text="Hogwarts School of Witchcraft and Wizardry Admissions Application", font="ar 15 bold").grid(row=0, column=3)
# The necessary variables to apply the school
Name = Label(root, text="Name")
Gender = Label(root, text="Gender")
PhoneNumber = Label(root, text="Phone Number")
HybridorPure = Label(root, text="Hybrid/Pure")
Pet = Label(root, text="Pet")
# Packing the fields
Name.grid(row=1, column=2)
Gender.grid(row=2, column=2)
PhoneNumber.grid(row=3, column=2)
HybridorPure.grid(row=4, column=2)
Pet.grid(row=5, column=2)
# Create Variables to store the above 
Namevalue = stringVar
Gendervalue = stringVar
PhoneNumbervalue = IntVar
HybridorPurevalue = stringVar
Petvalue = stringVar
# Create the entry filed
nameentry = Entry(root, textvariable = Namevalue)
Genderentry = Entry(root, textvariable = Gendervalue)
PhoneNumberentry = Entry(root, textvariable = PhoneNumbervalue)
HybridorPureentry = Entry(root, textvariable = HybridorPurevalue)
Petentry = Entry(root, textvariable = Petvalue)
# Pack the entry filed
nameentry.grid(row=1,column=3)
Genderentryy.grid(row=2,column=3)
PhoneNumberentry.grid(row=3,column=3)
HybridorPureentr.grid(row=4,column=3)
Petentry.grid(row=5,column=3)
#Submitted Button
Button(text="Submit",command=submitted).grid(row=7,column=3)
# Name the main loop
root.mainloop()


