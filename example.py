import tkinter

# main window
window = tkinter.Tk()
window.geometry("400x300")

# input element
ent_1 = tkinter.Entry(window)
ent_1.pack()

# label element
lbl_1 = tkinter.Label(window)
lbl_1.pack()

# function to display input in lbl_1
def showInput():
	txt_show = ent_1.get()
	lbl_1["text"] = txt_show 

# button element
btn_1 = tkinter.Button(window, text = "click", command = showInput)
btn_1.pack()

# show program
window.mainloop()




