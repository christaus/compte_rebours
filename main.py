from datetime import timezone
from datetime import datetime
from tkinter import *

def plusla():
    dt = datetime(2020, 7, 21, 17)
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
    lbl.config(text = f'Plus que\n{heures} heures\n{minutes} minutes\n{secondes} secondes !')
    w.after(500, tick)                                

w = Tk()
w.title('Débauche !')
lbl = Label(w, text = 'Il ne reste plus beaucoup de temps !')
lbl.pack(expand = True, fill = BOTH)
tick()
w.mainloop()
