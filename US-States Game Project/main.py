import turtle
import pandas
screen = turtle.Screen()
screen.title("US states Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data_file = pandas.read_csv("50_states.csv")
all_states = data_file.state.to_list()
guessed_states = []

# Create a single turtle for writing state names
state_turtle = turtle.Turtle()
state_turtle.hideturtle()
state_turtle.penup()

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(prompt="What's the another US state?:", title=f"{len(guessed_states)}/50 are correct").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [n for n in all_states if n not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_name = answer_state
        current_state = data_file[data_file["state"] == state_name]
        x_pos = current_state["x"].item()
        y_pos = current_state["y"].item()
        state_turtle.goto(x_pos, y_pos)
        state_turtle.write(state_name)



screen.exitonclick()