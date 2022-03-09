import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *

from helpWindow import HelpWindow

class App(Tk):
    __menubar: Menu
    __file_menu: Menu
    __help_menu: Menu
    __theme_menu: Menu

    __numFrame: LabelFrame
    __label1: Label
    __num1: Entry
    __label2: Label
    __num2: Entry

    __button_frame: Frame
    __add_button: Button
    __sub_button: Button
    __mul_button: Button
    __div_button: Button

    LIGHT_GRAY: str

    def __init__(self) -> None:
        super(App, self).__init__()

        self.style: Style = Style()
        self.theme_name: StringVar = StringVar()
        self.title("Calculator")
        self.resizable(False, False)

        self.__menubar = Menu(self)
        self.config(menu=self.__menubar)

        self.__help_menu = Menu(self.__menubar, tearoff=False)
        self.__help_menu.add_command(label="About", command=self.help)

        self.__file_menu = Menu(self.__menubar, tearoff=False)
        self.__theme_menu = Menu(self.__file_menu, tearoff=False)
        for theme in self.style.theme_names():
            self.__theme_menu.add_radiobutton(label=theme, variable=self.theme_name, command=lambda: self.change_theme(self.theme_name.get()))

        self.__file_menu.add_cascade(label="Themes", menu=self.__theme_menu)
        self.__file_menu.add_separator()
        self.__file_menu.add_command(label="Exit", command=self.destroy)

        self.__menubar.add_cascade(label="File", menu=self.__file_menu, underline=0)
        self.__menubar.add_cascade(label="Help", menu=self.__help_menu, underline=0)

        self.style.configure("InputFrame.TLabelframe", foreground="gray")

        self.__numFrame = LabelFrame(self, text="Numbers", style="InputFrame.TLabelframe")
        self.__numFrame.grid(column=0, row=0, sticky=NW, padx=5, pady=5)

        self.__label1 = Label(self.__numFrame, text="Number A: ")
        self.__label1.grid(column=0, row=0, padx=5)

        self.__num1 = Entry(self.__numFrame)
        self.__num1.grid(column=1, row=0, padx=5)

        self.__label2 = Label(self.__numFrame, text="Number B: ")
        self.__label2.grid(column=0, row=1)

        self.__num2 = Entry(self.__numFrame)
        self.__num2.grid(column=1, row=1)

        self.LIGHT_GRAY = "#e5e5e5"

        self.style.configure("ButtonFrame.TFrame", background=self.LIGHT_GRAY)
        self.style.configure("ButtonFrame.TButton", background=self.LIGHT_GRAY)

        self.__button_frame = Frame(self, style="ButtonFrame.TFrame")

        self.__add_button = Button(self.__button_frame, text="Sum", style="ButtonFrame.TButton",
                                   command=lambda: App.add_window(int(self.__num1.get()), int(self.__num2.get())))
        self.__add_button.grid(column=0, row=0, padx=5, pady=1)

        self.__sub_button = Button(self.__button_frame, text="Difference", style="ButtonFrame.TButton",
                                   command=lambda: App.sub_window(int(self.__num1.get()), int(self.__num2.get())))
        self.__sub_button.grid(column=0, row=1, padx=5, pady=1)

        self.__mul_button = Button(self.__button_frame, text="Product", style="ButtonFrame.TButton",
                                   command=lambda: App.mul_window(int(self.__num1.get()), int(self.__num2.get())))
        self.__mul_button.grid(column=0, row=2, padx=5, pady=1)

        self.__div_button = Button(self.__button_frame, text="Quotient", style="ButtonFrame.TButton",
                                   command=lambda: App.div_window(int(self.__num1.get()), int(self.__num2.get())))
        self.__div_button.grid(column=0, row=3, padx=5, pady=1)

        self.__button_frame.grid(column=1, row=0, sticky=NE)

    @staticmethod
    def add_window(a: int, b: int) -> None:
        showinfo("Sum", str(int(a) + int(b)))
        return

    @staticmethod
    def sub_window(a: int, b: int) -> None:
        showinfo("Sum", str(int(a) - int(b)))
        return

    @staticmethod
    def mul_window(a: int, b: int) -> None:
        showinfo("Sum", str(int(a) * int(b)))
        return

    @staticmethod
    def div_window(a: int, b: int) -> None:
        showinfo("Sum", str(int(a) / int(b)))
        return

    def change_theme(self, theme: StringVar | str) -> None:
        os.environ['THEME'] = theme
        print(os.environ.get('THEME'))
        self.style.theme_use(theme)
        return

    @staticmethod
    def help():
        help_window: HelpWindow = HelpWindow()
        help_window.mainloop()

if __name__ == '__main__':
    app: App = App()
    app.mainloop()
