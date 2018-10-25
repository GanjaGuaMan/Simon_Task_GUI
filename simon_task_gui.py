from tkinter import *
import random
import time


class SimonGUI():
    def __init__(self, root):
        self.__window = root
        self.__window.title("Simon Effect Tester")

        self.__canvas = Canvas(self.__window)
        self.__canvas.config(width = 1200)
        self.__canvas.config(height = 800)

        self.__frame = Frame(self.__window)
        
        
        self.__nr_label = Label(self.__frame)
        self.__nr_label.config(text = "nr stimuli")
        self.__nr_label.config(font = "CourierNew 20 bold")
        self.__nr_label.pack(side = 'left')

        self.__nr_entry = Entry(self.__frame)
        self.__nr_entry.config(background = 'white')
        self.__nr_entry.config(font = "CourierNew 20 bold")
        self.__nr_entry.config(justify = RIGHT)
        self.__nr_entry.config(width = 5)
        self.__nr_entry.pack(side = 'left')

        self.__ms_label = Label(self.__frame)
        self.__ms_label.config(text = "ms between")
        self.__ms_label.config(font = "CourierNew 20 bold")
        self.__ms_label.pack(side = 'left')

        self.__ms_entry = Entry(self.__frame)
        self.__ms_entry.config(background = 'white')
        self.__ms_entry.config(font = "CourierNew 20 bold")
        self.__ms_entry.config(justify = RIGHT)
        self.__ms_entry.config(width = 5)
        self.__ms_entry.pack(side = 'left')

        self.__msv_label = Label(self.__frame)
        self.__msv_label.config(text = "ms visible")
        self.__msv_label.config(font = "CourierNew 20 bold")
        self.__msv_label.pack(side = 'left')

        self.__msv_entry = Entry(self.__frame)
        self.__msv_entry.config(background = 'white')
        self.__msv_entry.config(font = "CourierNew 20 bold")
        self.__msv_entry.config(justify = RIGHT)
        self.__msv_entry.config(width = 5)
        self.__msv_entry.pack(side = 'left')

        self.__button_startnew = Button(self.__frame)
        self.__button_startnew.config(text = "Start New Simon Task")
        self.__button_startnew.config(font = "CourierNew 20 bold")
        self.__button_startnew.pack(side = 'left')

        self.__button_cancel = Button(self.__frame)
        self.__button_cancel.config(text = "Cancel")
        self.__button_cancel.config(font = "CourierNew 20 bold")
        self.__button_cancel.pack(side = 'left')

        self.__button_help = Button(self.__frame)
        self.__button_help.config(text = "Help")
        self.__button_help.config(font = "CourierNew 20 bold")
        self.__button_help.pack(side = 'left')
        
        self.__button_help.bind("<Button-1>", self.__HelpButtonHandler)
        self.__button_startnew.bind("<Button-1>", self.__StartHandler)

        self.c = 0

        
        self.__frame.pack(side = 'bottom')
        self.__canvas.pack()

    def __HelpButtonHandler(self, event):
        
        self.c = self.c + 1
        self.__canvas.create_text(100,100,anchor = NW,fill="black",font="CourierNew 20 bold",
                        text="welcome to the Simon Task\n\nblue square: press the 'q' key\n\nred square: press the 'p' key\n\npress Start button to start task")
        if self.c % 2 == 0:
            self.__canvas.delete(ALL)
                
    def __StartHandler(self, event):
        self.a = 0
        self.__rectanglebreak = int(self.__msv_entry.get())
        self.__recbetween = int(self.__ms_entry.get())
        self.__recreps = int(self.__nr_entry.get())
        self.__window.after(self.__rectanglebreak, self.__StartHandler2)

    def __clear(self, sec):
        self.__window.update()
        time.sleep(sec)
        self.__canvas.delete(ALL)



    def __StartHandler2(self):
        if self.__recreps > self.a:
            randnum = random.randint(1,4)
            if randnum == 1:
                self.__canvas.create_rectangle(100,400,300,200,fill = 'red', tags = "RSquareI")
                self.__clear(2)
            elif randnum == 2:
                self.__canvas.create_rectangle(100,400,300,200,fill = 'blue', tags = "BSquareI")
                self.__clear(2)
            elif randnum == 3:
                self.__canvas.create_rectangle(1100,400,900,200,fill = 'red', tags = "RSquareC")
                self.__clear(2)
            elif randnum == 4:
                self.__canvas.create_rectangle(1100,400,900,200,fill = 'blue', tags = "BSquareC")
                self.__clear(2)
 
        self.a = self.a + 1
        self.__window.after(self.__rectanglebreak, self.__StartHandler2)       
        
        


def main():
    root = Tk()
    window = SimonGUI(root)
    root.mainloop()


main()


