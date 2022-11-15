from turtle import Turtle, Screen
import random
screen = Screen()
screen.getcanvas()
screen.colormode(255)
COORDINATES = [(0,0), (-20, 0), (-40, 0)]
UNITS_MOVED = 20
class Snake():
	def __init__(self):
		self.squares = []
		self.create()
		self.head = self.squares[0]


	def create(self):
		for i in COORDINATES:
			new_squares = Turtle()
			new_squares.penup()
			new_squares.shape("square")
			new_squares.goto(i)
			new_squares.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
			self.squares.append(new_squares)

	def grow_longer(self):
		new_seg = Turtle()
		new_seg.penup()
		new_seg.shape("square")
		new_seg.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
		if self.head.heading() == 90 :
			self.x = self.squares[len(self.squares)-1].xcor()
			self.y = self.squares[len(self.squares)-1].ycor() - 20
			new_seg.setpos(self.x, self.y)
		elif self.head.heading() == 270:
			self.x = self.squares[len(self.squares)-1].xcor()
			self.y = self.squares[len(self.squares)-1].ycor() + 20
			new_seg.setpos(self.x, self.y)
		elif self.head.heading() == 0:
			self.y = self.squares[len(self.squares) - 1].ycor()
			self.x = self.squares[len(self.squares)-1].xcor() - 20
			new_seg.setpos(self.x,self.y)
		else:
			self.y = self.squares[len(self.squares) - 1].ycor()
			self.x = self.squares[len(self.squares)-1].xcor() +20
			new_seg.goto(self.x, self.y)
		self.squares.append(new_seg)

	def move(self):
		for ind in range(len(self.squares)-1, 0, -1):
			self.squares[ind].goto(self.squares[ind-1].pos())
		self.squares[0].forward(UNITS_MOVED)
	def turn_left(self):
		if self.head.heading() == 270:
			self.head.right(90)
		elif self.head.heading() == 90:
			self.squares[0].left(90)
		else:
			pass
	def turn_right(self):
		if self.head.heading() == 270:
			self.head.left(90)
		elif self.head.heading() == 90:
			self.squares[0].right(90)
		else:
			pass
	def down(self):
		if self.head.heading() == 0:
			self.head.right(90)
		elif self.head.heading()== 180:
			self.head.left(90)
		else:
			pass
	def up(self):
		if self.head.heading()==0:
			self.head.left(90)
		elif self.head.heading()==180:
			self.head.right(90)
		else:
			pass

class Food(Turtle):
	def __init__(self):
		super().__init__()
		self.food_xcoor = random.randint(-280, 280)
		self.food_ycoor = random.randint(-280, 280)

		
	def create_food(self, shape, color):
		self.shape(shape)
		self.color(color)
		self.penup()
		self.shapesize(1, 1)
		self.goto(self.food_xcoor, self.food_ycoor)
	def move_away(self):
		self.newx = random.randint(-280, 280)
		self.newy = random.randint(-280, 280)
		self.goto(self.newx, self.newy)
	def write_word(self, word):
		self.write(word, False, align = "center", font = ("Arial", 15, "normal"))

class Obstacle(Turtle):
	def __init__(self):
		super().__init__()
		self.xcoor = random.randint(-300,300)
		self.ycoor = random.randint(-300, 300)
		self.x_move = 10
		self.y_move = 10
		self.penup()
		self.shape("circle")
		self.shapesize(1, 1, 15)
		self.color("green")
	def create(self):
		self.goto(self.xcoor,self.ycoor)
	def move_around(self):
		self.newx2 = self.xcor() + self.x_move
		self.newy2 = self.ycor() + self.y_move
		self.goto(self.newx2, self.newy2)
	def bounce1(self):
		self.x_move *= -1
	def bounce2(self):
		self.y_move *= -1
class ConstantObstacle(Obstacle):
	def __init__(self):
		super().__init__()
		self.color("white")
		self.shape("square")
		self.shapesize(1,1, 12)

class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.point = 0
		self.lives = 3
		with open("highscore.txt") as high_score:
			self.high = int(high_score.read())
		self.penup()
		self.color("white")
		self.goto(0,370)
		self.update()
		self.hideturtle()

	def update(self):
		self.clear()
		self.write(f"Right answer: {self.point}   Lives: {self.lives}   Best right answer: {self.high}", False, "center", font=("Arial", 15, "normal"))

	def refresh(self):
		self.point += 1
		self.clear()
		self.update()
	def refresh2(self):
		self.lives -= 1
		self.clear()
		self.update()

	def reset(self):
		if self.point > self.high:
			self.high = self.point 
			with open("highscore.txt", mode = "w") as high_score:
				high_score.write(f"{self.high}")

	def game_over(self):
		self.reset()
		self.update()

class Display(Turtle):
	def __init__(self):
		super().__init__()
		self.color("white")
		self.penup()
		self.hideturtle()
	def write_def(self, defs):
		self.goto(0, 350)
		self.write(defs, False, "center", font = ("Arial", 15, "normal"))