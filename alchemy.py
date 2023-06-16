from tkinter import *
import random

window = Tk()
window.geometry('600x600')
window.title('Alchem')

class Steam:
    image = PhotoImage(file=r'D:\с компа\python\aroma.png').subsample(4,4)

class Water:
    image = PhotoImage(file=r'D:\с компа\python\water.png').subsample(4,4)

    def __add__(self, other):
        if isinstance(other,Fire):
            return Steam

class Fire:
    image = PhotoImage(file=r'D:\с компа\python\fire.png').subsample(4,4)

class Wind:
    image = PhotoImage(file=r'D:\с компа\python\wind.png').subsample(4,4)

class Ground:
    image = PhotoImage(file=r'D:\с компа\python\ground.png').subsample(4,4)


canvas = Canvas(width=600,height=600)
canvas.pack()
elements = [Wind(),Fire(),Water(),Ground()]
for elem in elements:
    canvas.create_image(random.randint(50,550),random.randint(50,550),image=elem.image)

def move(event):
    images_ids = canvas.find_overlapping(event.x,event.y,event.x +10,event.y+10)
    if len(images_ids)==2:
        elem_id_1, elem_id_2 = images_ids[0],images_ids[1]
        elem_1 = elements[elem_id_1-1]
        elem_2 = elements[elem_id_2-1]
        new_elem = elem_1 + elem_2
        if new_elem not in elements:
            elements.append(new_elem)
            canvas.create_image(event.x,event.y,image=new_elem.image)

window.bind('<B1-Motion>', move)

window.mainloop()