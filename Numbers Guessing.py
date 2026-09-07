import random

secrets = random.randint(1,100)
guess = 0
attempts = 0

while attempts < 7 :
    guess = int(input("enter a number: "))
    if guess < 1 :
        print("invaild number try again")
    else:
        attempts += 1
        if guess > secrets :
            print("too high")
        elif guess < secrets :
            print("too low")
        else:
            print("you got, nice work!!!")
            break

if guess != secrets:
    print(f"you lose, maximum tries reached {attempts}")