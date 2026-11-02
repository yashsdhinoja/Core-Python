from tkinter import *

root = Tk()
root.title("Oval_Canvas")
root.geometry("700x700")

o = Canvas(root, bg="black", height=500, width=600, cursor='pencil')

# ======>>>>>>>>>> TO CREATE A OVAL SHAPE OR ELLIPSE <<<<<<<<<<<<<<<======

oval_1 = o.create_oval(100, 100, 400, 400, width=5, fill="yellow", outline="red", activefill="green", activeoutline="white", activewidth=10, activedash=(10, 5), activestipple="gray50", activeoutlinestipple="gray50")
# activefill, activeoutline => (Border of oval shape) means hover. 

# An item is active when the mouse pointer is on top of it. Each active... option is the normal option’s hover version. It is used only while the mouse is over the shape, and the shape returns to normal when the mouse leaves.

# Normal option	    Active (hover) option	        What changes on hover
#   fill	            activefill	                    inside color
#   outline	            activeoutline	                border color
#   width	            activewidth	                    border thickness
#   dash	            activedash	                    border becomes dashed
#   stipple	            activestipple	                inside gets a dotted/pattern fill
#   outlinestipple	    activeoutlinestipple	        border gets a dotted/pattern look

o.pack()

root.mainloop()