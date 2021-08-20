import random

min=1
max=6

roll_more="yes"

while roll_more =="yes":
    print("ROLLING DICE")
    print("YOU ROLLED")
    print(random.randint(min,max))
    print(random.randint(min,max))
    roll_more = input("ROLL AGAIN?: ")
