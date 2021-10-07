from tkinter import*
from tkinter import ttk

root=Tk()
root.title("Canvas Thingy")
root.geometry("600x600")
root.maxsize(600,600)

colorlabel=Label(root,text="Color: ")
colorlabel.place(relx=0.81,rely=0.9,anchor=CENTER)

colorvals = ["black", "yellow", "cyan", "blue", "red"]

selcol = StringVar()

colorbox = ttk.Combobox(root, values = colorvals, textvariable=selcol, width=10,state="readonly")
colorbox.place(relx=0.91,rely=0.9,anchor=CENTER)

strxlabel=Label(root,text="Start X: ")
strxlabel.place(relx=0.11,rely=0.9,anchor=CENTER)

strxvals = [200, 400, 600]

selstrx = StringVar()

srtxbox = ttk.Combobox(root, values = strxvals, textvariable=selstrx, width=10,state="readonly")
srtxbox.place(relx=0.21,rely=0.9,anchor=CENTER)

strylabel=Label(root,text="Start Y: ")
strylabel.place(relx=0.11,rely=0.97,anchor=CENTER)

stryvals = [200, 400, 600]

selstry = StringVar()

strybox = ttk.Combobox(root, values = stryvals, textvariable=selstry, width=10,state="readonly")
strybox.place(relx=0.21,rely=0.97,anchor=CENTER)

endxlabel=Label(root,text="End X: ")
endxlabel.place(relx=0.41,rely=0.9,anchor=CENTER)

endxvals = [200, 400, 600]

selendx = StringVar()

endxbox = ttk.Combobox(root, values = endxvals, textvariable=selendx, width=10,state="readonly")
endxbox.place(relx=0.55,rely=0.9,anchor=CENTER)

endylabel=Label(root,text="Color: ")
endylabel.place(relx=0.41,rely=0.97,anchor=CENTER)

endyvals = [400, 600, 200]

selendy = StringVar()

endybox = ttk.Combobox(root, values = endyvals, textvariable=selendy, width=10,state="readonly")
endybox.place(relx=0.55,rely=0.97,anchor=CENTER)






canvas=Canvas(root, width=590, height=510, bg='white', highlightbackground="lightgray")




canvas.pack()
root.mainloop()