import PySimpleGUI as sg
import random

#sg.theme('BluePurple')

#generate a random number 0-100
#display that as a bar
#user input 'guess what % of bar filled?'
#store result
#repeat 10? times

layout = [
    [sg.Text('',key='-TEXT-')],
    [sg.Input(key='-IN-')],
    [sg.Button('Enter', bind_return_key = True), sg.Button('Exit')],
    [sg.ProgressBar(100,key='-PROGRESS-BAR-',size=(50,50))]
]

window = sg.Window('Introduction', layout)
window.finalize()

for i in range(0,10):
    window['-TEXT-'].update(f'Guess the percentage that the bar is filled  -  Attempt no. {i}')
    window['-IN-'].update(value='%',move_cursor_to=0)
    num = random.randrange(0,100,1) # generate random number 0-100 inclusive
    window['-PROGRESS-BAR-'].update(current_count=num)

    event, values = window.read()

    if event in (None, 'Exit'):
        break

    if event == 'Enter':
        print(values['-IN-'][:-1],' ',num)
        window['-IN-'].update()

window.close()
