from tkinter import *
from tkinter import ttk


import tkinter as tk
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор калорий и БМР")
        # Создаем поля для ввода значений
        self.label_weight = tk.Label(master, text="Вес (кг):")
        self.label_weight.grid(row=0, column=0)
        self.entry_weight = tk.Entry(master)
        self.entry_weight.grid(row=0, column=1)
        self.label_height = tk.Label(master, text="Рост (см):")
        self.label_height.grid(row=1, column=0)
        self.entry_height = tk.Entry(master)
        self.entry_height.grid(row=1, column=1)
        self.label_age = tk.Label(master, text="Возраст:")
        self.label_age.grid(row=2, column=0)
        self.entry_age = tk.Entry(master)
        self.entry_age.grid(row=2, column=1)
        self.label_gender = tk.Label(master, text="Пол:")
        self.label_gender.grid(row=3, column=0)
        self.var_gender = tk.StringVar(value="male")
        self.radiobutton_male = tk.Radiobutton(master, text="Мужской", variable=self.var_gender, value="male")
        self.radiobutton_male.grid(row=3, column=1)
        self.radiobutton_female = tk.Radiobutton(master, text="Женский", variable=self.var_gender, value="female")
        self.radiobutton_female.grid(row=3, column=2)
        self.label_activity = tk.Label(master, text="Активность:")
        self.label_activity.grid(row=4, column=0)
        self.var_activity = tk.StringVar(value="low")
        self.radiobutton_low = tk.Radiobutton(master, text="Низкая", variable=self.var_activity, value="low")
        self.radiobutton_low.grid(row=4, column=1)
        self.radiobutton_medium = tk.Radiobutton(master, text="Средняя", variable=self.var_activity, value="medium")
        self.radiobutton_medium.grid(row=4, column=2)
        self.radiobutton_high = tk.Radiobutton(master, text="Высокая", variable=self.var_activity, value="high")
        self.radiobutton_high.grid(row=4, column=3)
        # Создаем кнопку для расчета
        self.button_calculate = tk.Button(master, text="Рассчитать", command=self.calculate)
        self.button_calculate.grid(row=5, column=1)
        # Создаем поля для вывода результатов
        self.label_bmr = tk.Label(master, text="Базовый метаболизм:")
        self.label_bmr.grid(row=6, column=0)
        self.entry_bmr = tk.Entry(master, state="readonly")
        self.entry_bmr.grid(row=6, column=1)
        self.label_calories = tk.Label(master, text="Калории:")
        self.label_calories.grid(row=7, column=0)
        self.entry_calories = tk.Entry(master, state="readonly")
        self.entry_calories.grid(row=7, column=1)
    def calculate(self):
        # Получаем значения из полей ввода
        weight = float(self.entry_weight.get())
        height = float(self.entry_height.get())
        age = int(self.entry_age.get())
        gender = self.var_gender.get()
        activity = self.var_activity.get()
        # Рассчитываем БМР
        if gender == "male":
            bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
        else:
            bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
        # Учитываем уровень активности
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#Интерфейс к файлу python можно создать с помощью модуля tkinter. Например, если у нас есть файл с логикой, который принимает на вход два аргумента - число и степень, и выводит результат возведения числа в степень, то интерфейс к нему можно реализовать так:
#```python
import tkinter as tk
import main #имя нашего файла с логикой
#создаем класс для нашего интерфейса
class MyInterface:
    def __init__(self, master):
        self.master = master
        master.title("My Interface")
        #создаем поля для ввода числа и степени
        self.number_label = tk.Label(master, text="Number:")
        self.number_label.grid(row=0, column=0)
        self.number_entry = tk.Entry(master)
        self.number_entry.grid(row=0, column=1)
        self.power_label = tk.Label(master, text="Power:")
        self.power_label.grid(row=1, column=0)
        self.power_entry = tk.Entry(master)
        self.power_entry.grid(row=1, column=1)
        #создаем кнопку для вызова функции из нашего файла с логикой
        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=2, column=1)
        #создаем поле для вывода результата
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=3, column=1)
    #функция для вызова функции из нашего файла с логикой
    def calculate(self):
        number = float(self.number_entry.get())
        power = float(self.power_entry.get())
        result = my_module.power(number, power)
        self.result_label.config(text=result)
#создаем окно для нашего интерфейса
root = tk.Tk()
my_interface = MyInterface(root)
root.mainloop()
'''


у каждой функции по сути должен быть свой интерфейс, 
который исполняет функционал прописанный в main.py.



'''