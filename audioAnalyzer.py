# Code structure based on template provided by Dr. Navarro

from model import Model
from view import View
from controller import Controller
import tkinter as tk
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Audio Analyzer')
        # create a model
        model = Model('dummy.wav')
        # create a view and place it on the root window
        view = View(self)
        # create a controller
        controller = Controller(model, view)
        controller.NewAudio()
        # set the controller to view
        view.set_controller(controller)
        view.grid(row=0, column=0, padx=10, pady=10)
        

if __name__ == '__main__':
    app = App()
    app.mainloop()