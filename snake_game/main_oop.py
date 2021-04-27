from snake import Snake
from food import Food
from score_board import ScoreBoard
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Cute Snake')
screen.tracer(0)  # turn animation off, used with screen.update()


# then, move the snake, let it keep moving
continue_game = True
food = Food()
score_board = ScoreBoard()
new_snake = Snake()

while continue_game:
    # key binding has to be before set the snake to move in the while loop
    # the below functions in snake class, snake.up, snake.down, snake.left, snake.right
    # changes the heading of snake.segments[0]
    screen.onkey(new_snake.up, 'Up')
    screen.onkey(new_snake.down, 'Down')
    screen.onkey(new_snake.left, 'Left')
    screen.onkey(new_snake.right, 'Right')

    screen.listen()

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        new_snake.forward() # each segment moves forward by 1 distance

        # detect if snake collides with food, use distance method in snake. snake.distance(another_snake)
        if new_snake.head.distance(food) < 15:
            food.move()
            score_board.increase_score()
            new_snake.extend()
        # detect if snake collides with wall
        if new_snake.head.xcor() > 285 or new_snake.head.xcor() < -285 or new_snake.head.ycor() > 285 or new_snake.head.ycor() < -285:
            game_is_on = False

        for segment in new_snake.segments[1:]:
            if new_snake.head.distance(segment) < 15:
                game_is_on = False


    score_board.game_over()
    continue_game = screen.textinput('Continue?', f"You scored {score_board.score}. Do you want to start a new game? y/n.")
    score_board.reset_high_score()
    if continue_game == 'y':

        food.clear()
        new_snake.reset_snake()
    if continue_game == 'n':
        continue_game = False

screen.exitonclick()