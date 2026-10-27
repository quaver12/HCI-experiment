# HCI-experiment
Basic HCI experiment, testing the accuracy of user estimation based on the size of UI elements.

Users are prompted to guess what percentage of a progress bar is filled up, with
different sizes of progress bars being displayed. Saves the result to a csv file.

Requires pySimpleGui:

```
pip install pySimpleGui
```

Or for use on uni computers:

```
python3 -m venv hci_env
source hci_env/bin/activate
pip install pysimplegui
```

Then run ```python3 estimationExperiment.py```


