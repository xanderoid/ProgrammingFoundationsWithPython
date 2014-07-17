import turtle

def draw_shapes():
	window = turtle.Screen()
	window.bgcolor("red")

	jack = turtle.Turtle()
	jack.shape("turtle")
	jack.color("green")
	jack.speed(1)

	i = 0
	while (i<4):
		jack.fd(100)
		jack.rt(90)
		i += 1

	jill = turtle.Turtle()
	jill.shape("circle")
	jill.color("yellow")
	jill.speed(1)

	jill.circle(100)

	junior = turtle.Turtle()
	junior.shape("triangle")
	junior.color("black")
	junior.speed(1)

	i = 0
	while (i<3):
		junior.fd(100)
		junior.rt(120)
		i += 1

	window.exitonclick()

draw_shapes()