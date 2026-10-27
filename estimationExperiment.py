import PySimpleGUI as sg
import random
import csv

#small experiment, testing user's ability to estimate the value of UI elements (percentage bar), depending on the size of the element

#settings
outputfile = 'data.csv'
sets = 5 # how many different sizes of bar
reps = 10 # how guesses per bar size

layout = [
    [sg.Text('Guess what percentage the bottom bar is filled  -  '),sg.Text('',key='-ATTEMPT-TEXT-')],
    [sg.Input(key='-IN-')],
    [sg.Button('Enter', bind_return_key = True), sg.Button('Skip to next bar size'), sg.Text('Guessed value: x',key ='-GUESS-'), sg.Text('Real Value: x',key ='-VALUE-')],
    [sg.ProgressBar(100,key='-PROGRESS-BAR-',size=(30,30))]
]

data = [[[None for x in range (3)] for y in range(reps)] for z in range(sets)]
window = sg.Window('UI Estimation Experiment', layout)
window.finalize()

for i in range (sets-1,-1,-1):

    barsize = (2**(i))*40

    window['-PROGRESS-BAR-'].set_size(size = (None,barsize))
    for j in range(0,reps):

        window['-ATTEMPT-TEXT-'].update(f'Attempt no. {j+1}, bar size: 2^{i}')
        window['-IN-'].update(value='%',move_cursor_to=0)
        num = random.randrange(0,100,1) # generate random number 0-100 inclusive
        window['-PROGRESS-BAR-'].update(current_count=num)

        event, values = window.read()

        if event in (None, 'Skip to next bar size'):
            break

        if event == 'Enter':

            data[i][j][0]=f'2^{i}'
            data[i][j][1]=values['-IN-'][:-1]# save user guess
            data[i][j][2]=num                # save actual val
            window['-IN-'].update()
            window['-GUESS-'].update(f"Guessed value: {data[i][j][1]}")
            window['-VALUE-'].update(f"Real value: {data[i][j][2]}")
            #print(data[i][j][0],data[i][j][1])

# write data to csv file
with open(outputfile, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)                                                 # Create writer object
    csvwriter.writerow(['Bar size (relative)','User Guess (%)','Actual Value (%)'])   # write header
    for i in range (sets):                                                          # write data
        csvwriter.writerows(data[i])

print("written to",outputfile)
window.close()

