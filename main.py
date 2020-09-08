from tkinter import *
from tkinter import messagebox
import geo

root = Tk()


def get_coordinates():
    coord = geo.getcoordinates(data.get())
    if coord:
        text_result.insert(0.0, coord + '\n')
        # messagebox.showinfo('Coordinates', coord)
    else:
        messagebox.showerror('Борода', 'Введите адресс')


root['bg'] = 'grey'
root.title("Геокодер")
root.geometry('300x250')
root.wm_attributes('-alpha', 0.9)
# root.iconbitmap('icon.ico')
root.resizable(width=False, height=False)

# Event
text = Label(text='Введите адрес', font='20', bg='#3d3d42', fg='#ccc')
data = Entry(root, font='Consolas 15', relief='solid', justify='center')
# check_status = Checkbutton(text='Test_check')
get_button = Button(text='Получить координаты', command=get_coordinates)

global text_result
text_result = Text(root, width='20', height='10', wrap=WORD)

# Packer
text.pack(pady=5)
data.pack(pady=5)
# check_status.pack()
get_button.pack(pady=5)
text_result.pack(pady=5)

root.mainloop()
