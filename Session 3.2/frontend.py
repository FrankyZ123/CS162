#tutorial used: https://www.youtube.com/watch?v=ddoPYppcppc

#import everything from tkinter

from tkinter import *
import random
import string
TK_SILENCE_DEPRECATION=1

#Create Window object
window=Tk()

#define four labels Title Author Year ISBN
l1=Label(window, text="Title")
l1.grid(row=0, column=0)

for i in range(0, 10):
    for j in range(0, 10):
        rando_str=''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        l_cur=Label(window, text="{}".format(rando_str))
        l_cur.grid(row=i, column=j)

window.mainloop()