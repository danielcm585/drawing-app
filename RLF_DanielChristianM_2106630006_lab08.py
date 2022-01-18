from tkinter import Tk, Canvas, Frame, Button, Label, TOP, BOTTOM, BOTH, LEFT
from tkinter.colorchooser import askcolor

class Scribble(object):
    '''a simple pen drawing application'''

    def __init__(self):
        master = Tk()
        master.title('Simple Pen (Finger) Scribble')
        
        # Create instances of mouse coordinates and drawing color
        self.oldx, self.oldy = 0, 0
        self.color = 'green'
        
        # Create 400X250 canvas and bind mouse events to handlers
        self.canvas = Canvas(master=master, width=400, height=250, bg='white')
        self.canvas.bind("<Button-1>", self.begin)
        self.canvas.bind("<Button1-Motion>", self.draw)
        self.canvas.pack(expand=True, fill=BOTH)
        
        # Create a new frame to hold the buttons
        frame1 = Frame(master)
        frame1.pack(side=TOP)

        # Create clear and change color button
        self.bt_clear = Button(master=frame1, text='Clear', command=self.delete, bg='orange')
        self.bt_clear.pack(side=LEFT, padx=5)
        self.bt_color = Button(master=frame1, text='Color', command=self.change_color, bg=self.color)
        self.bt_color.pack(side=LEFT)

        # Create a message label
        self.message = Label(master=master, text='Press and drag the left mouse-button to draw', fg='blue')
        self.message.pack(side=BOTTOM)
        
        # Start the event loop
        master.mainloop()

    def begin(self, event):
        '''handles left button click by recording mouse position
        as the start of the curve'''
        
        # Set the mouse coordinates to current coordinates
        self.oldx, self.oldy = event.x, event.y

    def draw(self, event):
        '''handles mouse motion, while pressing left button, by
        connecting the previous mouse position to the new one'''

        # Create a line from last mouse coordinates to current coordinates
        self.canvas.create_line(self.oldx, self.oldy, event.x, event.y, fill=self.color)

        # Move the mouse coordinates to current coordinates
        self.oldx, self.oldy = event.x, event.y
    
    def delete(self):
        '''clear the canvas'''

        # Clear the canvas
        self.canvas.delete('all')
    
    def change_color(self):
        '''change the drawing color using the color chooser,
        also change the background color of the color button'''

        # Take the hex value from the color chooser
        self.color = askcolor()[-1] 

        # Change the drawing color 
        self.bt_color['bg'] = self.color

if __name__ == "__main__":
    Scribble()