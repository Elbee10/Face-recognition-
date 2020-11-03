from tkinter import *
from PIL import ImageTk, Image
import pymysql

connection = pymysql.connect(host="localhost",user="root",passwd="",database="attendance")
cursor = connection.cursor()






if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    gui.configure(background='grey')
    gui.title('Student attendance')
    gui.geometry('1800x700')

    topFrame = Frame(gui, bg='grey', width=400, height=10, pady=19, padx=19)
    center = Frame(gui, bg='gray', width=400, height=10, padx=0, pady=0)
    btm_frame = Frame(gui, bg='white', width=450, height=45, pady=3)
    btm_frame2 = Frame(gui, bg='lavender', width=450, height=60, pady=3)

    gui.grid_rowconfigure(1, weight=1)
    gui.grid_columnconfigure(0, weight=1)

    topFrame.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="ew")
    btm_frame.grid(row=3, sticky="ew")
    btm_frame2.grid(row=4, sticky="ew")


    w = Label( topFrame, text="Welcome to the school face recognition attendance", font = "Verdana 20 bold", bg='grey')

    #center.grid_rowconfigure(0, weight=1)
    #center.grid_rowconfigure(3, weight=1)
    center.grid_columnconfigure(0, weight=2)
    center.grid_columnconfigure(3, weight=2)

    login = Button(center, text='Login')
    Quit = Button(center, text='Quit', command=quit)
    img = Image.open("/Users/alibarma/workspace/Face-recognition-/schoolLogo.jpg")
    img = img.resize((1600, 300), Image.ANTIALIAS)
    img=ImageTk.PhotoImage(img)
    imgPanel = Label(topFrame, image = img)






    w.grid(row=0, columnspan=2)
    login.grid(row=1, column=2, sticky='w')
    Quit.grid(row=1, column=3)
    imgPanel.grid(row=1, column=1)




    gui.mainloop()
