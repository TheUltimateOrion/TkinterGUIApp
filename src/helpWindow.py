import os
from json import *
from tkinter import *
from tkinter.ttk import *

from PIL import Image, ImageTk


class HelpWindow(Toplevel):
    __empty: Frame
    __mainFrame: Frame
    __helpIcon: Label
    __helpText: Label
    __closeButton: Button
    __buttonFrame: Frame

    LIGHT_GRAY: str

    def __init__(self):
        super(HelpWindow, self).__init__()

        self.__mainFrame = Frame(self)

        _helpfile = open('res/helpWindow.json', mode='r')
        helpfile = loads(_helpfile.read())
        self._img = Image.open(helpfile['Icon']['url'])
        self.img = ImageTk.PhotoImage(self._img.resize((helpfile['Icon']['size'][0], helpfile['Icon']['size'][1]), Image.ANTIALIAS))

        self.__helpIcon = Label(self.__mainFrame, image=self.img)
        self.__helpText = Label(self.__mainFrame, text=helpfile['Text'], wraplength=250)
        self.__helpIcon.grid(column=0, row=0, padx=5, pady=10)
        self.__helpText.grid(column=1, row=0, padx=5, pady=10)

        self.LIGHT_GRAY = "#e5e5e5"

        style = Style()
        style.theme_use(os.environ.get('THEME'))
        style.configure("Button.TFrame", background=self.LIGHT_GRAY)
        style.configure("Close.TButton", background=self.LIGHT_GRAY)

        self.__buttonFrame = Frame(self, style="Button.TFrame")

        self.__buttonFrame.columnconfigure(0, weight=0)
        self.__buttonFrame.columnconfigure(1, weight=1)

        if len(helpfile['Buttons']) > 0:
            self.__closeButton = Button(self.__buttonFrame, text=helpfile['Buttons'][0], command=self.destroy, style="Close.TButton")
            self.__closeButton.grid(column=1, row=0, padx=10, pady=5, sticky=SE)

        self.__mainFrame.pack()
        self.__buttonFrame.pack(fill='x')
        self.title("Help")
