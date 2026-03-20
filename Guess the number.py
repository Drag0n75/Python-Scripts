import random

dudd = random.randint(1, 10)  # so dud its the correct number, 1 its the smallest and 10 the biggest
ans = 0 # the answer by fkin defalut, it will wont change anything but it needs to be something
while ans != dudd: # the loop for infinite guesses
	ans = int(input()) # sets da damn answer that you will give 
	if ans < dudd: # the first always should be if, and tje last one elif or else, i used elif
		print("its bigger") # wait its gonna do if number bigger 
	elif ans > dudd: # the elif its like an else but in else you cant do mucb things
			print("its smaller") # the thing that it does if tje number its smaller
print("you won bud1!1!1!1!1") # the win message, since i havent added a thing that does something when its correct it will move to this print
# the < its if the number in the right its bigger example : 4 < 5 since 5 its bigger , and > if the number in the left its bigger