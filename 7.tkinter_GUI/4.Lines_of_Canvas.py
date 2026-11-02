from tkinter import *

root = Tk()

root.title("Canvas")
root.geometry("900x900")

c = Canvas(root, bg="blue", height=500, width=600, cursor='pencil')

# ======>>>>>>>>>> TO CREATE A LINE. <<<<<<<<<<<<<<<======

# Line 1 (your original): a line with one bend
line1 = c.create_line(50, 30, 200, 50, 200, 150, width=4, fill="white")
# Line 2: a straight horizontal line
line2 = c.create_line(50, 250, 450, 250, width=4, fill="yellow")
# # Line 3: a square drawn with lines
line3 = c.create_line(300, 50, 450, 50, 450, 200, 300, 200, 300, 50, width=3, fill="red")
# Line 4: a mountain shape with an arrow at the end
line4 = c.create_line(50, 400, 250, 320, 450, 400, width=4, fill="red")
# Line 5: a dashed line
line5 = c.create_line(50, 450, 450, 450, width=4, fill="black", dash=(6,3))

c.pack()
root.mainloop()