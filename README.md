# Speed-Accuracy-Test

This GitHub repository is designed to help users test the optimal mouse DPI settings for speed and accuracy. It contains two files, `survey.py` and `mouse.py`, which are responsible for creating a survey and mouse test, respectively. The survey and mouse test are used to collect data on the user's preferences and mouse performance, which will be used to determine the optimal mouse DPI settings.

## Usage

The `survey.py` and `mouse.py` files can be used to create a survey and mouse test, respectively. To use the files, first import them into your project:

```python
from survey import start_survey
from mouse import start_mouse_test
```

Next, call the `start_survey` and `start_mouse_test` functions, which will set up the survey and mouse test windows and run the GUI. When the user clicks the submit button, the survey and mouse test responses will be stored in the `survey_response_data` and `mouse_response_data` variables, respectively.

For example:

```python
# Create the survey window and run the GUI
start_survey()

# Create the mouse test window and run the GUI
start_mouse_test()
```

Once the survey and mouse test are complete, the data can be used to determine the optimal mouse DPI settings for speed and accuracy.

The code collects data from the experiment, including circle data (position and radius), click data (mouse position, time, distance from the circle center, and whether or not the click was within the circle radius), and experiment data (computer number, DPI setting, and experiment ID). The data is stored in a dataframe and written to a CSV file.