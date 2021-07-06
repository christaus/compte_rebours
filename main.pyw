from datetime import timezone
from datetime import datetime
from tkinter import *
import os
#dt = datetime(2021, 5, 22, 15, 55) YYYY,MM,DD,hh,mm
dt = datetime(2021, 7, 6, 11, 0)

chemin_script = os.path.abspath(__file__)
repertoire_script = chemin_script[
    : next(
        i
        for i in reversed(range(len(chemin_script)))
        if chemin_script[i] == os.path.sep
    )
    + 1
]


def plusla():
    # Année, mois, jour_du_mois, heure, minutes
    global dt
    dt_now = datetime.today()
    timestamp = round(dt.replace(tzinfo=timezone.utc).timestamp())
    timestamp_now = round(dt_now.replace(tzinfo=timezone.utc).timestamp())
    return timestamp - timestamp_now


def tick():
    heures = 0
    minutes = 0
    secondes = plusla()
    if secondes > 3599:
        heures = divmod(secondes, 3600)[0]
        secondes -= heures * 3600
    if secondes > 59:
        minutes = divmod(secondes, 60)[0]
        secondes -= minutes * 60
    lbl.config(
        text=f"Plus que\n{heures} heures\n{minutes} minutes\n{secondes} secondes !"
    )
    w.after(500, tick)


w = Tk()
w.title("Débauche !")
w.iconphoto(False, PhotoImage(file=f"{repertoire_script}icon.png"))
lbl = Label(w, text="Il ne reste plus beaucoup de temps !")
lbl.pack(expand=True, fill=BOTH)
tick()
w.mainloop()
