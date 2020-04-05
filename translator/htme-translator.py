#author: Francesco Zucca (discord: Francesco#0894)

import eng_to_ipa as ipa
import tkinter
from tkinter import messagebox
from tkinter import font

def translate(root, inp, res):
    inp=inp.replace("¿"," ").replace("¡"," ")
    ph = ipa.convert(inp, stress_marks="secondary").replace("ˌ","").replace("aɪ","1").replace("o","2").replace("ʧ","3").replace("aʊ","4").replace("ɔɪ","5")
    print(ph)
    if not ipa.isin_cmu(inp):
        print("A word (marked with * at the end) could not be translated into phonemes.")
        print("You get this warn if you have a ¿ or ¡, too, because of the way I impemented it.")
    res.delete(1.0, "end-1c")
    res.insert(1.0, ph.replace("* ","¿").replace("* ","¡"))
    

top=tkinter.Tk()
top.title("HTME Translator")
top.geometry("360x408+10+10")
top.tk.call('wm', 'iconphoto', top._w, tkinter.PhotoImage(file='htme.gif'))

head=tkinter.Frame(height=20)
left=tkinter.Frame(width=10)
right=tkinter.Frame(width=10)
head.pack()
left.pack(side="left")
right.pack(side="right")

htmefont = font.Font(root=top, family="HTME Language", size=24)
htmeevo = font.Font(root=top, family="HTME Language evolution 1", size=24)
copy = font.Font(root=top, family="Helvetica", size=8)

w = tkinter.Text(master=top, bg="white", height=10, width=40)
w.pack(fill="x")

r = tkinter.Text(master=top, bg="white", height=4, width=50)
r.config(font=htmeevo)

b = tkinter.Button(master=top, text="Translate!", command = lambda: translate(top, w.get("1.0", "end-1c"), r))
q = tkinter.Button(master=top, text="¿", command = lambda: w.insert("insert", "¿"))
e = tkinter.Button(master=top, text="¡", command = lambda: w.insert("insert", "¡"))
b.place(relx=0.37,rely=0.5)
q.place(relx=0.3,rely=0.5)
e.place(relx=0.55,rely=0.5)

author = tkinter.Text(master=top, height=1, width=55)
author.insert(1.0, "Made by Francesco Zucca (discord Francesco#0894). Do not steal.")
author.config(state="disabled", font=copy)
author.pack(side="bottom")
r.pack(side="bottom", fill="x")

top.mainloop()
