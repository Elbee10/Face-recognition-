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
    gui.geometry('900x700')

    Grid.rowconfigure(gui, 0, weight=1)
    Grid.columnconfigure(gui, 0, weight=1)

    topFrame = Frame(gui, bg='grey', width=400, height=10, pady=19, padx=19)
    center = Frame(gui, bg='grey', width=400, height=10, padx=0, pady=0)
    btm_frame2 = Frame(gui, bg='grey', width=450, height=60, pady=3)



    topFrame.grid(row=0, sticky=N+S+E+W)
    center.grid(row=1, sticky=N+S+E+W)
    btm_frame2.grid(row=2, sticky=N+S+E+W)



    w = Label( topFrame, text="Welcome to the school face recognition attendance", font = "Verdana 20 bold", bg='grey')
    copy = Label( btm_frame2, text="Copy right Munyema Jr. 2020", font = "Verdana12", bg='grey')
    adminLabel = Label(center, text='Click for Administrator panel', font='Verdana12', bg='grey')
    usernameLabel = Label( center, text="Username", font = "Verdana12", bg='grey')
    passwordLabel = Label( center, text="Password", font = "Verdana12", bg='grey')


    for i in range(2):
        topFrame.grid_rowconfigure(i, weight=1)
        topFrame.grid_columnconfigure(i, weight=1)
        center.grid_columnconfigure(i, weight=1)
    for i in range(5):
        center.grid_rowconfigure(i, weight=1)
        btm_frame2.grid_columnconfigure(0, weight=1)
    btm_frame2.grid_rowconfigure(0, weight=1)



    login = Button(center, text='Login', width=5, height=1)
    admin = Button(center, text='Administrator')
    passwordInput = Entry(center, show='*')
    usernameInput = Entry(center)


    img = Image.open("/Users/alibarma/workspace/Face-recognition-/schoolLogo.jpg")
    img = img.resize((1000, 300), Image.ANTIALIAS)
    img=ImageTk.PhotoImage(img)
    imgPanel = Label(topFrame, image = img)

    w.grid(row=0, columnspan=2)
    copy.grid(row=0, column=4)

    passwordLabel.grid(row=3,column=1)
    usernameLabel.grid(row=1,column=1)
    adminLabel.grid(row=1, column=0)

    passwordInput.grid(row=4,column=1, pady=1)
    usernameInput.grid(row=2,column=1, pady=1)

    login.grid(row=5, column=1, pady=15)
    admin.grid(row=2, column=0, pady=15)
    imgPanel.grid(row=1, column=1)




    gui.mainloop()
