print("welcome")
player=input('do u want to play?')
if player.lower() != "yes":
    quit()
print("ok lets play")   
SCORE=0 
question = input(" What is the capital of France?")
if question.lower() == "paris":
    print("correct")
    SCORE+=1
else:
    print("wrong answer")
question = input(" Who wrote the play Romeo and Juliet?")
if question.lower() == "william shakespeare":
    print("correct")
    SCORE+=1
else:
    print("wrong answer")
question = input("What is the largest planet in our solar system?")
if question.lower() == "jupiter":
    print("correct")
    SCORE+=1
else:
    print("wrong answer")
question = input(" How many bones are in the adult human body")
if question == "206":
    print("correct")
    SCORE+=1
else:                                                               #u can add many question as you wish
    print("wrong answer")
question = input(" Which planet is known as the Red Planet?")
if question.lower() == "mars":
    print("correct")
    SCORE+=1
else:
    print("wrong answer")

print("your score is "+str(SCORE))