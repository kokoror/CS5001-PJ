import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('US State Game')
image = 'blank_states_img.gif' # note turtle only accepts gif format
# add new shape
screen.addshape(image)
# after adding shape, you can use this shape in turtle
turtle.shape(image)

# the below code gets the coordinate of the click on the screen
# def add_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(add_mouse_click_coor)

# read csv file
data = pd.read_csv("50_states.csv", index_col='state')
# print(data.head())
states = data.index.to_list()
guessed_states = []
while len(guessed_states) < len(states):

    answer = screen.textinput(title=f'{len(guessed_states)}/50 right',
                              prompt="What's the next state's name?", ).title()
    if answer == 'Exit':
        break

    if answer in states and answer not in guessed_states:
        guessed_states.append(answer)
        x_cor = data.loc[answer, 'x']
        y_cor = data.loc[answer, 'y']
        # print(x_cor, y_cor)
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.goto(x_cor, y_cor)
        new_turtle.write(answer, align='center', font=('Arial', 12, 'normal'))


not_guessed_states = list(set(states) - set(guessed_states))
print(not_guessed_states)
not_guessed_data = data.loc[not_guessed_states]
not_guessed_data.to_csv("not_guessed_data.csv")

# screen.mainloop() keeps the screen open

# screen.exitonclick()
