import turtle

# Create a Turtle screen
window = turtle.Screen()

# Create a Turtle object
t = turtle.Turtle()

# Draw a square
for i in range(4):  # Loop 4 times to draw all sides of the square
    t.forward(100)  # Move forward by 100 units
    t.right(90)     # Turn right by 90 degrees

# Close the window when clicked
window.exitonclick()