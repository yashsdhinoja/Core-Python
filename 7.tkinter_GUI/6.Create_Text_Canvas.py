from tkinter import *

root = Tk()
root.title("Create_Text_Canvas")
root.geometry("500x500")

o = Canvas(root, bg="black", height=500, width=500, cursor="pencil")

fnt=('Times', 40, 'bold')
id = o.create_text(260, 100, text="Yash", font=fnt, fill="yellow", activefill="green")

fnt=('Arial', 35, 'bold italic underline')
id = o.create_text(260, 100, text="Kya Bolti Public", font=fnt, fill="red", activefill="white")

o.pack()
root.mainloop()