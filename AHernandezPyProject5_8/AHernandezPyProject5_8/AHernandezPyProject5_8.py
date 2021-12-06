import tkinter as tk
import tkinter.font as tkfont

app = tk.Tk()
app.winfo_toplevel().title("PyProject5_8")
app.geometry("640x480")
fontStyle = tkfont.Font(family="Verdana", size=18)

lblMessage = tk.Label(app, text="The system is idle.", font=fontStyle)

pixelVirtual = tk.PhotoImage(width=1, height=1)
lblMessage.pack(side=tk.TOP)



def sysOn():
    lblMessage.config(text="System Running.")

def sysOff():
    lblMessage.config(text="System Off.")

btnSysOn=tk.Button(app,text="System On", bg="grey", fg="black",image=pixelVirtual, width=200,height=100,compound="c", command = sysOn)
btnSysOn.place(x=100,y=400)
btnSysOff=tk.Button(app,text="System Off", bg="grey", fg="black",image=pixelVirtual, width=200,height=100,compound="c", command = sysOff)
btnSysOff.place(x=340,y=400)
btnExit=tk.Button(app,text="EXIT",command=app.quit)
btnExit.pack(side=tk.BOTTOM)

app.mainloop()