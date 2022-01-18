from tkinter import *

def main():
    global drawing_area

    root = Tk()
    root.title("Drawer")
    drawing_area = Canvas(root, width=300, height=300, bg="white")

    # Binding Events to the canvas
    drawing_area.bind("<B1-Motion>", drag)
    drawing_area.bind("<ButtonRelease-1>", drag_end)
    drawing_area.pack()

    # Buttons
    # Quit Button
    b1 = Button(root, text="Quit")
    b1.pack()
    b1.bind("<Button-1>", quit)

    # Clear Button
    b2 = Button(root, text="Clear")
    b2.pack()
    b2.bind("<Button-1>", clear)

    # Save Button
    b3 = Button(root, text="Save")
    b3.pack()
    b3.bind("<Button-1>", save)
    root.mainloop()
