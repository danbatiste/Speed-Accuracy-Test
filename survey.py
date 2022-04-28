import pandas as pd
from tkinter import *


questions = {
    "How fast would you say your mouse/trackpad speed at home is?" : ("radio", ("slow", "medium", "fast")),
    "At home do you use a mouse or a trackpad?" : ("radio", "mouse trackpad other".split()),
    "How fast do you think you type?" : ("radio", ["below average", "average", "above average"]),
    "How many hours per week do you play videogames?" : ("text", None),
    "Sex" : ("radio", ("M", "F")),
}


def submit(survey_response_data, experiment_id):
    # Format the questions and responses
    questions = []
    responses = []
    for question, var in survey_response_data:
        questions.append(question)
        responses.append(var.get())
    # Put questions/responses into a dataframe and save it
    save_responses(
        pd.DataFrame({
        "Question" : questions,
        "Response" : responses
        }), experiment_id
    )


def save_responses(survey_response_df, experiment_id):
    # Save survey response dataframe as a csv
    survey_response_df.to_csv(f"experiments/{experiment_id}_survey.csv")


def start_survey(window_x, window_y, experiment_id, questions=questions):
    # Set up the window
    window = Tk()
    window.title("Anonymous survey")
    window.geometry(f"{window_x}x{window_y}")

    Label(window, text="(Optional) Anonymous Survey", font=20, pady=15).grid(row=1)

    # Set up all the questions
    survey_response_data = []
    text_variables = []
    text_idx = 0
    radio_variables = []
    radio_idx = 0
    for i, question_data in enumerate(questions.items(), start=2):
        question, question_type = question_data
        question_type, question_content = question_type

        # Set up text questions, store variables in text_variables and responses in survey_response_data
        Label(window, text=question, pady=5, width=50, justify='left', anchor='w').grid(row=i, sticky=W)

        if question_type == "text":
            text_variables.append(StringVar(window, ""))
            survey_response_data.append((question, text_variables[text_idx]))
            # Label(window, text=question, pady=10, width=60, justify='left', anchor='w').grid(row=i, sticky=W)
            Entry(window, textvariable=text_variables[text_idx]).grid(row=i, column=1, sticky=W)
            text_idx += 1
        
        # Set up radio questions, store variables in radio_variables and responses in survey_response_data
        if question_type == "radio":
            radio_variables.append(StringVar(window, str(question_content[0])))
            survey_response_data.append((question, radio_variables[radio_idx]))
            # Label(window, text=question, justify='left', anchor='w').grid(row=i)
            for j, option in enumerate(question_content):
                Radiobutton(window, text=option,
                           variable=radio_variables[radio_idx],
                           value=option, justify="left").grid(row=i, column=j+1, sticky=W)
            radio_idx += 1

    

    # Set up "submit" button
    button_width = 60
    button_height = 5
    submit_button = Button(window, text="Submit", width=button_width,
                           height=button_height, command=(lambda: [submit(survey_response_data, experiment_id), window.destroy()]),
                           bg="#88f088")
    submit_button.place(x=(window_x/2 - (button_width/2)*window_x/100), y=(window_y*0.55 - (button_height/2)*(window_y/100)))


    # Set up "opt out" button
    submit_button = Button(window, text="Opt out and exit survey", width=button_width,
                           height=button_height, command=(lambda: [submit(survey_response_data, experiment_id), window.destroy()]),
                           bg="#f08888")
    submit_button.place(x=(window_x/2 - (button_width/2)*window_x/100), y=(window_y*0.75 - (button_height/2)*(window_y/100)))

    # Run the gui
    window.mainloop()


    


if __name__ == "__main__":
    start_survey(720, 480, "test_experiment_survey")

