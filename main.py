from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import pandas as pd
import numpy as np
from openpyxl.utils.dataframe import dataframe_to_rows
import geo

root = Tk()


def get_coordinates():
    coord = geo.getcoordinates(data.get())
    if coord:
        text_result.insert(0.0, coord + '\n')
        # messagebox.showinfo('Coordinates', coord)
    else:
        messagebox.showerror('Борода', 'Введите адресс')


def get_coordinates_form_exel():
    # Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    try:
        text_result.insert(0.0, 'Вычисляем координаты...' + '\n')
        filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        data = pd.read_excel(filename)
        array = data['Address']
        mat = geo.getcoordinates_from_excel(array)
        data['Pos'] = mat
        data.to_excel(filename, index=False)
    except Exception:
        messagebox.showerror('Борода', 'Что-то пошло не так')
    else:
        messagebox.showinfo('Result', "Координаты записали в тот же файл, можно смотерть")
    pass


# настройка окна приложения
root['bg'] = 'grey'
root.title("Геокодер")
root.geometry('300x350')
root.wm_attributes('-alpha', 0.9)
# root.iconbitmap('icon.ico')
root.resizable(width=False, height=False)

# Event создание объектов для окна
text = Label(text='Введите адрес', font='20', bg='#3d3d42', fg='#ccc')
data = Entry(root, font='Consolas 15', relief='solid', justify='center')
# check_status = Checkbutton(text='Test_check')
get_button = Button(text='Получить координаты', command=get_coordinates)
get_button2 = Button(text='Загрузить файл c адресами', command=get_coordinates_form_exel)

global text_result
text_result = Text(root, width='20', height='10', wrap=WORD)

# Packer размещение объектов в окне
text.pack(pady=5)
data.pack(pady=5)
# check_status.pack()
get_button.pack(pady=5)
text_result.pack(pady=5)
get_button2.pack(pady=5)

# запуск приложения в цикле
root.mainloop()
