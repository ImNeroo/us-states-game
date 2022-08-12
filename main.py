import turtle
import pandas

# Create a screen in turtle that shows the U.S. Map
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
correct_guesses = []


# TODO: Use a loop to allow the user to keep guessing

while len(correct_guesses) < 50:
    # TODO: Convert the guess to Title case
    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's name?").title()
    # TODO: Check if the guess is among the 50 states
    if answer_state == "Exit":
        break
    if answer_state in state_list:
        # TODO: Keep track of the score
        score += 1
        # TODO: Write correct guesses onto the map
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        state = data[data.state == answer_state]
        new_turtle.goto(x=int(state.x), y=int(state.y))
        new_turtle.write(f"{answer_state}", align="center")
# TODO: Record the correct guesses in a list
        correct_guesses.append(answer_state)

states_learn = {"state": []}
# states_to_learn.csv
for state in state_list:
    if state not in correct_guesses:
        states_learn["state"].append(state)
df = pandas.DataFrame(states_learn)
df.to_csv("states_to_learn.csv")
