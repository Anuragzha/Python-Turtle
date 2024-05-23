import turtle

def draw_heart():
    turtle.color("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

def display_quote(quote):
    turtle.penup()
    turtle.goto(0, -180)
    turtle.color("black")
    turtle.write(quote, align="center", font=("Arial", 14, "normal"))

if __name__ == "__main__":
    turtle.speed(2)
    draw_heart()
    valentine_quote = "You are the reason for my happiness🤣🤣. Happy Valentines Day! in Advance"
    display_quote(valentine_quote)
    turtle.hideturtle()
    turtle.done()
