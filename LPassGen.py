from tkinter import *
from functools import partial
import random
root = Tk()
genrated = ''

def passgen():
    genrated = ''
    charlimitset = 0
    charlimitset = int(entry_chlimit.get())
    charlimitloop = charlimitset
    print(charlimitset)
    path = 'passletters.txt'
    letterlist = open(path,'r')
    ltrlist = letterlist.read().splitlines()
    print(ltrlist)
    while charlimitloop > 0 :
        genrated += random.choice(ltrlist)
        charlimitloop = charlimitloop - 1
    entry_name.delete('0',END)
    entry_name.insert('0',genrated)
    print(genrated)


text = genrated
label = Label(root, text='')
entry_name = Entry(root, textvariable=text)
longtext = Label(root, text='Character Limit:')
entry_chlimit = Entry(root)
button = Button(root, text='Generate', command=passgen)


entry_name.grid(column=0, row=1)
longtext.grid(column=0, row=3)
entry_chlimit.grid(column=0, row=4)
button.grid(column=0, row=5)

root.iconbitmap('iconefulltaille.ico')
root.mainloop() 