import PySimpleGUI as sg
import random
import csv

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

sets = 5 # how many different sizes of bar
reps = 10 # how guesses per bar size

data = [[[None]*2]*(reps+1)]*sets

window = sg.Window('Introduction', layout)
window.finalize()

for i in range (0,sets):
    #data[0] = [f'Bar Size {i+1}'] # add header
    for j in range(1,reps+1):
        data[0][j] = ['User Guess (%)', 'Actual Value (%)'] # add header

        window['-TEXT-'].update(f'Guess the percentage that the bar is filled  -  Attempt no. {j}, bar size: {i+1}')
        window['-IN-'].update(value='%',move_cursor_to=0)
        num = random.randrange(0,100,1) # generate random number 0-100 inclusive
        window['-PROGRESS-BAR-'].update(current_count=num)

        event, values = window.read()

        if event in (None, 'Exit'):
            break

        if event == 'Enter':
            data[i][j][0]=['-IN-'][:-1]  # save user guess
            data[i][j][1]=num            # save actual val

            print(values['-IN-'][:-1],' ',num)
            window['-IN-'].update()

print(data)

window.close()
