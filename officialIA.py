import os
import random
vocab = [] #2D array
definitions = []
right_choice = 0
appear = 0
game_is_on = False

os.system("cls")

print("Enter session name, date and time for progress tracking")

name = input()
date = input()
Time = input()

os.system("cls")

print("Enter words and their definitions for the game")

while True:
	words = input()
	if words != "done":
		defs = input()
		vocab.append([words, 0, 0, 0]) # [[word, wrong, right, frequency]]
		definitions.append(defs)
	else:
		game_is_on = True  
		os.system("cls")
		break
		
from turtle import Turtle, Screen
from snakeclasses import Snake, Food, ScoreBoard, Obstacle, ConstantObstacle, Display
import time



speed = 0.1
s = Screen()
s.setup(width = 800, height = 800)
s.bgcolor("black")
s.title("IB Computer Science IA")
s.tracer(0)
s.listen()

index = random.randint(0, len(definitions) - 1)
d = Display()
d.write_def(definitions[index])
noah = Snake()

#food creation
foods = []

food1 = Food()
food1.create_food("circle", "red")
food1.color("white")
food1.shapesize(0.3, 0.3)

food2 = Food()
food2.create_food("circle", "blue")
food2.color("white")
food2.shapesize(0.3, 0.3)

food3 = Food()
food3.create_food("circle", "green")
food3.color("white")
food3.shapesize(0.3, 0.3)

foods.append(food1)
foods.append(food2)
foods.append(food3)

right_food = random.choice(foods)
right_food.write_word(vocab[index][0])
vocab[index][3] +=1
max_appear = 1
appear += 1

temp = vocab[index]
vocab.remove(vocab[index])

for fo in foods:
	if fo == right_food:
		continue
	else:
		wrong = random.choice(vocab)
		fo.write_word(wrong[0])

vocab.insert(index, temp)

scoreboard = ScoreBoard()

obstacle_moving = []
standing_obstacle = []

s.onkey(noah.turn_right, "d")
s.onkey(noah.turn_left, "a")
s.onkey(noah.up, "w")
s.onkey(noah.down, "s")
 
#the main loop
while game_is_on:
	s.update()
	
	time.sleep(speed)
	noah.move()

	
#colliding with right foods 
	if noah.head.distance(right_food) < 15 :
		food1.move_away()
		food2.move_away()
		food3.move_away()
		
		right_choice += 1
		noah.grow_longer()

		scoreboard.refresh()
		
		
		temp[2] += 1

		new_def = random.choice(definitions)
		new_index = definitions.index(new_def)
		d.clear()
		d.write_def(new_def)

		for fo in foods:
			fo.clear()
		right_food_2 = random.choice(foods)
		right_food_2.write_word(vocab[new_index][0])
		vocab[new_index][3] += 1
		appear += 1
		right_food = right_food_2
		

		temp = vocab[new_index]
		vocab.remove(vocab[new_index])

		for fo in foods:
			if fo == right_food:
				continue
			else:
				wrong = random.choice(vocab)
				fo.write_word(wrong[0])
		vocab.insert(new_index, temp)

#detecting collision with wrong words
	for f in foods:
		if f != right_food and noah.head.distance(f) < 12:

			speed = speed - 0.005

			scoreboard.refresh2()

			obs = Obstacle()
			obs.create()
			obstacle_moving.append(obs)
			obs2 = ConstantObstacle()
			obs2.create()
			standing_obstacle.append(obs2)

			food1.move_away()
			food2.move_away()
			food3.move_away()

			new_def = random.choice(definitions)
			new_index = definitions.index(new_def)
			d.clear()
			d.write_def(new_def)

			for fo in foods:
				fo.clear()
			temp[1] += 1
			right_food_2 = random.choice(foods)
			right_food_2.write_word(vocab[new_index][0])
			vocab[new_index][3] += 1
			appear += 1
			right_food = right_food_2
		
			temp = vocab[new_index]
			vocab.remove(vocab[new_index])

			for fo in foods:
				if fo == right_food:
					continue
				else:
					wrong = random.choice(vocab)
					fo.write_word(wrong[0])
			vocab.insert(new_index, temp)




#moving the black obstacles around
	for o in obstacle_moving:
		o.move_around()
		if o.ycor() > 380 or o.ycor() < -380:
			o.bounce2()
		if o.xcor() > 380 or o.xcor() < -380:
			o.bounce1()

#colliding with black obstacles
	for j in obstacle_moving:
		if noah.head.distance(j) < 15:
			scoreboard.refresh2()

#colliding with white obstacle
	for l in standing_obstacle:
		if noah.head.distance(l) < 20 and scoreboard.lives :
			scoreboard.refresh2()
		
#detecting collision with the walls
	if noah.head.xcor() > 390 or noah.head.xcor()< -390 or noah.head.ycor()>390 or noah.head.ycor()<-390:
		game_is_on = False
		scoreboard.game_over()

#detecting collision with the snake body
	for i in noah.squares:
		if i == noah.head:
			pass
		else:
			if noah.head.distance(i) < 10:
				scoreboard.refresh2()

#running out of lives
	if scoreboard.lives == 0:
		game_is_on = False
		scoreboard.game_over()

s.exitonclick()

#sort the data using reverse bubble sort
for i in range(len(vocab)):
	for j in range(len(vocab) - i -1):
		if vocab[j][2] < vocab[j+1][2]:
			vocab[j], vocab[j+1] = vocab[j+1], vocab[j]

#processing data after finishing the game

import pandas as pd
print(pd.DataFrame(vocab, columns = ["Word/questions", "Wrong", "Right", "Appearance"]))


#store the history of playing

with open("history.txt", mode = "a") as h:
	h.write(name)
	h.write("\n")

	h.write(date)
	h.write("\n")

	h.write(Time)
	h.write("\n")

	h.write(f"Your score in {name} session was {right_choice / appear * 10} /10 \n")

	h.write("\n")
	h.write("\n")

print("DO YOU WANNA SEE YOUR HISTORY?")
ask = input()
if ask == "YES":
	os.system("cls")
	with open("history.txt") as s:
		print(s.read())
