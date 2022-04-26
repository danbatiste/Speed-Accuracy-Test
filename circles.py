import pygame as pg
import time
import random as rand
import pandas as pd
import numpy as np

# Experiment paremeters
window_x = 720
window_y = 480
circle_radius_range = [10, 100]
experiment_allotted_time = 2 # seconds

computer_no = 1
dpi_setting = 1 # 0, 1, 2
experiment_id = f"comp{computer_no}_{int(time.time())}"



# Initialize starting variables
black = pg.Color(0, 0, 0)
white = pg.Color(255, 255, 255)
green = pg.Color(0, 255, 0)

bgcolor = black
circle_color = white


# Start simulation
pg.init()

pg.display.set_caption('Click Test')
game_window = pg.display.set_mode((window_x, window_y))
fps = pg.time.Clock()

def stop_experiment():
    game_window.fill(black)
    font = pg.font.SysFont('times new roman', 50)
    stop_experiment_surface = font.render("Time is up!", True, green)
    stop_experiment_rect = stop_experiment_surface.get_rect()
    stop_experiment_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(stop_experiment_surface, stop_experiment_rect)
    pg.display.flip()
    time.sleep(2)
    #pg.quit()
    #quit()

def start_screen():
    font = pg.font.SysFont('times new roman', 50)
    stop_experiment_surface = font.render("Click anywhere to start!", True, green)
    stop_experiment_rect = stop_experiment_surface.get_rect()
    stop_experiment_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(stop_experiment_surface, stop_experiment_rect)
    pg.display.flip()

# Initialize experiment data collection
experiment_df_columns = [
    # Circle data
    "circle_x",
    "circle_y",
    "circle_radius",

    # Click data
    "click_x",
    "click_y",
    "time_clicked",
    "click_distance_from_circle_center",
    "click_success",

    # Experiment data
    "computer_no",
    "dpi_setting",
    "experiment_id",

]
experiment_results = []

# Start screen loop (runs til user clicks for first time)
user_clicked = False
user_released_click = False
start_screen()
while not (user_clicked and user_released_click):
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[0]:
            try:
                user_clicked = True
            except:
                pass
        if event.type == pg.MOUSEBUTTONUP:
            try:
                user_released_click = True
            except:
                pass


# Start experiment
experiment_start_time = time.time()
while True:
    # At end of experiment (after time runs out)
    if time.time() - experiment_start_time >= experiment_allotted_time:
        stop_experiment()
        experiment_df = pd.DataFrame(experiment_results, columns=experiment_df_columns)
        experiment_df.to_csv(f"experiments/{experiment_id}.csv")
        pg.quit()
        break

    # On user click:
    if user_clicked:
        circle_radius = rand.randrange(*circle_radius_range)
        circle_position = [rand.randrange(circle_radius, (window_x - circle_radius))//1,
                            rand.randrange(circle_radius, (window_y - circle_radius))//1]
        game_window.fill(bgcolor)
        pg.draw.circle(game_window, circle_color, circle_position, circle_radius, circle_radius)
        pg.display.update()
        fps.tick(10)
        user_released_click = False
        user_clicked = False

    # Check if user clicked; if so update dataframe and go to next circle
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[0] and user_released_click:
            try:
                user_clicked = True

                # Enter data from circle click into experiment results for this experiment
                mouse_pos = pg.mouse.get_pos()
                click_distance_from_circle_center = np.sqrt(
                    (circle_position[0] - mouse_pos[0])**2 +\
                    (circle_position[1] - mouse_pos[1])**2
                )
                experiment_results_entry = [
                    # Circle data
                    circle_position[0],
                    circle_position[1],
                    circle_radius,

                    # Click data
                    mouse_pos[0],
                    mouse_pos[1],
                    time.time() - experiment_start_time,
                    click_distance_from_circle_center,
                    click_distance_from_circle_center <= circle_radius,

                    # Experiment data
                    computer_no,
                    dpi_setting,
                    experiment_id,
                ]
                experiment_results.append(experiment_results_entry)
            except:
                pass
        elif event.type == pg.MOUSEBUTTONUP:
            user_released_click = True
            user_clicked = False
        else:
            user_clicked = False

# Start the survey now
from survey import *
start_survey(window_x, window_y, experiment_id)
quit()
