import random



cm =random.randint(1,10)
attempt =0
max_attempt = 7

while attempt<max_attempt :
    guess = int(input("enter your choice from 1 to 10"))
    attempt+=1
    

    if guess < cm :
        print("to low")
    elif guess >cm :
        print("to high")
    else:
       print(f"you won the game{attempt}")
       break
    print(f"You have {max_attempt - attempt} attempts left\n")
else:
    print("correct ansewer is ",cm)
    

        