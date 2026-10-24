import PySimpleGUI as sg
import random
import csv

#small experiment, testing user's ability to estimate the value of UI elements (percentage bar), depending on the size of the element

#settings
outputfile = 'data.csv'
sets = 5 # how many different sizes of bar
reps = 10 # how guesses per bar size

layout = [
    [sg.Text('',key='-TEXT-')],
    [sg.Input(key='-IN-')],
    [sg.Button('Enter', bind_return_key = True), sg.Button('Exit')],
    [sg.ProgressBar(100,key='-PROGRESS-BAR-',size=(50,50))]
]

data = [[[None for x in range (2)] for y in range(reps+1)] for z in range(sets)]
window = sg.Window('UI Estimation Experiment', layout)
window.finalize()

for i in range (0,sets):
    data[i][0] = [f'(Bar size {i+1}) User Guess (%)', 'Actual Value (%)'] # add header
    for j in range(1,reps+1):

        window['-TEXT-'].update(f'Guess the percentage that the bar is filled  -  Attempt no. {j}, bar size: {i+1}')
        window['-IN-'].update(value='%',move_cursor_to=0)
        num = random.randrange(0,100,1) # generate random number 0-100 inclusive
        window['-PROGRESS-BAR-'].update(current_count=num)

        event, values = window.read()

        if event in (None, 'Exit'):
            break

        if event == 'Enter':
            data[i][j][0]=values['-IN-'][:-1]# save user guess
            data[i][j][1]=num                # save actual val
            window['-IN-'].update()
            print(data[i][j][0],data[i][j][1])

# write data to csv file
with open(outputfile, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)        # Create writer object
    for i in range (sets):
        csvwriter.writerows(data[i])              # Write multiple rows

print("written to",outputfile)
window.close()

