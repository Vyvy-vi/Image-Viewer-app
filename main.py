from tkinter import *
import PIL
from PIL import Image, ImageTk

wind= Tk()
i1= ImageTk.PhotoImage(Image.open("images/index.jpg"))
i2= ImageTk.PhotoImage(Image.open("images/index2.jpg"))
i3= ImageTk.PhotoImage(Image.open("images/index3.jpg"))
i4= ImageTk.PhotoImage(Image.open("images/index4.jpg"))
i5= ImageTk.PhotoImage(Image.open("images/images5.jpg"))
img_list=[i1,i2,i3,i4,i5]
fr = LabelFrame(wind, padx=5, pady=5)
fr.grid(row=0, column=0, columnspan= 3, padx=8, pady=8)
l = Label(fr,image= i1)
#l.grid(row=0, column =0, columnspan= 3)
l.grid(row=0, column=0)
status = Label(wind, text= f'Image 1 of {len(img_list)}', bd=1, relief=SUNKEN,anchor=E)
def img_list_gen():
    #TODO
    return


global index
index=0
def next():
    global l
    global index
    if index != len(img_list)-1:
        index+=1
        l.grid_forget()
        l= Label(fr,image= img_list[index])
        #l.grid(row= 0, column= 0, columnspan= 3)
        l.grid(row =0, column= 0)
    else:
        next_but = Button(wind, text='>>', state= DISABLED)
    # stat_update
    status = Label(wind, text= f'Image {index+1} of {len(img_list)}', bd=1, relief=SUNKEN,anchor=E)
    status.grid(row =3, column=0, columnspan=3, sticky=W+E)

def prev():
    global l
    global index
    if index!=0:
        index-=1
        l.grid_forget()
        l= Label(fr, image= img_list[index])
        #l.grid(row= 0, column= 0, columnspan=3)
        l.grid(row= 0, column= 0)
    else:
        back_but = Button(wind, text='<<', state= DISABLED)
    # stat_update
    status = Label(wind, text= f'Image {index+1} of {len(img_list)}', bd=1, relief=SUNKEN,anchor=E)
    status.grid(row =3, column=0, columnspan=3, sticky=W+E)
exit_but= Button(wind, text="EXIT", command= wind.quit)
back_but= Button(wind, text="<<", command=prev)
next_but= Button(wind, text=">>", command=next)

back_but.grid(row =1, column =0)
exit_but.grid(row =1, column =1, pady=5) # pady
next_but.grid(row =1, column =2)

wind.title('Image Viewer')
status.grid(row =3, column=0, columnspan=3, sticky=W+E)
wind.mainloop()
