from tkinter import *

root=Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")
root.configure(background="aqua")

label_planet = Label(root, text="Planet : ", bg="aqua")
label_planet_name = Label(root, font=("courier", 18, "bold"), bg="aqua")
label_planet_image = Label(root, bg="gold2", highlightthickness=5, borderwidth=2, relief=SOLID)
label_planet_gravity_radius = Label(root, font=("castellar"), bg="aqua")
label_planet_info = Label(root, font=("courier",10,"bold"), bg="aqua", wraplength=5)

def PlanetInfo():
    print("Planet")
    
btn = Button(root, text="Show planet Info", command=PlanetInfo)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)

label_planet.place(relx=0.2, rely=0.1, anchor=CENTER)
label_planet_name.place(relx=0.5, rely=0.25, anchor=CENTER)
label_planet_image.place(relx=0.5, rely=0.5, anchor=CENTER)
label_planet_gravity_radius.place(relx=0.5, rely=0.8, anchor=CENTER)
label_planet_info.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()