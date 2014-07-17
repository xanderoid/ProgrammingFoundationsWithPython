import turtle

def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.fd(100)
		some_turtle.rt(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")

	jack = turtle.Turtle()
	jack.shape("turtle")
	jack.color("green")
	jack.speed(10)

	for i in range (1,37):
		draw_square(jack)
		jack.right(10)

	# jill = turtle.Turtle()
	# jill.shape("circle")
	# jill.color("yellow")
	# jill.speed(1)

	# jill.circle(100)

	# junior = turtle.Turtle()
	# junior.shape("triangle")
	# junior.color("black")
	# junior.speed(1)

	# i = 0
	# while (i<3):
	# 	junior.fd(100)
	# 	junior.rt(120)
	# 	i += 1

	window.exitonclick()

draw_art()