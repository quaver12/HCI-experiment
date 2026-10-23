import PySimpleGUI as sg
import random

#sg.theme('BluePurple')

#generate a random number 0-100
#display that as a bar
#user input 'guess what % of bar filled?'
#store result
#repeat 10? times


layout = [
    [sg.Text('Guess the percentage the bar is filled:')],
    [sg.Input(key='-IN-')],
    [sg.Button('Start'), sg.Button('Exit')],
    [sg.ProgressBar(100,key='-PROGRESS-BAR-',size=(50,50))]
]

window = sg.Window('Introduction', layout)
window.finalize()

while True:
    num = random.randrange(0,100,1) # generate random number 0-100 inclusive
    window['-PROGRESS-BAR-'].update(current_count=num)

    event, values = window.read()

    if event in (None, 'Exit'):
        break

    if event == 'Start':
        print(values['-IN-'],' ',num)

window.close()
