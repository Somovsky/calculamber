from math import sqrt
from decimal import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from decimal import *

#Создаем класс для окна приложения
class Window(ttk.Frame):
    # основные настройки
    def __init__(self, master):
        super().__init__(master, padding=2)
        self.create_variables()
        self.create_widgets()
        self.create_layout()
        self.bind_buttons()

    #создание перемнных
    def create_variables(self):
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.var3 = tk.StringVar()
        self.var3.set('0')
        self.localizations = dict(English=['Calculate', 'Enter number:', 'Answer:', 'About', 'Calculamber\nAutors: Teplouhov Vladislav, Nikolay Perminov\nOfficial page: http://en.k0per.design/\nВерсия: 1.0', 'Digits after the decimal point:', 'Calculamber', 'Error'],
                                  Русский=['Посчитать', 'Введите число:', 'Ответ:', 'О программе', 'Калькулямбер\nАвторы: Теплоухов Владислав, Николай Перминов\nОфициальный сайт: http://ru.k0per.design/\nВерсия: 1.0', 'Цифр после запятой:', 'Калькулямбер', 'Ошибка'],
                                  Український=['Порахувати', 'Введіть число:', 'Відповідь:', 'Про програму', 'Калькулямбер\nАвтори: Теплоухов Владiслав, Нiколай Пермiнов\nОфіційний сайт: http://ua.k0per.design/\nВерсiя 1.0', 'Цифр після коми:', 'Калькулямбер', 'Помилка'])
        self.language = tk.StringVar()
        self.language.set('Русский')

    #описание виджета смены языка
    def create_widgets(self):
        self.var1Entry = ttk.Entry(self, textvariable=self.var1)
        self.Button = ttk.Button(self, text=self.localizations[self.language.get()][0])
        self.var1Label = ttk.Label(self, text=self.localizations[self.language.get()][1])
        self.var2Entry = ttk.Entry(self, textvariable=self.var2, state='readonly')
        self.var2Label = ttk.Label(self, text=self.localizations[self.language.get()][2])
        self.var3Entry = ttk.Entry(self, textvariable=self.var3)
        self.var3Label = ttk.Label(self, text=self.localizations[self.language.get()][5])
        self.radiobuttonRussian = ttk.Radiobutton(self, text='Русский', variable=self.language,
                                                  command=self.ChangeLanguage, value='Русский')
        self.radiobuttonEnglish = ttk.Radiobutton(self, text='English', variable=self.language,
                                                  command=self.ChangeLanguage, value='English')
        self.radiobuttonUkrainian = ttk.Radiobutton(self, text='Український', variable=self.language,
                                                  command=self.ChangeLanguage, value='Український')
        self.InfoButton = ttk.Button(self, text=self.localizations[self.language.get()][3])

    #описание интерфейса
    def create_layout(self):
        self.var1Label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.var1Entry.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.var2Label.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.var2Entry.grid(row=2, column=1, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.var3Label.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.var3Entry.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.radiobuttonRussian.grid(row=0, column=2, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.radiobuttonEnglish.grid(row=0, column=3, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.radiobuttonUkrainian.grid(row=0, column=4, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.Button.grid(row=1, column=2, columnspan=2, rowspan=2, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.InfoButton.grid(row=1, column=4, columnspan=1, rowspan=2, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

    #процедура вычисления корня
    def calculate(self, event):
        try:
            flag = False
            a = Decimal(self.var1.get())
            if a < 0:
                flag = True
                a = abs(a)
            val1 = Decimal(a)
            getcontext().prec = int(self.var3.get()) + len(str(int(a**Decimal('0.5'))))
            if flag:
                self.var2.set(str((val1 ** Decimal('0.5')).quantize(Decimal(str(10**(-int(self.var3.get())))))) + 'i')
            else:
                self.var2.set(str((val1 ** Decimal('0.5')).quantize(Decimal(str(10**(-int(self.var3.get())))))))
        except:
            self.var2.set(self.localizations[self.language.get()][7])

    #функция вызова меню о программе
    def ShowInfo(self, event):
        messagebox.showinfo(title=self.localizations[self.language.get()][3],message=self.localizations[self.language.get()][4])

    #функция смены языка
    def ChangeLanguage(self):
        self.Button.config(text=self.localizations[self.language.get()][0])
        self.var1Label.config(text=self.localizations[self.language.get()][1])
        self.var2Label.config(text=self.localizations[self.language.get()][2])
        self.var3Label.config(text=self.localizations[self.language.get()][5])
        self.InfoButton.config(text=self.localizations[self.language.get()][3])

    #бинд клавиш
    def bind_buttons(self):
        self.Button.bind('<Button-1>', self.calculate)
        self.InfoButton.bind('<Button-1>', self.ShowInfo)

#основная процедура
def main():
    root = tk.Tk()
    Window(root)
    root.title('Calculamber')
    root.minsize(width=530, height=70)
    root.mainloop()

#вызов основной процедуры
main()
