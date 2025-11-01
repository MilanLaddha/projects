import turtle
import random
import time

# --- Game Setup ---

# Screen setup
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.title("Snake in a Box by Gemini")
wn.tracer(0)  # Turns off screen updates for manual control

# Game variables
delay = 0.1  # Controls game speed (lower is faster)
score = 0
high_score = 0

# --- Snake Head ---
head = turtle.Turtle()
head.speed(0)  # Animation speed (fastest)
head.shape("circle")
head.color("green")
head.penup()  # Don't draw when moving
head.goto(0, 0)
head.direction = "stop" # Initial direction

# --- Snake Food ---
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100) # Initial food position

# --- Snake Body Segments ---
segments = []

# --- Scoreboard ---
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle() # Don't show the turtle used for writing
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# --- Functions ---

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20) # Move by 20 pixels (size of square)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def reset_game():
    global score, delay
    time.sleep(1) # Pause for a second on game over
    head.goto(0, 0)
    head.direction = "stop"

    # Hide the segments
    for segment in segments:
        segment.clear() # Clear the drawing
        segment.hideturtle()
    segments.clear() # Remove all segments from the list

    # Reset score and delay
    score = 0
    delay = 0.1
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))
    wn.update() # Update the screen to show the cleared segments and updated score

# --- Keyboard Bindings ---
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# --- Main Game Loop ---
while True:
    wn.update() # Update the screen

    # Check for collision with border (the "box")
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset_game()

    # Check for collision with food
    if head.distance(food) < 20: # Distance is less than a square's side
        # Move the food to a random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey") # Body color
        new_segment.penup()
        segments.append(new_segment)

        # Increase score
        score += 10

        # Speed up the game (optional, but makes it harder)
        if delay > 0.05: # Don't go too fast
            delay -= 0.001

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20: # If head collides with any segment
            reset_game()

    time.sleep(delay) # Control the game speed

wn.mainloop() # Keeps the window open