import tkinter
from tkinter import ttk
from graphics import x, low, middle, high
from graphics import tmprt_diff_high, tmprt_diff_low, tmprt_diff_middle
import  matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from fuzzy_logic import Q, temp_difference_high, temp_is_high
from fuzzy_logic import temp_difference_middle, temp_is_optional
from fuzzy_logic import temp_difference_low, temp_is_low


def fuzzy_membership():
    fuzzy_membership_temperature()
    fuzzy_membership_temperature_difference()
    get_power_destribution(data)

def get_power_destribution(arguments):
    start = arguments['current_temperature']
    end = arguments['final_temperature']
    optimal_power = Q(arguments)
    power = optimal_power
    power_distrb = []
    for current in range(start, end-1, -1):
        if temp_difference_high(current, end) and temp_is_high(current):
            power += optimal_power * 0.15
        elif temp_difference_middle(current, end) and temp_is_high(current):
            power += optimal_power * 0.15
        elif temp_difference_middle(current, end) and temp_is_optional(current):
            power = optimal_power
        elif  temp_difference_low and temp_is_high(current):
            power = optimal_power
        elif temp_difference_low and temp_is_optional(current):
            power -= optimal_power * 0.05
        elif temp_difference_low and temp_is_low:
            power -= optimal_power * 0.05
        power_distrb.append(power)
    x = [i for i in range(start, end-1, -1)]
    fig3 = plt.figure(figsize=(5, 3))
    canvas3 = FigureCanvasTkAgg(fig3, root)
    ax = plt.axes()
    plt.xlabel('температура, t')
    plt.ylabel('потужність роботи конденсатора, кВт')

    ax.plot(x, power_distrb)
    canvas3.draw()
    canvas3.get_tk_widget().place(y=300, x=275)

def fuzzy_membership_temperature():
    fig1 = plt.figure(figsize=(5, 3))
    canvas1 = FigureCanvasTkAgg(fig1, root)
    ax = plt.axes()
    ax.plot(x, middle, '-o', label='middle')
    ax.plot(x, low, '--', label='low')
    ax.plot(x, high, '-x', label='high')
    plt.legend()
    plt.title('Fuzzy temperature membership function')
    canvas1.draw()
    canvas1.get_tk_widget().place(x=800, y=25)

def fuzzy_membership_temperature_difference():
    fig2 = plt.figure(figsize=(5, 3))
    canvas2 = FigureCanvasTkAgg(fig2, root)
    ax = plt.axes()
    X = [i for i in range(11)]
    ax.plot(X, tmprt_diff_middle, '-o', label='middle')
    ax.plot(X, tmprt_diff_low, '--', label='low')
    ax.plot(X, tmprt_diff_high, '-x', label='high')
    plt.legend()
    plt.title('Fuzzy temperatures difference membership function')
    canvas2.draw()
    canvas2.get_tk_widget().place(x=800, y=350)

root = tkinter.Tk()
area_label = tkinter.Label(root, text="Площа приміщення: ")
area_label.place(x=25, y=25)
ceiling_label = tkinter.Label(root, text="Висота потолка: ")
ceiling_label.place(x=25, y=55)
insolation_label = tkinter.Label(root, text="Інсоляція (освітлення сонцем): ")
insolation_label.place(x=25, y=85)
number_of_people_label = tkinter.Label(root, text="Кількість людей: ")
number_of_people_label.place(x=25, y=115)
number_of_computers_label = tkinter.Label(root, text="Кількість комп'ютерів: ")
number_of_computers_label.place(x=25, y=145)
number_of_people = tkinter.IntVar()
number_of_people.set(1)
number_of_people_entry = tkinter.Entry(root, textvariable=number_of_people)
number_of_people_entry.place(x=200, y=115, width=45)
number_of_computers = tkinter.IntVar()
number_of_computers.set(2)
number_of_computers_entry = tkinter.Entry(root, textvariable=number_of_computers)
number_of_computers_entry.place(x=200, y=145, width=45)
insolation_inbox = ttk.Combobox(root, values=['Слабка', 'Середня', 'Сильна'])
insolation_inbox.place(x=200, y=85, width=75)
insolation_inbox.current(1)
area = tkinter.DoubleVar()
area.set(20.0)
area_entry = tkinter.Entry(root, textvariable=area)
area_entry.place(width=30, x=200, y=25)
ceiling = tkinter.DoubleVar()
ceiling.set(2.5)
ceiling_entry = tkinter.Entry(root, textvariable=ceiling)
ceiling_entry.place(y=55, x=200, width=30)

is_highest_floor = tkinter.BooleanVar()
is_highest_floor_checkbutton = tkinter.Checkbutton(root, variable=is_highest_floor,
                                                    onvalue=1, offvalue=0)
is_highest_floor_checkbutton.place(x=200, y=175)
is_highest_floor_label = tkinter.Label(root, text="Верхній поверх: ")
is_highest_floor_label.place(x=25, y=175)

glazing_area_label = tkinter.Label(root, text='Площа скління: ')
glazing_area_label.place(x=25, y=235)
glazing_area = tkinter.DoubleVar()
glazing_area.set(2.0)
glazing_area_entry = tkinter.Entry(root, textvariable=glazing_area)
glazing_area_entry.place(x=200, y=235, width=45)

current_temperature = tkinter.IntVar()
current_temperature_label = tkinter.Label(root, text='Поточна температура повітря: ')
current_temperature_label.place(x=25, y=270)
current_temperature_entry = tkinter.Entry(root, textvariable=current_temperature)
current_temperature_entry.place(x=200, y=270, width=40)
current_temperature.set(23)

final_temperature = tkinter.IntVar()
final_temperature.set(19)
final_temperature_label = tkinter.Label(root, text="Кінцева температура повітря: ")
final_temperature_label.place(x=25, y=300)

final_temperature_entry = tkinter.Entry(root, textvariable=final_temperature)
final_temperature_entry.place(x=200, y=300, width=40)

button = tkinter.Button(root, text='OK', command=fuzzy_membership)
button.place(x=100, y=350)

data = {'area': area.get(),
        'ceiling': ceiling.get(),
        'insolation': insolation_inbox.get(),
        'number_of_people': number_of_people.get(),
        'number_of_computers': number_of_computers.get(),
        'is_highest_floor': is_highest_floor.get(),
        'glazing_area': glazing_area.get(),
        'current_temperature': current_temperature.get(),
        'final_temperature': final_temperature.get()
        }

root.geometry("1000x500")
root.title('Fuzzy logic')
root.mainloop()
