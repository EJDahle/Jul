from tkinter import *

def flytt_firkant():
    # Flytter alle objekt med "firkant1" tag-en 0 i x-retning og 1 i y-retning
    lærret.move('firkant1', 0, 1)
    
    # Passer på plasseringen til "firkant1"
    y = firkant_y.get() + 1

    # Dersom firkant1 forlater skjermen, skubbes den til toppen igjen
    if y > 600:
        firkant_y.set(0)
        lærret.move('firkant1', 0, -y)
    else:
        firkant_y.set(y)

    # Kjører funksjonen "flytt_firkant" etter 20 millisekund
    root.after(20, flytt_firkant)

root = Tk()

# Lager lærrete vi skal tegne på, og plasserer den i vinduet.
lærret = Canvas(root, width = 1000, height = 600, bg = 'white')
lærret.pack()

# Kode for å lage rette streker
lærret.create_line(100, 200, 200, 400)

# Et polygon er en mangekant. Vi kan "fylle" denne med en farge
lærret.create_polygon(200, 200, 400, 250, 300, 100, fill = "blue")

# En firkant kan tegnes med koden under:
lærret.create_rectangle(10, 10, 150, 150)

# Passer på plasseringen til objektet
firkant_y = IntVar()
firkant_y.set(0)

# Lager et objekt bundet til en tag
lærret.create_rectangle(500, firkant_y.get() - 20, 520, firkant_y.get(), fill = "gray90", tags = ("firkant1"))

# Kjører funksjonen flytt_firkant
flytt_firkant()




root.mainloop()
